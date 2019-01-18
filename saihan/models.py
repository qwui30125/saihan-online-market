# -*- coding:utf-8 -*-

import datetime
import werkzeug.security
from saihan import db


class BaseModel(object):
    """模型基类，为每个模型补充创建时间与更新时间"""

    create_time = db.Column(db.DateTime, default=datetime.datetime.now)  # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)  # 记录的更新时间


class User(BaseModel, db.Model):
    """用户"""
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)  # 用户编号
    type = db.Column(  # 账户类型
        db.Enum(  # 枚举
            "PERSONAL",  # 个人,
            "BUSINESS",  # 商家
            "ADVERTISEMENT",  # 广告商
            "ADMINISTRATOR",  # 管理员
        ),
        nullable=False, index=True)
    username = db.Column(db.String(32), unique=True, nullable=False)  # 用户暱称
    password_hash = db.Column(db.String(128), nullable=False)  # 密码的散列值

    # 加上property装饰器后，会把函数变为属性，属性名即为函数名
    @property
    def password(self):
        """读取属性的函数行为"""
        raise AttributeError("这个属性只能设置，不能读取")

    # 使用这个装饰器, 对应设置属性操作
    @password.setter
    def password(self, value):
        """
        设置属性  user.password = ""
        :param value: 设置属性时的数据 value就是 "", 原始的明文密码
        :return:
        """
        self.password_hash = werkzeug.security.generate_password_hash(value)

    def check_password(self, passwd):
        """
        检验密码的正确性
        :param passwd:  用户登录时填写的原始密码
        :return: 如果正确，返回True， 否则返回False
        """
        return werkzeug.security.check_password_hash(self.password_hash, passwd)


class Profile(BaseModel, db.Model):
    """个人资料"""
    __tablename__ = "user_profile"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    mobile = db.Column(db.String(11), unique=True, nullable=False)  # 手机号
    nickname = db.Column(db.String(32))  # 昵称
    avatar = db.Column(db.String(128))  # 用户头像路径
    info = db.Column(db.Text())  # 个人简介
    addresses = db.relationship("Address", backref="user")
    products = db.relationship("Product", backref="seller")
    orders = db.relationship("Order", backref="buyer")
    # statuses_sent = db.relationship("Status", backref="source")
    # statuses_received = db.relationship("Status", backref="target")


class Address(BaseModel, db.Model):
    """地址"""
    __tablename__ = "user_addresses"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user_profile.user_id"), nullable=False)
    country = db.Column(db.String(32))  # 国家
    province = db.Column(db.String(32))  # 省/直辖市
    city = db.Column(db.String(32))  # 城市
    street = db.Column(db.String(32))  # 街道
    name = db.Column(db.String(32))  # 联系人姓名
    phone = db.Column(db.String(32))  # 联系人电话


class Authenticate(BaseModel, db.Model):
    """实名认证信息"""
    __tablename__ = "user_authenticates"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    type = db.Column(  # 认证类型
        db.Enum(  # 枚举
           "PERSONAL",  # 个人,
            "BUSINESS",  # 商家
            "ADVERTISEMENT",  # 广告商 
        ),
        nullable=False, index=True)
    status = db.Column(  # 认证状态
        db.Enum(
            "PENDING",  # 新申请
            "COMPLETED",  # 完成
            "REJECTED",  # 被拒绝
        ),
        default="PENDING", nullable=False, index=True)


class AuthenticateDocuments(BaseModel, db.Model):
    """认证使用的文件"""
    __tablename__ = "user_authenticate_documents"

    id = db.Column(db.Integer, primary_key=True)
    apply_id = db.Column(db.Integer, db.ForeignKey("user_authenticates.id"), nullable=False)
    filename = db.Column(db.String(64), nullable=False)  # 文件名


class Product(BaseModel, db.Model):
    """商品"""
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    seller_id = db.Column(db.Integer, db.ForeignKey("user_profile.user_id"), nullable=False)
    name = db.Column(db.String(32), nullable=False)
    description = db.Column(db.Text())
    price = db.Column(db.Integer, nullable=False)
    attachments = db.relationship("ProductMedia", backref="product")


class Order(BaseModel, db.Model):
    """订单"""
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    buyer_id = db.Column(db.Integer, db.ForeignKey("user_profile.user_id"), nullable=False)
    status = db.Column(  # 订单状态
        db.Enum(
            "PENDING",  # 新订单
            "PURCHASED",  # 买家已付款
            "DELIVERED",  # 卖家已发货
            "COMPLETED",  # 已完成
            "CANCELLED"  # 已取消
        ),
        default="PENDING", nullable=False, index=True)
    comments = db.Column(db.Text())  # 备注


class Status(BaseModel, db.Model):
    """评价"""
    __tablename__ = "statuses"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer,  db.ForeignKey("orders.id"), nullable=False)
    # source_id = db.Column(db.Integer, db.ForeignKey("user_profile.user_id"), nullable=False)  # 评价人
    # target_id = db.Column(db.Integer, db.ForeignKey("user_profile.user_id"), nullable=False)  # 被评价人
    level = db.Column(  # 评价等级
        db.Enum(
            "PENDING",  # 没有作出评价
            "POSITIVE",  # 好评
            "NEUTRAL",  # 中评
            "NEGATIVE"  # 差评
        ),
        default="PENDING", nullable=False, index=True)
    text = db.Column(db.Text())
    reply = db.Column(db.Text())


class ProductMedia(BaseModel, db.Model):
    """商品照片"""
    __tablename__ = "product_medias"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    filename = db.Column(db.String(64), nullable=False)  # 文件名
