# coding:utf-8

from . import app_admin
from saihan import db
from flask import render_template,redirect,url_for
from flask_login import current_user
from saihan.models import User, Profile, Authenticate, Product , Order,ProductMedia
# from saihan.models import ...

@app_admin.route("/user/")
@app_admin.route("/user/<int:page>")
def admin_user(page=1):
    admin = current_user
    # user_cout = len(User.query.all())
    # print(user_cout)
    users = Profile.query.limit(5).offset((page-1)*5)
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
    pic = []
    for order in orders:
        pro = ProductMedia.query.filter_by(id = order.product_id).first()
        pic.append(pro.filename)
    return render_template("admin_order.html",pro_list = pro_list,orders = orders,pic = pic)

@app_admin.route("/adver/")
@app_admin.route("/adver/<int:page>")
def admin_adver(page=1):
    return render_template("admin_adver.html")

# 以下为删除信息视图函数
@app_admin.route('/remove_user/<int:user_id>')
def remove_user(user_id):
    item = User.query.filter_by(id=user_id).first()
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("admin.admin_user"))

@app_admin.route('/remove_order/<int:order_id>')
def remove_order(order_id):
    item = Order.query.filter_by(id=order_id).first()
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("admin.admin_order"))

@app_admin.route('/remove_product/<int:product_id>')
def remove_product(product_id):
    item = Product.query.filter_by(id=product_id).first()
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("admin.admin_product"))
