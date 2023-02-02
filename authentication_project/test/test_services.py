import unittest

import requests

class logged_in_test(unittest.TestCase):

    def test_registration_form(self):
        response = requests.get("http://localhost:5000/registration")
        assert response.status_code == 200

    def test_login_template(self):
        response = requests.get("http://localhost:5000/login")
        assert response.status_code == 200

    def test_logged_in_template(self):
        # Need to log in first to access the endpoint
        response = requests.get("http://localhost:5000/logged_in")
        assert response.status_code == 401

    def test_two_fa_login_template(self):
        # Need to log in first to access the endpoint
        response = requests.get("http://localhost:5000/two_fa_login_template")
        assert response.status_code == 200

    def test_login_user_back(self):
        response = requests.post("http://localhost:5000/login_user", data={
            "username": "test_user_service",
            "password": "test_password_service"
        })
        assert response.status_code == 200

    def test_registration(self):
        response = requests.post("http://localhost:5000/register_user", data={
            "username": "test_user_service",
            "password": "test_password_service",
            "email": "test@test.com",
            "birthdate": "2000-01-01",
            "first_name": "Test",
            "last_name": "User",
            "otp": False
        })
        assert response.status_code == 201

# def test_two_fa_login():
#     # Need to log in and access two_fa_login_template first to access this endpoint
#     response = requests.post("http://localhost:5000/two_fa_login", data={
#         "otp_code": "1234"
#     })
#     assert response.status_code == 302
