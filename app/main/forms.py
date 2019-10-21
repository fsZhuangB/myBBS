"""
    froms.py
    表单对象
"""
from flask_wtf import Form
from wtforms import StringField, SubmitField, validators

class NameForm(Form):
    """
    这个函数用来生成表单
    DataRequired()用来验证，保证提交的字段不为空
    StringField类表示属性为type="text"的<input>元素
    SubmitField类表示属性为type="submit"的<input>元素
    """
    name = StringField('What is your name?', [validators.DataRequired()])
    submit = SubmitField('Submit')