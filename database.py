from model import *


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_story(name, time, title, story):
    story1 = Story(
        name=name,
        time=time,
        title=title,
        story=story
        )
    session.add(story1)
    session.commit()

def query_all():
	all_stories = session.query(Story).all()
	return all_stories

def delete_all():
	session.query(Story).delete()
	session.commit()
