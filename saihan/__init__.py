# coding:utf-8

from flask import Flask, redirect, url_for
from config import config_map
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_login import LoginManager

# 数据库
db = SQLAlchemy()

# 登录管理
login_manager = LoginManager()


# 工厂模式
def create_app(config_name):
    """
    创建flask的应用对象
    :param config_name: str  配置模式的模式的名字 （"develop",  "product"）
    :return:
    """
    app = Flask(__name__)

    # 根据配置模式的名字获取配置参数的类
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)

    # 使用app初始化db, login_manage
    db.init_app(app)

    # 使用app初始化login_manage
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    # 注册蓝图
    from saihan import admin, adver, seller, user, common
    app.register_blueprint(common.app_common, url_prefix="/common")
    app.register_blueprint(admin.app_admin, url_prefix="/admin")
    app.register_blueprint(adver.app_adver, url_prefix="/adver")
    app.register_blueprint(seller.app_seller, url_prefix="/seller")
    app.register_blueprint(user.app_user, url_prefix="/user")

    @app.route("/")
    def index():
        return redirect(url_for("common.index"))


    return app
