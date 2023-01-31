import re

from flask import Flask, request, jsonify, redirect, render_template

from config.app_config import MysqlConfiguration
from dao.MySQL_users_DAO import MySqlUsersDao
from utils.login_utils import psw_check

app = Flask(__name__, template_folder='templates')

db = MySqlUsersDao(MysqlConfiguration.HOST.value, MysqlConfiguration.USER.value,
                   MysqlConfiguration.PASSWORD.value, MysqlConfiguration.DATABASE.value)


@app.route('/')
def index():
    return render_template('registration.html')


@app.route('/login', methods=['POST'])
def login():
    response = request.form
    query_result = db.get_user(username=response.get('username'))
    if query_result and psw_check(response.get('password'), query_result.password):
        if query_result.two_factor_auth:
            return redirect("two_fa_login")
        else:
            return jsonify({'message': 'User logged successfully'}), 200
    elif not query_result:
        return jsonify({'message': 'User: ' + response.get('username') + 'doesnt exist'}), 200


@app.route('/registration', methods=['POST'])
def registration():
    if request.method == 'POST':
        response = request.form
        ciao = response.get('otp')
        # date must have form year-month-day
        if db.get_user(username=response.get('username')):
            return jsonify({'error': 'Username already exists'}), 409
        if db.get_user(email=response.get('email')):
            return jsonify({'error': 'Email already exists'}), 409
        if not re.match(r"[^@]+@[^@]+\.[^@]+", response.get('email')):
            return jsonify({'error': 'Invalid email format'}), 400

        try:
            db.insert_user(response.get('username'), response.get('password'), response.get('email'), response.get('birth_date'),
                           response.get('first_name'), response.get('last_name'), bool(response.get('otp')))
        except Exception as e:
            return jsonify({'error': str(e)}), 500

        return jsonify({'message': 'User registered successfully'}), 201


@app.route('/2fa_login', methods=['POST'])
def two_fa_login():
    pass


app.run()
