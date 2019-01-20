# coding:utf-8

from . import app_adver
from saihan import db
from flask import render_template
import saihan.models as models
# from saihan.models import ..

# 广告界面
@app_adver.route("/adver_manage")
def adver_manage():
    user1 = {
    'img_url':'guanggao1.jpg',
    'xinxi':'神犬小七',
    'jine':'3000'
    }
    user2 ={
    'img_url':'guanggao3.jpg',
    'xinxi':'招聘信息',
    'jine':'5000'
    }
    users = [user1, user2]
    return render_template("adver_manage.html",users = users,name='张三')
@app_adver.route("/adver_release")
def adver_release():
    dic = {
    'name':'李四'
    }
    return render_template("adver_release.html",d1=dic)

# 购物车
@app_adver.route("/adver_cart")
def adver_cart():
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
    return render_template("adver_cart.html")


    # 支付界面
@app_adver.route("/place_order")
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
@app_adver.route('/detail/<int:product_id>')
def detail(product_id=None):
    product_id = product_id
    product = models.Product.query.filter_by(id=product_id).first()
    print(product.name, product.price)
    return render_template("detail.html", product=product)

# 个人简介
@app_adver.route('/user_center_info',defaults={'user_id':None})
@app_adver.route('/user_center_info/<int:user_id>')
def user_center_info(user_id=None):
    user_id = user_id
    profile = models.Profile.query.filter_by(user_id=user_id).first()
    return render_template("user_center_info.html",profile=profile)


# 我的订单
@app_adver.route('/user_center_order')
def user_center_order():
    return render_template("user_center_order.html")


# 收货地址
@app_adver.route('/user_center_site')
def user_center_site():
    return render_template("user_center_site.html")