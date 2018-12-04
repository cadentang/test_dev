__author__ = 'caden'
__data__ = ' 21:15'

from django import forms

from .user_models import UserInfo


class LoginForm(forms.Form):
	"""登录验证表单"""
	username = forms.CharField(required=True)
	password = forms.CharField(required=True)

