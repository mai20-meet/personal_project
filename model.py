from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Story(Base):
   __tablename__ = 'mystory'
   id = Column(Integer, primary_key=True)
   name= Column(String)
   time=Column(String)
   title=Column(String)
   story=Column(String)

   def __repr__(self):
   		return str(self.__dict__)
  



