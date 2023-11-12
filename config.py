# config.py

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default-secret-key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://appuser:password@localhost/task_manager'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
