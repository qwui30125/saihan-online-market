# coding:utf-8

from . import app_admin
from saihan import db
from flask import render_template
from flask_login import current_user
from saihan.models import User, Profile, Authenticate, Product , Order
# from saihan.models import ...

@app_admin.route("/user/")
@app_admin.route("/user/<int:page>")
def admin_user(page=1):
    admin = current_user
    # user_cout = len(User.query.all())
    # print(user_cout)
    users = User.query.limit(5).offset((page-1)*5)
    for user in users:
        # print(user.profile)
        user.authenticate = Authenticate.query.filter_by(user_id=user.id).first()
    return render_template("admin_user.html",
                           users=users)

@app_admin.route("/product/")
@app_admin.route("/product/<int:page>")
def admin_product(page=1):
    products = Product.query.limit(5).offset((page-1)*5)
    return render_template("admin_product.html",
                           products=products)

@app_admin.route("/order/")
@app_admin.route("/order/<int:page>")
def admin_order(page=1):
    orders = Order.query.limit(5).offset((page-1)*5)
    pro_list = []
    for order in orders:
        product = Product.query.filter_by(id = order.product_id)
        pro_list.append(product)
    print(pro_list)
    return render_template("admin_order.html",pro_list = pro_list,orders = orders)

@app_admin.route("/adver/")
@app_admin.route("/adver/<int:page>")
def admin_adver(page=1):
    return render_template("admin_adver.html")