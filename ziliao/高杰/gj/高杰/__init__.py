# __init__.py

import os
from flask import Flask
from axf.views import axf
# BASE_DIR建立一个基础路径，用于静态文件static，templates的调用
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def create_app():
    """初始化，创建app
    """
    # 建立静态文件static，tamplates的路径
    static_dir = os.path.join(BASE_DIR, 'static')
    templates_dir = os.path.join(BASE_DIR, 'templates')

    # 建立app
    app = Flask(__name__, templates_folder=templates_dir, static_folder=static_dir)
    # 将路由axf注册到蓝图blueprint，因为我使用了蓝图来管理和规划url，url_prefix参数表示在url前面必须加上axf前面，这是为了与同一个项目中不同的app进行区分，这里‘/axf’一定要加 / 不然会报错
    app.resgister_blueprint(blueprint=axf, url_prefix='/axf')

    return ap