from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, String, Date, Boolean

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    username = Column(String(255), primary_key=True)
    password = Column(String(255))
    email = Column(String(255), unique=True)
    birthdate = Column(Date)
    first_name = Column(String(255))
    last_name = Column(String(255))
    two_factor_auth = Column(Boolean)
