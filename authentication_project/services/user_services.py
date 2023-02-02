import re

from flask import Flask, request, jsonify, redirect, render_template, url_for, flash
from flask import session
from flask_login import LoginManager, login_user, login_required, logout_user

from config.app_config import MysqlConfiguration
from config.app_constants import PSW, MAIL, USERNAME, BIRTHDATE, FIRST_NAME, LAST_NAME
from dao.MySQL_users_DAO import MySqlUsersDao
from utils.flask_utils import User
from utils.login_utils import psw_check
from utils.send_email import send_otp_mail

app = Flask(__name__, template_folder='templates')
app.secret_key = "a_secret_key"

login_manager = LoginManager(app)
login_manager.init_app(app)

db = MySqlUsersDao(MysqlConfiguration.HOST.value, MysqlConfiguration.USER.value,
                   MysqlConfiguration.PASSWORD.value, MysqlConfiguration.DATABASE.value)


@app.route('/registration')
def registration_form():
    return render_template('registration.html')


@app.route('/login')
def login_template():
    return render_template('login.html')


@app.route('/logged_in')
@login_required
def logged_in_template():
    return render_template('logged_in.html')


@app.route('/two_fa_login_template')
def two_fa_login_template():
    if USERNAME not in session:
        return redirect(url_for('login_template'))
    user = db.get_user(username=session[USERNAME])

    if user is None:
        flash('something went wrong')
        return redirect(url_for('login_template'))
    otp = send_otp_mail()
    print(otp)
    db.update_user(user=user.username, otp=otp)
    return render_template('otp.html')


@app.route('/login_user', methods=['POST'])
def login_user_back():
    response = request.form
    # query to get user data
    query_result = db.get_user(username=response.get(USERNAME))

    # if the user exists and if the password is correct you can go to the next step or complete the login
    if query_result and psw_check(response.get('password').encode('utf-8'), query_result.password.encode('utf-8')):

        # if 2fa is enabled
        if query_result.two_factor_auth:
            session[USERNAME] = query_result.username

            return redirect(url_for("two_fa_login_template"))

        else:
            # logged in
            user = User(query_result.id, query_result.username, query_result.password, query_result.email)
            login_user(user)
            return redirect(url_for("logged_in_template"))

    return redirect(url_for("login_template"))


@app.route('/register_user', methods=['POST'])
def registration():
    if request.method == 'POST':
        response = request.form
        # date must have form year-month-day
        if db.get_user(username=response.get(USERNAME)):  # check if the username already exists
            return jsonify({'error': 'Username already exists'}), 409
        if db.get_user(email=response.get('email')):  # check if the username already exists
            return jsonify({'error': 'Email already exists'}), 409
        if not re.match(r"[^@]+@[^@]+\.[^@]+", response.get('email')):  # check if the email format is wrong
            return jsonify({'error': 'Invalid email format'}), 400

        try:
            # insert new user in db
            db.insert_user(response.get(USERNAME), response.get(PSW), response.get(MAIL),
                           response.get(BIRTHDATE),
                           response.get(FIRST_NAME), response.get(LAST_NAME), bool(response.get('otp')))
        except Exception as e:
            return jsonify({'error': str(e)}), 500

        return jsonify({'message': 'User registered successfully'}), 201


@app.route('/two_fa_login', methods=['POST'])
def two_fa_login():
    response = request.form
    # check if the user is active
    if USERNAME not in session:
        return redirect(url_for('login_template'))

    user = db.get_user(username=session[USERNAME])
    # if the user exists
    if user is None:
        flash('something went wrong')
        return redirect(url_for('login_template'))

    # if the otp is correct login in
    if user.otp == response.get('otp'):
        user = User(user.id, user.username, user.password, user.email)
        login_user(user)
        return redirect(url_for("logged_in_template"))
    flash('wrong otp')
    return redirect(url_for("login_template"))


@app.route("/logout")
@login_required
def logout_user_():
    logout_user()
    session.pop(USERNAME, None)
    return redirect(url_for("login_template"))


@login_manager.user_loader
def load_user(id):
    user = db.get_user(id=id)
    if user:
        return user
    else:
        return None
