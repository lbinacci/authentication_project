import re

from flask import Flask, request, jsonify, redirect, render_template, url_for
from flask_login import LoginManager, login_user, login_required
from config.app_config import MysqlConfiguration
from dao.MySQL_users_DAO import MySqlUsersDao
from utils.flask_utils import User
from utils.login_utils import psw_check

app = Flask(__name__, template_folder='templates')
app.secret_key = "a_secret_key"

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
db = MySqlUsersDao(MysqlConfiguration.HOST.value, MysqlConfiguration.USER.value,
                   MysqlConfiguration.PASSWORD.value, MysqlConfiguration.DATABASE.value)

@login_manager.user_loader
def load_user(username):
    user = db.get_user(username=username)
    if user:
        return User(user.id, user.username, user.password, user.email)
    else:
        return None


@app.route('/registration')
def registration_form():
    return render_template('registration.html')


@app.route('/login')
def login_template():
    return render_template('login.html')


def two_fa_template():
    return render_template('otp.html')


@app.route('/example')
@login_required
def example():
    return render_template('example.html')


@app.route('/login_user', methods=['POST'])
def login():
    response = request.form
    # query to get user data
    query_result = db.get_user(username=response.get('username'))

    # if the user exists and if the password is correct you can go to the next step or complete the login
    if query_result and psw_check(response.get('password').encode('utf-8'), query_result.password.encode('utf-8')):

        # if 2fa is enabled
        if query_result.two_factor_auth:

            return redirect("two_fa_login")

        else:
            # logged in
            user = User(query_result.id, query_result.username, query_result.password, query_result.email)
            login_user(user)
            return redirect(url_for("example"))
            # return jsonify({'message': 'User logged successfully'}), 201
    elif not query_result:
        return jsonify({'message': 'User: ' + response.get('username') + ' doesnt exist'}), 208
    # gestire password


@app.route('/register_user', methods=['POST'])
def registration():
    if request.method == 'POST':
        response = request.form
        # date must have form year-month-day
        if db.get_user(username=response.get('username')):
            return jsonify({'error': 'Username already exists'}), 409
        if db.get_user(email=response.get('email')):
            return jsonify({'error': 'Email already exists'}), 409
        if not re.match(r"[^@]+@[^@]+\.[^@]+", response.get('email')):
            return jsonify({'error': 'Invalid email format'}), 400

        try:
            db.insert_user(response.get('username'), response.get('password'), response.get('email'),
                           response.get('birth_date'),
                           response.get('first_name'), response.get('last_name'), bool(response.get('otp')))
        except Exception as e:
            return jsonify({'error': str(e)}), 500

        return jsonify({'message': 'User registered successfully'}), 201


@app.route('/2fa_login', methods=['POST'])
def two_fa_login():
    pass


app.run()
