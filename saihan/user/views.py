# coding:utf-8

from . import app_user
from saihan import db
from flask import render_template
import saihan.models as models
# from saihan.models import ...

# 购物车
@app_user.route("/user_cart")
def user_cart():
    # cart=Cart.query.filter_by(user_id=).all()
    # carts=[]
    # for item in cart:
    #     product=Product.query.filter_by(id=item.product_id)
    #     carts.append({
    #     'attachments':'product.attachments',
    #     'description':'product.description',
    #     'price':'product.price'        
    # })

    # cart={
    #     'attachments':'Product.attachments',
    #     'description':'Product.description',
    #     'price':'Product.price'        
    # }
    return render_template("user_cart.html")


    # 支付界面
@app_user.route("/place_order")
def place_order(places=None):
    place1 = {
    'img_url':'p11.jpg',
    'danwei':'一块',
    'xinxi':'卡西欧',
    'jine':8000
    }
    place2 ={
    'img_url':'p15.jpg',
    'danjia':'一辆',
    'xinxi':'劳斯莱斯',
    'jine':500000
    }
    if not places:
        places = [place1, place2]
    return render_template("place_order.html",place=places)


# 商品详细信息
@app_user.route('/detail/<int:product_id>')
def detail(product_id=None):
    product_id = product_id
    product = models.Product.query.filter_by(id=product_id).first()
    product = models.Product()
    return render_template("detail.html", product=product)

# 个人简介
@app_user.route('/user_center_info',defaults={'user_id':None})
@app_user.route('/user_center_info/<int:user_id>')
def user_center_info(user_id=None):
    user_id = user_id
    profile = models.Profile.query.filter_by(user_id=user_id).first()
    return render_template("user_center_info.html",profile=profile)


# 我的订单
@app_user.route('/user_center_order')
def user_center_order():
    user_id = 1
    order = Order.query.filter_by(buyer_id = id).first()
    if order.status ==  :

    elif :

    else:

    return render_template("user_center_order.html")


# 收货地址
@app_user.route('/user_center_site')
def user_center_site():
    return render_template("user_center_site.html")


@app_user.route("/site")
def site():
    return render_template("user_site.html")