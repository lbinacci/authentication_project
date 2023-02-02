from enum import Enum


class MysqlConfiguration(Enum):
    HOST = "localhost"
    USER = "user"
    PASSWORD = "password"
    DATABASE = "users_db"
    CREATE_USERS_TABLE = "CREATE TABLE users (" \
                         "username VARCHAR(255) PRIMARY KEY," \
                         "password VARCHAR(255) NOT NULL," \
                         "email VARCHAR(255) NOT NULL," \
                         "birthdate DATE NOT NULL," \
                         "first_name VARCHAR(255) NOT NULL," \
                         "last_name VARCHAR(255) NOT NULL," \
                         "two_factor_auth BOOLEAN NOT NULL);" \
                         "UNIQUE (email)"


if __name__ == '__main__':
    print(MysqlConfiguration.DATABASE)