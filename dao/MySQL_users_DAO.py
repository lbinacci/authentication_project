from dataclasses import dataclass
from datetime import datetime

import bcrypt
import mysql.connector
from mysql.connector import MySQLConnection
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.db_models import User


class MySqlUsersDao:
    def __init__(self, host, username, password, database_name):
        """
        The above function is a constructor that takes in the host, username, password, and database name as
        parameters and assigns them to the class variables.
        
        :param host: The hostname of the database server. This is usually localhost, meaning the database
        server is running on the same computer as the Python script
        :param username: The username you use to log into your database
        :param password: the password for the user
        :param database_name: The name of the database you want to connect to
        """
        self.host = host
        self.username = username
        self.password = password
        self.database_name = database_name

    def insert_user(self, username: str, password: str, email: str, birthdate: str, first_name: str, last_name: str,
                    two_factor_auth: bool):
        """
        It takes in a bunch of user information and inserts it into the database.
        
        :param username: string
        :param password: the password the user entered
        :param email: str
        :param birthdate: datetime.date(year, month, day)
        :param first_name: str
        :param last_name: str,
        :param two_factor_auth: boolean
        """

        engine = create_engine(f"mysql://{self.username}:{self.password}@{self.host}/{self.database_name}")
        session_maker = sessionmaker(bind=engine)
        session = session_maker()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        new_user = User(
            username=username,
            password=hashed_password.decode('utf-8'),
            email=email,
            birthdate=birthdate,
            first_name=first_name,
            last_name=last_name,
            two_factor_auth=two_factor_auth
        )
        session.add(new_user)
        session.commit()

        engine.dispose()

    def get_user(self, username: str = None, email: str = None):
        engine = create_engine(f"mysql://{self.username}:{self.password}@{self.host}/{self.database_name}")
        session_maker = sessionmaker(bind=engine)
        session = session_maker()

        # restituisce None se non trova nulla
        if username:
            query_result = session.query(User).filter_by(username=username).first()
        else:
            query_result = session.query(User).filter_by(email=email).first()

        engine.dispose()
        return query_result


# insert_user("ewqewewdq", "brtewqeudsades", "dsdads@dsa2dsa.com", "1990-01-01", "John", "Doe", False)
if __name__ == '__main__':
    db = MySqlUsersDao("localhost", "user", "password", "users_db")

    print(db.get_user("mauretto"))
    db.insert_user("ewqewew3213123dq", "brtewqeudsades", "dsdads@dsa2321dsa.com", "1990-01-01", "John", "Doe", False)
