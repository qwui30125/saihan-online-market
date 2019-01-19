# coding:utf-8

from . import app_adver
from saihan import db
from flask import render_template
# from saihan.models import ..
@app_adver.route("/adver_manage")
def adver_manage():
    user1 = {
    'img_url':'guanggao1.jpg',
    'xinxi':'神犬小七',
    'jine':'3000'
    }
    user2 ={
    'img_url':'guanggao3.jpg',
    'xinxi':'招聘信息',
    'jine':'5000'
    }
    users = [user1, user2]
    return render_template("adver_manage.html",users = users,name='张三')
@app_adver.route("/adver_release")
def adver_release():
    dic = {
    'name':'李四'
    }
    return render_template("adver_release.html",d1=dic)