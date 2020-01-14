
from model import *


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

cart = []

def add_login(user_name, anonimos_name):
    users = login(
        user_name=user_name,
        anonimos_name=anonimos_name,
    session.add(users)
    session.commit()


