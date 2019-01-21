# coding:utf-8

from . import app_user
from saihan import db
from flask import render_template, url_for
from saihan.models import Product, Order, Profile
from flask_login import current_user, login_required
# from saihan.models import ...

# 购物车
@app_user.route("/cart")
@login_required
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
    return render_template("user_cart.html", user=current_user)


# 支付界面
@app_user.route("/place_order")
@login_required
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
    return render_template("place_order.html",place=places, user=current_user)


# 商品详细信息
@app_user.route('/detail/<int:product_id>')
@login_required
def detail(product_id=None):
    product_id = product_id
    product = Product.query.filter_by(id=product_id).first()
    product = Product()
    return render_template("detail.html", product=product, user=current_user)

# 个人简介
@app_user.route('/info')
@login_required
def user_info():
    user = current_user
    profile = Profile.query.filter_by(user_id=user.id).first()
    if not profile:
        profile = Profile(user_id=user.id, mobile="11111111111", nickname=user.username, avatar="saihan.png")
        db.session.add(profile)
        db.session.commit()
    profile_img = url_for("static", filename="images/usericon/"+profile.avatar)
    return render_template("user_info.html", 
                           profile=profile, 
                           profile_img=profile_img,
                           user=current_user)


# 我的订单
@app_user.route('/order')
@login_required
def user_order():
    user_id = 1
    order = Order.query.filter_by(buyer_id = id).first()
 
    return render_template("user_order.html",  user=current_user)


# 收货地址
@app_user.route('/site')
@login_required
def user_site():
    return render_template("user_site.html",  user=current_user)

# 实名认证
@app_user.route('/auth')
@login_required
def user_auth():
    return render_template("user_auth.html",  user=current_user)
