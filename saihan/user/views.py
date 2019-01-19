# coding:utf-8

from . import app_user
from saihan import db
from flask import render_template
# from saihan.models import ...

@app_user.route("/info")
def info():
    return render_template("user_info.html")

@app_user.route("/order")
def order():
    return render_template("user_order.html")

@app_user.route("/site")
def site():
    return render_template("user_site.html")