# coding:utf-8

from flask import Blueprint


# 创建蓝图对象
app_admin = Blueprint("admin", __name__, static_folder="./static", template_folder="./templates")


# 导入蓝图的视图
from . import views
