"""
    __init__.py
    使用程序工厂函数
    延迟创建程序实例，把创建过程移到可显式调用的工厂函数中
"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth_login'


def create_app(config_name):
    from .main import main as main_blueprint
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)  # 注册蓝本

    # auth用认证蓝本
    # url_prefix是可选参数，注册后蓝本中定义的所有路由都会加入指定前缀
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # 附加路由和自定义错误页面
    return app