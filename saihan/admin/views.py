# coding:utf-8

from . import app_admin
from saihan import db
from flask import render_template
# from saihan.models import ...

@app_admin.route("/admin_userinfo")
def admin_userinfo():
    user_list = [
        {
            "id":"UserSH0001",
            "username":"前田敦子",
            "user_pic":"static/images/qiantian.jpg",
            "type":"买家",
            "check":"已实名",
            "regs_time":"2018-1-1",
            "last_time":"2019-1-15"
            },
        {
             "user_id":"UserSH0002",
            "user_name":"赵吏",
            "user_pic":"static/images/li.jpeg",
            "user_type":"买家",
            "check":"已实名",
            "regs_time":"2018-1-1",
            "last_time":"2019-1-15"
         },
         {
             "user_id":"UserSH0002",
            "user_name":"赵吏",
            "user_pic":"static/images/li.jpeg",
            "user_type":"买家",
            "check":"已实名",
            "regs_time":"2018-1-1",
            "last_time":"2019-1-15"
         },
         {
             "user_id":"UserSH0002",
            "user_name":"赵吏",
            "user_pic":"static/images/li.jpeg",
            "user_type":"买家",
            "check":"已实名",
            "regs_time":"2018-1-1",
            "last_time":"2019-1-15"
         },
         {
             "user_id":"UserSH0002",
            "user_name":"赵吏",
            "user_pic":"static/images/li.jpeg",
            "user_type":"买家",
            "check":"已实名",
            "regs_time":"2018-1-1",
            "last_time":"2019-1-15"
         }
    ]
    return render_template("admin_center.html",u_list = user_list)

@app_admin.route("/admin_productinfo")
def admin_productinfo():
    return render_template("admin_productinfo.html")

@app_admin.route("/admin_order")
def admin_order():
    return render_template("admin_order.html")

@app_admin.route("/admin_adver")
def admin_adver():
    adver_list = [
        {
            "adver_id":"AdverSH0002",
            "adver_name":"赵吏",
            "adver_pic":"static/images/li.jpeg",
            
        }
    ]
    return render_template("admin_adver.html")