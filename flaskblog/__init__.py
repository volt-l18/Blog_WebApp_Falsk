from ast import Import
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from jinja2.nodes import ImportedName
from sqlalchemy.orm import backref

app = Flask(__name__)
app.config['SECRET_KEY'] = '457e9068bdca2a4d6cdf300d3e510c49'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from flaskblog import routes
