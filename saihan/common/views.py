# coding:utf-8

from . import app_common
from saihan import db, login_manager
from flask import render_template, request, session, redirect, url_for
from saihan.models import User, Profile
from flask_login import login_user, current_user, login_required, logout_user
# from saihan.models import ...

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

@login_manager.unauthorized_handler
def unauthorized():
    return render_template("error.html", error="未登录")

@app_common.route("/index")
def index():
    return render_template("index.html", user=current_user)


@app_common.route("/register", methods=["POST", "GET"])
def register():
    """注册
    请求的参数： 手机号、短信验证码、密码、确认密码
    参数格式：表单数据
    """
    method = request.method
    # 如果是get方法,返回静态页面
    if request.method == "GET":
        return render_template("register.html")

    # 如果是POST方法,则获取请求的表单数据，返回字典
    req_dict = request.form.to_dict()
    # print(dir(req_dict))

    username = req_dict.get("username")
    password = req_dict.get("pwd")
    password2 = req_dict.get("cpwd")
    mobile = req_dict.get("mobile")
    # print(username)
    # print(password)

    # 校验参数
    if not all([username, password, password2, mobile]):
        return render_template("error.html", error="参数不完整")

    # 密码验证
    if password != password2:
        return render_template("error.html", error="两次密码不一致")

    # 判断用户是否注册过
    try:
        user = User.query.filter_by(username=username).first()
    except Exception as e:
        raise
        return render_template("error.html", error="数据库异常")
    else:
        if user is not None:
            # 表示用户已存在
            return render_template("error.html", error="用户已存在")

    # 保存用户的注册数据到数据库中
    user = User(username=username, type="PERSONAL")
    user.password = password  # 设置属性
    print(user.password_hash)
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError as e:
        # 数据库操作错误后的回滚
        db.session.rollback()
        raise
        return render_template("error.html", error="用户已存在")
    except Exception as e:
        db.session.rollback()
        raise
        return render_template("error.html", error="查询数据库异常")
    # # 返回结果
    # return jsonify(errno=RET.OK, errmsg="注册成功")
    # 注册成功自动生成个人资料
    profile = Profile(user_id=user.id, mobile=mobile, nickname=username, avatar="saihan.png")

    return render_template("error.html", error="注册成功")


@app_common.route("/login", methods=["GET", "POST"])
def login():
    """用户登录
    参数： 用户名、密码
    """
    # 检查请求方式，GET请求返回登录页面
    method = request.method
    if method == "GET":
        return render_template("login.html")
    # 获取参数
    req_dict = request.form.to_dict()
    # print(req_dict)
    username = req_dict.get("username")
    password = req_dict.get("pwd")

    # 校验参数
    # 参数完整的校验
    if not all([username, password]):
        return render_template("error.html", error="参数不完整")

    # 从数据库中根据手机号查询用户的数据对象
    try:
        user = User.query.filter_by(username=username).first()
    except Exception as e:
        raise
        return render_template("error.html", error="获取用户信息失败")

    # 用数据库的密码与用户填写的密码进行对比验证
    if user is None or not user.check_password(password):
        return render_template("error.html", error="用户名或密码错误")

    login_user(user)
    # print(user)
    # 如果验证相同成功，保存登录状态， 在session中
    # return render_template("error.html", error=user.type)
    if user.type == "PERSONAL":
        return redirect(url_for("common.index"))
    elif user.type == "BUSINESS":
        return redirect(url_for("seller.seller_items"))
    elif user.type == "ADVERTISEMENT":
        return redirect(url_for("adver.adver_manage"))
    elif user.type == "ADMINISTRATOR":
        return redirect(url_for("admin.admin_user"))

@app_common.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("common.index"))
