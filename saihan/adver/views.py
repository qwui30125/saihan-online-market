# coding:utf-8

from . import app_adver
from saihan import db
from flask import render_template
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
def place_order():
    place1 = {
    'img_url':'p11.jpg',
    'danwei':'一块',
    'xinxi':'卡西欧',
    'jine':3000
    }
    place2 ={
    'img_url':'p15.jpg',
    'danjia':'一辆',
    'xinxi':'劳斯莱斯',
    'jine':500000
    }
    places = [place1, place2]
    return render_template("place_order.html",place=places)


# 商品详细信息
@app_adver.route('/detail')
def detail():
    return render_template("detail.html")

