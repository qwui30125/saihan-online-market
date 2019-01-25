# coding:utf-8

from . import app_seller
from saihan import db
from flask import render_template,request, url_for, current_app, jsonify
from saihan.models import Product, Profile,ProductMedia,Order
from flask_login import current_user, login_required
import os
import datetime
# from saihan.models import ...


@app_seller.route("/items")
@login_required
def seller_items():
    profile = Profile.query.filter_by(user_id=current_user.id).first()
    products = Product.query.filter_by(seller_id=current_user.id)
    prod_stat = {
        "SELLING":"出售中",
        "SELLED":"已售出"
    }
    # print(url_for("static", filename="images/products/"+products[0].attachments[0].filename))
    return render_template("seller_items.html",
                            profile=profile,
                            products=products,
                            prod_stat=prod_stat)


@app_seller.route("/order",methods=["GET","POST"])
def seller_order():
    # name = Product.query.filter_by(seller_id=current_user.id).all()
    products = Product.query.filter_by(seller_id=current_user.id).all()
    # print(current_app.config["UPLOAD_FOLDER"])
    order_list = []
    product_list = []
    user_list = []
    for product in products:
        orders = Order.query.filter_by(product_id=product.id).all()
        for order in orders:
            user_profile = Profile.query.filter_by(user_id=order.buyer_id).first()
            user_list.append(user_profile)
            order_list.append(order)
            product_list.append(product)
    stat_dict = {   
        "PENDING":"未付款",
        "PURCHASED":'买家已付款',
        "DELIVERED":'卖家已发货',
        "COMPLETED":'已完成',
        "CANCELLED":"已取消"
    }
    
    return render_template("seller_order.html",
                            products=product_list,
                            orders=order_list,
                            users=user_list,
                            length=len(order_list),
                            stat_dict=stat_dict)

    
        


@app_seller.route("/release", methods=["GET", "POST"])
def seller_release():
    if request.method == "GET":
        return render_template("seller_release.html")
    else:
        # 使用POST方法,发送FromData对象,
        # 获取商品文字信息,并存储
        name = request.form.get('name')
        description = request.form.get('description')
        price = int(request.form.get('price'))
        print(name, description, price)
        product = Product(seller_id =current_user.id,name=name,description=description,price=price)
        db.session.add(product)
        db.session.commit()

        # 获取商品图片并存储到saihan/static/images/products/...文件中
        upload_folder = current_app.config['UPLOAD_FOLDER']
        prod_img = request.files.get('picture')
        # 更改文件名,使用时间字符串防止重名
        ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f") 
        ext = prod_img.filename.split(".")[-1]  # 获取文件扩展名
        prod_filename = ftime+"."+ext 
        prod_img.save(os.path.join(upload_folder, "products/"+prod_filename))
        picture = ProductMedia(product_id = product.id,filename = prod_filename)
        db.session.add(picture)
        db.session.commit()

        return jsonify({"resultCode":200})
    