# coding:utf-8

from . import app_seller
from saihan import db
from flask import render_template,request, url_for
from saihan.models import Product, Profile,ProductMedia,Order
from flask_login import current_user, login_required
# from saihan.models import ...


@app_seller.route("/items")
@login_required
def seller_items():
    profile = Profile.query.filter_by(user_id=current_user.id).first()
    products = Product.query.filter_by(seller_id=current_user.id)
    # print(url_for("static", filename="images/products/"+products[0].attachments[0].filename))
    return render_template("seller_items.html",
                            profile=profile,
                            products=products)


@app_seller.route("/order",methods=["GET","POST"])
def seller_order():
    # name = Product.query.filter_by(seller_id=current_user.id).all()
    products = Product.query.filter_by(seller_id=current_user.id).all()
    
    # l=[]
    
    # for order in order:
    #     order = Order.query.filter_by(product_id=product.id).all()
    #     l.append(order)
    
    return render_template("seller_order.html",products=products
                                        #  ,orders=orders,l=l,dic=dic
                                         )

    
        


@app_seller.route("/release", methods=["GET", "POST"])
def seller_release():
    if request.method == "GET":
        return render_template("seller_release.html")
    else:
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        picture = request.form.get('picture')
        product = Product(seller_id =current_user.id,name=name,description=description,price=price)
        
        db.session.add(product)
        db.session.commit()
        photo = ProductMedia(product_id = product.id,filename = picture)

        db.session.add(photo)
        db.session.commit()
        return "插入成功"
    