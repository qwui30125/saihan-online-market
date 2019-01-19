# coding:utf-8

from . import app_admin
from saihan import db
from flask import render_template
# from saihan.models import ...

@app_admin.route("/admin_userinfo")
def admin_userinfo():
    user_list = [
        {
            "user_id":User.id,
            "user_name":Profile.nickname,
            "user_pic":Profile.avatar,
            "user_type":User.type,
            "check":Authenticate.status,
            "phone_number":Profile.mobile,
            "addr":Profile.addess
            },
        {
             "user_id":User.id,
            "user_name":Profile.nickname,
            "user_pic":Profile.avatar,
            "user_type":User.type,
            "check":Authenticate.status,
            "phone_number":Profile.mobile,
            "addr":Profile.addess
         },
         {
             "user_id":User.id,
            "user_name":Profile.nickname,
            "user_pic":Profile.avatar,
            "user_type":User.type,
            "check":Authenticate.status,
            "phone_number":Profile.mobile,
            "addr":Profile.addess
         },
         {
             "user_id":User.id,
            "user_name":Profile.nickname,
            "user_pic":Profile.avatar,
            "user_type":User.type,
            "check":Authenticate.status,
            "phone_number":Profile.mobile,
            "addr":Profile.addess
         },
         {
             "user_id":User.id,
            "user_name":Profile.nickname,
            "user_pic":Profile.avatar,
            "user_type":User.type,
            "check":Authenticate.status,
            "phone_number":Profile.mobile,
            "addr":Profile.addess
         }
    ]
    return render_template("admin_center.html",u_list = user_list)

@app_admin.route("/admin_productinfo")
def admin_productinfo():
    pro_list=[
        {
            "pro_pic":Product.attachments,
            "id":Product.id,
            "pro_name":Product.name,
            "seller_name":Product.seller_name,
            "price":Product.price,
            "status":Product.status
        },
        {
            "pro_pic":Product.attachments,
            "id":Product.id,
            "pro_name":Product.name,
            "seller_name":Product.seller_name,
            "price":Product.price,
            "status":Product.status
        },
        {
            "pro_pic":Product.attachments,
            "id":Product.id,
            "pro_name":Product.name,
            "seller_name":Product.seller_name,
            "price":Product.price,
            "status":Product.status
        },
        {
            "pro_pic":Product.attachments,
            "id":Product.id,
            "pro_name":Product.name,
            "seller_name":Product.seller_name,
            "price":Product.price,
            "status":Product.status
        },
        {
            "pro_pic":Product.attachments,
            "id":Product.id,
            "pro_name":Product.name,
            "seller_name":Product.seller_name,
            "price":Product.price,
            "status":Product.status
        }
    ]
    return render_template("admin_productinfo.html",pro_list = pro_list)

@app_admin.route("/admin_order/<int:page>")
def admin_order():
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

@app_admin.route("/admin_adver")
def admin_adver():
    ad_list = [
        {
            "ad_id":"AdverSH0002",
            "ad_name":"赵吏",
            "ad_pic":"static/images/li.jpeg",
            "ad_price":""
        }
    ]
    return render_template("admin_adver.html",ad_list = da_list)