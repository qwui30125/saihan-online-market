# coding:utf-8

from . import app_common
from saihan import db
from flask import render_template, request
from saihan.models import User
# from saihan.models import ...

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
    user.generate_password_hash(password)
    user.password_hash = password  # 设置属性
    print(password)
    # try:
    #     db.session.add(user)
    #     db.session.commit()
    # except IntegrityError as e:
    #     # 数据库操作错误后的回滚
    #     db.session.rollback()
    #     # 表示手机号出现了重复值，即手机号已注册过
    #     current_app.logger.error(e)
    #     return jsonify(errno=RET.DATAEXIST, errmsg="手机号已存在")
    # except Exception as e:
    #     db.session.rollback()
    #     # 表示手机号出现了重复值，即手机号已注册过
    #     current_app.logger.error(e)
    #     return jsonify(errno=RET.DBERR, errmsg="查询数据库异常")

    # # 保存登录状态到session中
    # session["name"] = mobile
    # session["mobile"] = mobile
    # session["user_id"] = user.id

    # # 返回结果
    # return jsonify(errno=RET.OK, errmsg="注册成功")