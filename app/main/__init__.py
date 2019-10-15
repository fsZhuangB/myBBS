"""
    __init__.py
    创建蓝本程序：灵活定义路由
"""

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
