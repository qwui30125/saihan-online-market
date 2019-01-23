# coding:utf-8

from . import app_user
from saihan import db
from flask import render_template, url_for, redirect
from saihan.models import Product, Order, Profile, Address
from flask_login import current_user, login_required
# from saihan.models import ...

# 购物车
# @app_user.route("/cart")
# @login_required
# def user_cart():
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
    # cart = Cart.query.filter_by(user_id=current_user.id)
    # products = []
    # for item in cart:
    #     product = Product.query.filter_by(id=item.product_id).first()
    #     products.append(product)
    # return render_template("user_cart.html",
    #                        user=current_user,
    #                        cart=cart,
    #                        products=products,
    #                        length=len(products))
    
    # print(help(url_for))



# 提交订单界面
@app_user.route("/place_order/")
@app_user.route("/place_order/<int:product_id>")
@login_required
def place_order(product_id=None):
    if product_id == None:
        return redirect(url_for("common.index"))
    product = Product.query.filter_by(id=product_id).first()
    address = Address.query.filter_by(user_id=current_user.id).first()
    return render_template("place_order.html",
                            product=product,
                            address=address)


# 商品详细信息
@app_user.route('/detail/<int:product_id>')
@login_required
def detail(product_id=None):
    product = Product.query.filter_by(id=product_id).first()
    return render_template("product_detail.html", 
                            product=product, 
                            user=current_user)

# @app_user.route('/detail/buy/<int:product_id>')
# @login_required
# def add_to_cart(product_id):
#     product = Product.query.filter_by(id=product_id).first()
#     if product.status == "SELLED":
#         return redirect(url_for("common.error", error="商品已售出"))
#     else:
#         cart = Cart(user_id=current_user.id, product_id=product_id)
#         db.session.add(cart)
#         db.session.commit()
#     return redirect(url_for("user.detail", product_id=product_id))


# @app_user.route('/cart/remove/<int:product_id>')
# @login_required
# def remove_from_cart(product_id):
#     item = Cart.query.filter_by(product_id=product_id, user_id=current_user.id).first()
#     db.session.delete(item)
#     db.session.commit()
#     return redirect(url_for("user.user_cart"))


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
    orders = current_user.profile[0].orders
    return render_template("user_order.html",
                           orders=orders,
                           user=current_user)

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
