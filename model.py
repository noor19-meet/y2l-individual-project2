from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, PickleType
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	__tablename__="users"
	user_id=Column(Integer,primary_key=True)
	name=Column(String)
	email=Column(String)
	password=Column(String)