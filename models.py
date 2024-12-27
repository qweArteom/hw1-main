from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Departure(Base):
    __tablename__ = 'departures'
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)

class Tour(Base):
    __tablename__ = 'tours'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    departure = Column(String, nullable=False)
    picture = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    stars = Column(Integer, nullable=False)
    country = Column(String, nullable=False)
    nights = Column(Integer, nullable=False)
    date = Column(String, nullable=False)

engine = create_engine('sqlite:///travel.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()