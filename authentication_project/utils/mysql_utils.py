
from config.app_config import MysqlConfiguration
from dao.MySQL_users_DAO import MySqlUsersDao
from model.db_models import Base


def init_mysql_users_db():
    db = MySqlUsersDao(MysqlConfiguration.HOST.value, MysqlConfiguration.USER.value,
                       MysqlConfiguration.PASSWORD.value, MysqlConfiguration.DATABASE.value)
    # User.__table__.drop(engine)
    engine, session = db.create_session()
    Base.metadata.create_all(engine)


