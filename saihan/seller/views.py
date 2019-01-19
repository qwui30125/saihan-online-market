# coding:utf-8

from . import app_seller
from saihan import db
from flask import render_template
# from saihan.models import ...

@app_seller.route("/items")
def seller_items():
    dic1={
        'name':'Casio/卡西欧 EX-TR350',
        'price':5000,
        'heji':5000,
        'use':'删除',
        'photo':"static/天天生鲜项目页面/images/adv01.jpg"
    }
    dic2={
        'name':'Casio/卡西欧 EX-TR350',
        'price':5000,
        'heji':5000,
        'use':'删除',
        'photo':"static/天天生鲜项目页面/images/adv01.jpg"
    }
    user = [dic1,dic2]
    return render_template("seller_items.html",user=user)


@app_seller.route("/order")
def seller_order():
    return render_template("seller_order.html")


@app_seller.route("/release")
def seller_release():
    return render_template("seller_release.html")