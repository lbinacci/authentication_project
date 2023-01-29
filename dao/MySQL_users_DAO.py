from dataclasses import dataclass

import bcrypt
import mysql.connector
from mysql.connector import MySQLConnection
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.db_models import User


@dataclass
class MySqlUsersDao:
    def __init__(self, host, username, password, database_name):
        self.host = host
        self.username = username
        self.password = password
        self.database_name = database_name
        self.engine = create_engine(f"mysql://{self.username}:{self.password}@{self.host}/{self.database_name}")

    def insert_user(self, username, password, email, birthdate, first_name, last_name, two_factor_auth):

        session_maker = sessionmaker(bind=self.engine)
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


# insert_user("ewqewewdq", "brtewqeudsades", "dsdads@dsa2dsa.com", "1990-01-01", "John", "Doe", False)
