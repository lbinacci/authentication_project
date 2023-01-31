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
    query_result = db.get_user(username=response['username'])
    if query_result and psw_check(response['password'], query_result.password):
        if query_result.two_factor_auth:
            return redirect("two_fa_login")
        else:
            return jsonify({'message': 'User logged successfully'}), 200
    elif not query_result:
        return jsonify({'message': 'User: ' + response['username'] + 'doesnt exist'}), 200


@app.route('/registration', methods=['POST'])
def registration():

    if request.method == 'POST':
        response = request.form

        # date must have form year-month-day
        if db.get_user(username=response['username']):
            return jsonify({'error': 'Username already exists'}), 409
        if db.get_user(email=response['email']):
            return jsonify({'error': 'Email already exists'}), 409
        if not re.match(r"[^@]+@[^@]+\.[^@]+", response['email']):
            return jsonify({'error': 'Invalid email format'}), 400

        try:
            db.insert_user(response['username'], response['password'], response['email'], response['birth_date'], response['first_name'],
                           response['last_name'], bool(response['otp']))
        except Exception as e:
            return jsonify({'error': str(e)}), 500

        return jsonify({'message': 'User registered successfully'}), 201


@app.route('/2fa_login', methods=['POST'])
def two_fa_login():
    pass

app.run()