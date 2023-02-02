from services.user_services import app
from utils.mysql_utils import init_mysql_users_db
import logging
import time


time.sleep(10)
try:
    init_mysql_users_db()
except Exception as e:
    logging.error("can't create table, error:" + str(e))

app.run(host='0.0.0.0')
