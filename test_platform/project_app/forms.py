from django import forms
from .models import Project, Module


class AddProjectForm(forms.ModelForm):
	"""项目表单"""
	class Meta:
		model = Project
		exclude = ['create_time']


class ModuleForm(forms.ModelForm):
	"""模块表单"""
	class Meta:
		model = Module
		exclude = ['create_time']