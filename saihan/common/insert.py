# coding:utf-8
# insert.py
from . import app_common
from saihan import db
from saihan.models import *

@app_common.route("/insert_user_admin_saihan")
def insert_user():
    userA = User(type='PERSONAL', username='userA', 
        password_hash="pbkdf2:sha256:50000$AmvDhqDQ$7e68cbb\47c8627127b63b53aedd9969a98e5e5385443c07d54feeca5826ff2a8")
    userB = User(type='PERSONAL', username='userB', 
        password_hash="pbkdf2:sha256:50000$AmvDhqDQ$7e68cbb47c8627127b63b53aedd9969a98e5e5385443c07d54feeca5826ff2a8")
    sellerA = User(type='BUSINESS', username='sellerA', 
        password_hash="pbkdf2:sha256:50000$AmvDhqDQ$7e68cbb47c8627127b63b53aedd9969a98e5e5385443c07d54feeca5826ff2a8")
    sellerB = User(type='BUSINESS', username='sellerB', 
        password_hash="pbkdf2:sha256:50000$AmvDhqDQ$7e68cbb47c8627127b63b53aedd9969a98e5e5385443c07d54feeca5826ff2a8")
    adverA = User(type='ADVERTISEMENT', username='adverA', 
        password_hash="pbkdf2:sha256:50000$AmvDhqDQ$7e68cbb47c8627127b63b53aedd9969a98e5e5385443c07d54feeca5826ff2a8")
    adverB = User(type='ADVERTISEMENT', username='adverB', 
        password_hash="pbkdf2:sha256:50000$AmvDhqDQ$7e68cbb47c8627127b63b53aedd9969a98e5e5385443c07d54feeca5826ff2a8")
    admin = User(type='ADMINISTRATOR', username='admin', 
        password_hash="pbkdf2:sha256:50000$AmvDhqDQ$7e68cbb47c8627127b63b53aedd9969a98e5e5385443c07d54feeca5826ff2a8")
    users = [userA, userB, sellerA, sellerB, adverA, adverB, admin]
    try:
        db.session.add_all(users)
    except:
        db.session.rollback()
        raise
    else:
        db.session.commit()
    return "插入成功"

@app_common.route("/insert_profile_admin_saihan")
def insert_profile():
    userA = User.query.filter_by(username='userA').first()
    userB = User.query.filter_by(username='userB').first()
    sellerA = User.query.filter_by(username='sellerA').first()
    sellerB = User.query.filter_by(username='sellerB').first()
    adverA = User.query.filter_by(username='adverA').first()
    adverB = User.query.filter_by(username='adverB').first()
    admin = User.query.filter_by(username='admin').first()

    profileAu = Profile(user_id=userA.id, mobile="13113151342", nickname="大司马", avatar="dsm.jpg")
    profileBu = Profile(user_id=userB.id, mobile="13213151343", nickname="神超", avatar="shenchao.jpg")
    profileAs = Profile(user_id=sellerA.id, mobile="13313151343", nickname="刘某", avatar="liumou.jpg")
    profileBs = Profile(user_id=sellerB.id, mobile="13413151343", nickname="微笑", avatar="weixiao.jpg")
    profileAa = Profile(user_id=adverA.id, mobile="13513151343", nickname="孙亚龙", avatar="syl.jpeg")
    profileBa = Profile(user_id=adverB.id, mobile="13613151343", nickname="管高尚", avatar="adverB.jpg")
    profileAad = Profile(user_id=admin.id, mobile="13713151343", nickname="admin", avatar="admin.jpg")
    profiles = [profileAu, profileBu, profileAs, profileBs, profileAa, profileBa, profileAad]
    try:
        db.session.add_all(profiles)
    except:
        db.session.rollback()
        return "插入失败"
    else:
        db.session.commit()
    return "插入成功"

@app_common.route("/insert_product_admin_saihan")
def insert_product():
    # id = db.Column(db.Integer, primary_key=True)
    # seller_id = db.Column(db.Integer, db.ForeignKey("user_profile.user_id"), nullable=False)
    # name = db.Column(db.String(32), nullable=False)
    # description = db.Column(db.Text())
    # price = db.Column(db.Integer, nullable=False)
    # status = db.Column(
    #     db.Enum(
    #         "SELLING", # 出售中
    #         "SELLED" # 已出售
    #     ),
    #     default="SELLING")
    # attachments = db.relationship("ProductMedia", backref="product")
    sellerA = User.query.filter_by(username='sellerA').first()
    sellerB = User.query.filter_by(username='sellerB').first()

    productAA = Product(seller_id=sellerA.id, name="内向性格的竞争力", price="50", description="未拆封,半价转卖")
    productAB = Product(seller_id=sellerA.id, name="大明", price="40", description="未拆封,半价转卖")
    productAC = Product(seller_id=sellerA.id, name="金庸传", price="45", description="未拆封,半价转卖")
    productAD = Product(seller_id=sellerA.id, name="了不起的莎士比亚", price="60", description="未拆封,半价转卖")
    productBA = Product(seller_id=sellerB.id, name="二手车11", price="5000", description="一口价")
    productBB = Product(seller_id=sellerB.id, name="二手车22", price="4000", description="一口价")
    productBC = Product(seller_id=sellerB.id, name="二手车33", price="4500", description="一口价")
    productBD = Product(seller_id=sellerB.id, name="二手车44", price="6000", description="一口价")
    products = [productAA, productAB, productAC, productAD, productBA, productBB, productBC, productBD]
    try:
        db.session.add_all(products)
    except:
        db.session.rollback()
        return "插入失败"
    else:
        db.session.commit()
    # class ProductMedia(BaseModel, db.Model):
    # """商品照片"""
    # __tablename__ = "product_medias"
    # id = db.Column(db.Integer, primary_key=True)
    # product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    # filename = db.Column(db.String(64), nullable=False)  # 文件名
    prod_imgAA = ProductMedia(product_id=productAA.id, filename="p3.jpg")
    prod_imgAB = ProductMedia(product_id=productAB.id, filename="p4.jpg")
    prod_imgAC = ProductMedia(product_id=productAC.id, filename="p2.jpg")
    prod_imgAD = ProductMedia(product_id=productAD.id, filename="p1.jpg")
    prod_imgBA = ProductMedia(product_id=productBA.id, filename="p14.jpg")
    prod_imgBB = ProductMedia(product_id=productBB.id, filename="p15.jpg")
    prod_imgBC = ProductMedia(product_id=productBC.id, filename="p16.jpg")
    prod_imgBD = ProductMedia(product_id=productBD.id, filename="p17.jpg")
    prod_imgs = [prod_imgAA, prod_imgAB, prod_imgAC, prod_imgAD, prod_imgBA, prod_imgBB, prod_imgBC, prod_imgBD]
    try:
        db.session.add_all(prod_imgs)
    except:
        db.session.rollback()
        return "插入失败"
    else:
        db.session.commit()
    
    return "插入成功"