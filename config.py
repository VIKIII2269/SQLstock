import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/assignment'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
