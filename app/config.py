import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:postgres@localhost:5432/bn_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    
