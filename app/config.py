"""Конфигурация основного приложения и базы данных"""

class Configuration:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost/flask_blog'
    SECRET_KEY = 'something very secret'