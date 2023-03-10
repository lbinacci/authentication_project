from flask_login import UserMixin
from sqlalchemy import Column, String, Date, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base, UserMixin):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), unique=True)
    password = Column(String(255))
    email = Column(String(255), unique=True)
    birthdate = Column(Date)
    first_name = Column(String(255))
    last_name = Column(String(255))
    two_factor_auth = Column(Boolean)
    otp = Column(String(255))
