# coding:utf-8

from . import app_seller
from saihan import db
from flask import render_template,request, url_for
from saihan.models import Product, Profile
from flask_login import current_user, login_required
# from saihan.models import ...


@app_seller.route("/items")
def seller_items():
    profile = Profile.query.filter_by(user_id=current_user.id).first()
    products = Product.query.filter_by(seller_id=current_user.id)
    # print(url_for("static", filename="images/products/"+products[0].attachments[0].filename))
    return render_template("seller_items.html",
                            profile=profile,
                            products=products)


@app_seller.route("/order",methods=["GET","POST"])
def seller_order():
    if request.method == "GET":
        return render_template("seller_order.html")
    else:
        pass
        


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
    