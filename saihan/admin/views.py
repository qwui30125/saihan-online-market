# coding:utf-8

from . import app_admin
from saihan import db
from flask import render_template
from flask_login import current_user
from saihan.models import User, Profile, Authenticate, Product
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
    # profile = Profile.query.limit(5)
    # profile = Profile.query.limit(5).offset(6)
    # profile = Profile.query.count(Profile.id)
    # profile.id 
    # page = 2
    # n = 5
    # m = 5*(page-1)
    # product = Product.query.limit()
    order_list = [
        {
            "pro_name":Product.name,
            "order_id":Order.id,
            "statu":Order.status,
            "buyer_id":Order.buyer_id,
            "pro_pic":Order.attachments,
            "order_price":Order.price,
            "seller_id":Order.seller_id
        },
        {
            "pro_name":Product.name,
            "order_id":Order.id,
            "statu":Order.status,
            "buyer_id":Order.buyer_id,
            "pro_pic":Order.attachments,
            "order_price":Order.price,
            "seller_id":Order.seller_id 
        },
        {
            "pro_name":Product.name,
            "order_id":Order.id,
            "statu":Order.status,
            "buyer_id":Order.buyer_id,
            "pro_pic":Order.attachments,
            "order_price":Order.price,
            "seller_id":Order.seller_id
        },
        {
            "pro_name":Product.name,
            "order_id":Order.id,
            "statu":Order.status,
            "buyer_id":Order.buyer_id,
            "pro_pic":Order.attachments,
            "order_price":Order.price,
            "seller_id":Order.seller_id 
        },
        {
            "pro_name":Product.name,
            "order_id":Order.id,
            "statu":Order.status,
            "buyer_id":Order.buyer_id,
            "pro_pic":Order.attachments,
            "order_price":Order.price,
            "seller_id":Order.seller_id 
        }
    ]
    return render_template("admin_order.html",order_list=order_list)

@app_admin.route("/adver/")
@app_admin.route("/adver/<int:page>")
def admin_adver(page=1):
    ad_list = [
        {
            "ad_id":"AdverSH0002",
            "ad_name":"赵吏",
            "ad_pic":"static/images/li.jpeg",
            "ad_price":""
        }
    ]
    return render_template("admin_adver.html",ad_list = da_list)