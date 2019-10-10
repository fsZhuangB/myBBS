from flask import Flask, render_template, url_for, redirect, session,flash # session 是用户会话，用于储存请求之间需要记住值的词典
from flask_wtf import Form
from wtforms import StringField, SubmitField,validators
from wtforms.validators import Required
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os

from datetime import datetime

app = Flask(__name__)

"""
Use this code, or you will get:
KeyError: 'A secret key is required to use CSRF.'
"""
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)

"""
配置数据库
"""
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))
# def hello_world():
#     # name = None
#     form = NameForm()
#     if form.validate_on_submit():
#         session['name'] = form.name.data
#         name = form.name.data
#         form.name.data = ''
#     return render_template('index.html', form=form, name=name, current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


class NameForm(Form):
    """
    这个函数用来生成表单
    DataRequired()用来验证，保证提交的字段不为空
    StringField类表示属性为type="text"的<input>元素
    SubmitField类表示属性为type="submit"的<input>元素
    """
    name = StringField('What is your name?', [validators.DataRequired()])
    submit = SubmitField('Submit')


"""
  定义Role和User模型
"""


class Role(db.Model):
    __tablename__ = 'roles' # 在数据库中使用的表名
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        """
        用于调试和测试时使用
        :return: 返回一个具有可读性的字符串表示模型
        """
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == '__main__':
    app.run()
