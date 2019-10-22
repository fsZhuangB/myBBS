"""
    auth/views.py
    用户认证：蓝本中的路由和视图函数
"""

from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user
from . import auth
from ..models import User
from .forms import LoginForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    用户认证模板
    :return: render_template('auth/login.html')
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)
