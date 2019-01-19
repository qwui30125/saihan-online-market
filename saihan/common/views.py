# coding:utf-8

from . import app_common
from saihan import db
from flask import render_template, request, session, redirect, url_for, flash
from saihan.models import User
# from saihan.models import ...

@app_common.route("/index")
def index():
    if 'username' in session:
        user_id = session["user_id"]
        username = session["username"]
        return render_template("index.html", username=username)
    return render_template("index.html")


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
    print(dir(req_dict))

    username = req_dict.get("username")
    password = req_dict.get("pwd")
    password2 = req_dict.get("cpwd")
    email = req_dict.get("email")
    print(username)
    print(password)

    # 校验参数
    if not all([username, password, password2, email]):
        return "<h1>参数不完整</h1>"


    if password != password2:
        return "<h1>两次密码不一致</h1>"


    # 判断用户是否注册过
    try:
        user = User.query.filter_by(username=username).first()
    except Exception as e:
        raise
        return "数据库异常"
    else:
        if user is not None:
            # 表示手机号已存在
            return "用户已存在"

    # 盐值   salt

    #  注册
    #  用户1   password="123456" + "abc"   sha1   abc$hxosifodfdoshfosdhfso
    #  用户2   password="123456" + "def"   sha1   def$dfhsoicoshdoshfosidfs
    #
    # 用户登录  password ="123456"  "abc"  sha256      sha1   hxosufodsofdihsofho

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
        return "用户已存在"
    except Exception as e:
        db.session.rollback()
        raise
        return "查询数据库异常"

    # # 保存登录状态到session中
    session["username"] = user.username
    session["user_id"] = user.id

    # # 返回结果
    flash('登录成功')
    return redirect(url_for("common.index"))


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
    print(req_dict)
    username = req_dict.get("username")
    password = req_dict.get("pwd")

    # 校验参数
    # 参数完整的校验
    if not all([username, password]):
        return "参数不完整"

    # 从数据库中根据手机号查询用户的数据对象
    try:
        user = User.query.filter_by(username=username).first()
    except Exception as e:
        raise
        return "获取用户信息失败"

    # 用数据库的密码与用户填写的密码进行对比验证
    if user is None or not user.check_password(password):
        return "用户名或密码错误"

    # 如果验证相同成功，保存登录状态， 在session中
    session["username"] = user.username
    session["user_id"] = user.id

    flash('登录成功')
    return redirect(url_for("common.index"))

@app_common.route("/session", methods=["GET"])
def check_login():
    """检查登陆状态"""
    # 尝试从session中获取用户的名字
    username = session.get("username")
    # 如果session中数据name名字存在，则表示用户已登录，否则未登录
    if username is not None:
        return "已登录"
    else:
        return "未登录"


@app_common.route("/session", methods=["DELETE"])
def logout():
    """登出"""
    # 清除session数据
    session.clear()
    return "已登出"