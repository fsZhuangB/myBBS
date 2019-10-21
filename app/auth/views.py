"""
    auth/views.py
    用户认证：蓝本中的路由和视图函数
"""

from flask import render_template
from . import auth


@auth.route('/login')
def login():
    """
    用户认证模板
    :return: render_template('auth/login.html')
    """
    return render_template('auth/login.html')
