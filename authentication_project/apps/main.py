from services.user_services import app
from utils.mysql_utils import init_mysql_users_db
import logging

try:
    init_mysql_users_db()
except Exception as e:
    logging.error("can't create table, error:" + str(e))


app.run()
