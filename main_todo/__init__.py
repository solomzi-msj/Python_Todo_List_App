from flask import Flask
from main_todo import forms

app = Flask(__name__)
app.config['SECRET_KEY'] = 'djfhIUFHEFB;ijJ;AG;h4aa3aga4g8ghsr8jtdj'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from main_todo import routes
from main_todo import models
from main_todo import helper_functions