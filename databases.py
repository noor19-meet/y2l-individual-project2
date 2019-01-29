from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind = engine)
session_factory = scoped_session(DBSession)
session = session_factory()

def add_user(name, email, password):
	
	user_object = User(
	name=name,
	email = email,
	password = password)
	session.add(user_object)
	session.commit()

def query_by_id(activity_id):
	activity = session.query(Activity).filter_by(
		activity_id=activity_id).first()
	return activity

def query_all_activities():
	activities = session.query(Activity).all()
	return activities

def query_by_name(name):
	activities=session.query(Activity).filter_by(
		name=name).all()
	return activities

def query_user_by_email(email):
	user = session.query(User).filter_by(email=email).first()
	return user

# 	print([a.email for a in session.query(User).all()])