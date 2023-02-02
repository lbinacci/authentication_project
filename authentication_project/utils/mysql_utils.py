from sqlalchemy import create_engine

from config.app_config import MysqlConfiguration
from model.db_models import Base


def init_mysql_users_db():
    engine = create_engine(f"mysql://{MysqlConfiguration.USER.value}:{MysqlConfiguration.PASSWORD.value}"
                           f"@{MysqlConfiguration.HOST.value}/{MysqlConfiguration.DATABASE.value}")

    Base.metadata.create_all(engine)

