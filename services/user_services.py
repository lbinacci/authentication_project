import re

from flask import Flask, request, jsonify

from config.app_config import MysqlConfiguration
from dao.MySQL_users_DAO import MySqlUsersDao

app = Flask(__name__)

db = MySqlUsersDao(MysqlConfiguration.HOST.value, MysqlConfiguration.USER.value,
                   MysqlConfiguration.PASSWORD.value, MysqlConfiguration.DATABASE.value)




@app.route('/login', methods=['POST'])
def login():
    pass


@app.route('/registration', methods=['POST'])
def registration():

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        if db.get_user(username=username):
            return jsonify({'error': 'Username already exists'}), 409
        if db.get_user(email=email):
            return jsonify({'error': 'Email already exists'}), 409
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return jsonify({'error': 'Invalid email format'}), 400

        return jsonify({'message': 'User registered successfully'}), 201


@app.route('/2fa_login', methods=['POST'])
def two_fa_login():
    pass

app.run()