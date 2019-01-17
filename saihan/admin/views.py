# coding:utf-8

from . import app_admin
from saihan import db
from flask import render_template
# from saihan.models import ...

@app_admin.route("/admin_userinfo")
def admin_userinfo():
    return render_template("admin_center.html")

@app_admin.route("/admin_productinfo")
def admin_productinfo():
    return render_template("admin_productinfo.html")

@app_admin.route("/admin_order")
def admin_order():
    return render_template("admin_order.html")

@app_admin.route("/admin_adver")
def admin_adver():
    return render_template("admin_adver.html")