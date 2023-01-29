import logging

import mysql.connector
from sqlalchemy import create_engine

from config.app_config import MysqlConfiguration
from dao.MySQL_users_DAO import MySqlUsersDao
from model.db_models import Base


def init_mysql_users_db():
    engine = create_engine(f"mysql://{MysqlConfiguration.USER.value}:{MysqlConfiguration.PASSWORD.value}"
                           f"@{MysqlConfiguration.HOST.value}/{MysqlConfiguration.DATABASE.value}")

    Base.metadata.create_all(engine)

if __name__ == '__main__':
    # init_mysql_users_db()

    MySqlUsersDao()


