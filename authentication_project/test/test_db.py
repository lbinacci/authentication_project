import time
import unittest
import bcrypt

from dao.MySQL_users_DAO import MySqlUsersDao


class MySqlUsersDaoTest(unittest.TestCase):
    def setUp(self):
        self.db = MySqlUsersDao("localhost", "user", "password", "users_db")
        self.username = "test_user"
        self.password = "test_password"
        self.email = "test_user@email.com"
        self.birthdate = "2000-01-01"
        self.first_name = "Test"
        self.last_name = "User"
        self.two_factor_auth = False

    def tearDown(self):
        time.sleep(1)

    def test_get_insert_user(self):
        self.db.insert_user(self.username, self.password, self.email, self.birthdate, self.first_name, self.last_name, self.two_factor_auth)
        user = self.db.get_user(username=self.username)
        self.assertIsNotNone(user)
        self.assertEqual(user.username, self.username)
        self.assertTrue(bcrypt.checkpw(self.password.encode('utf-8'), user.password.encode('utf-8')))
        self.assertEqual(user.email, self.email)
        self.assertEqual(str(user.birthdate), self.birthdate)
        self.assertEqual(user.first_name, self.first_name)
        self.assertEqual(user.last_name, self.last_name)
        self.assertEqual(user.two_factor_auth, self.two_factor_auth)

    def test_update_user(self):
        # self.db.insert_user(self.username, self.password, self.email, self.birthdate, self.first_name, self.last_name, self.two_factor_auth)
        new_otp = '11112222'
        self.db.update_user(user=self.username, otp=new_otp)
        user = self.db.get_user(username=self.username)
        self.assertEqual(user.otp, new_otp)

