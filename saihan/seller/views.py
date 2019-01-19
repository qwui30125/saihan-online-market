# coding:utf-8

from . import app_seller
from saihan import db
from flask import render_template,request
from saihan.models import Product
# from saihan.models import ...


@app_seller.route("/items")
def seller_items():
    dic1={
        'name':'Product.name',
        'price':'Product.price',
        'heji':5000,
        'use':'删除',
        'photo':"ProductMedia.filename"
    }
    dic2={
        'name':'Product.name',
        'price':'Product.price',
        'heji':5000,
        'use':'删除',
        'photo':"ProductMedia.filename"
    }

    users = [dic1,dic2]
    return render_template("seller_items.html",users=users)


@app_seller.route("/order",methods=["GET","POST"])
def seller_order():
    if request.method == "GET":
        return render_template("seller_order.html")
    else:
        


@app_seller.route("/release", methods=["GET", "POST"])
def seller_release():
    if request.method == "GET":
        return render_template("seller_release.html")
    else:
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        picture = request.form.get('picture')
        user = Product(name=name,description=description,price=price,attachments=picture)
        db.session.add(user)
    