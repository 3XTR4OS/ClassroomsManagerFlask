import json
from flask import Flask
from .models import db

cabs_app = Flask(__name__)
config_path = 'static//config.json'
with open(config_path, mode='r', encoding='UTF8') as file:
    json_file = json.load(file)
    __login = json_file['database_login']
    __password = json_file['database_password']
    __host = json_file['database_host']
    __db_name = json_file['database_name']

connection_string: str = f'postgresql+psycopg2://{__login}:{__password}@{__host}/{__db_name}'
cabs_app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
cabs_app.config.from_object('config')
db.init_app(cabs_app)

from classrooms_app import views

