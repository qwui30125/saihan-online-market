# coding:utf-8

from . import app_seller
from saihan import db
from flask import render_template
# from saihan.models import ...

@app_seller.route("/items")
def seller_items():
    return render_template("seller_items.html")


@app_seller.route("/order")
def seller_order():
    return render_template("seller_order.html")


@app_seller.route("/release")
def seller_release():
    return render_template("seller_release.html")