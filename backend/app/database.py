from sqlalchemy import create_engine 
# * create_engine is used to create a connection to the database
from sqlalchemy.ext.declarative import declarative_base
# * declarative_base is used to create a base class for our models
# * with declarative_base, we can write in python way and it will be translated to SQL
# * used for creating the tables in the database
from sqlalchemy.orm import sessionmaker
# * sessionmaker is used to create a session for interacting with the database
from app.config import settings

engine = create_engine(settings.DATABASE_URL)
# * create_engine takes the database URL from the settings and creates a connection to the database

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# * opens a session to the database, basically database related functions

Base = declarative_base()

def get_db():
    db = SessionLocal() # * one session for each request, we will use this session to interact with the database
    try:
        yield db
    finally:
        db.close()

        