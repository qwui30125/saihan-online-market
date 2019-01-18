# coding:utf-8

from . import app_user
from saihan import db
from flask import render_template
# from saihan.models import ...

@app_user.route("index")
def index():
    return "user index"
