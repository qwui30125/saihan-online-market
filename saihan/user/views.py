# coding:utf-8

from . import app_user
from saihan import db
from flask import render_template
from saihan.models import Product, Order, Profile
# from saihan.models import ...

# 购物车
@app_user.route("/cart")
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
    product = Product.query.filter_by(id=product_id).first()
    product = Product()
    return render_template("detail.html", product=product)

# 个人简介
@app_user.route('/info',defaults={'user_id':None})
@app_user.route('/info/<int:user_id>')
def user_info(user_id=None):
    user_id = user_id
    profile = Profile.query.filter_by(user_id=user_id).first()
    return render_template("user_info.html",profile=profile)


# 我的订单
@app_user.route('/order')
def user_order():
    user_id = 1
    order = Order.query.filter_by(buyer_id = id).first()
 
    return render_template("user_order.html")


# 收货地址
@app_user.route('/site')
def user_site():
    return render_template("user_site.html")

# 实名认证
@app_user.route('/auth')
def user_auth():
    return render_template("user_auth.html")
