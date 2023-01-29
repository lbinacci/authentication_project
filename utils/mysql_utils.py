import logging

import mysql.connector
from sqlalchemy import create_engine

from config.app_config import MysqlConfiguration
from model.db_models import Base


# def init_mysql_users_db():
#     mydb = mysql.connector.connect(
#         host=MysqlConfiguration.HOST,
#         user=MysqlConfiguration.USER,
#         password=MysqlConfiguration.PASSWORD,
#         database=MysqlConfiguration.DATABASE
#     )
#
#     cursor = mydb.cursor()
#     try:
#         cursor.execute(MysqlConfiguration.CREATE_USERS_TABLE)
#
#     except Exception as e:
#         logging.error(e)
#
#     finally:
#         cursor.close()
#         mydb.close()


def init_mysql_users_db():
    engine = create_engine(f"mysql://{MysqlConfiguration.USER.value}:{MysqlConfiguration.PASSWORD.value}"
                           f"@{MysqlConfiguration.HOST.value}/{MysqlConfiguration.DATABASE.value}")

    Base.metadata.create_all(engine)


if __name__ == '__main__':
    init_mysql_users_db()


