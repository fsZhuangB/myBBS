"""
    __init__.py
    使用程序工厂函数
    延迟创建程序实例，把创建过程移到可显式调用的工厂函数中
"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
# from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
# mail = Mail()
moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    # mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    # 附加路由和自定义错误页面
    return app