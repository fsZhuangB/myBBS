"""
    auth/__init__.py
    创建蓝本，用户认证系统相关的路由
"""
from flask import Blueprint
auth = Blueprint('auth', __name__)
from . import views