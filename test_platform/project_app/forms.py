from django import forms
from .models import Project, Module


class AddProjectForm(forms.ModelForm):
	"""项目表单"""
	# name = forms.CharField(label="项目名称", required=True)
	# describe = forms.CharField(label='项目描述', required=True, widget=forms.Textarea)
	# status = forms.BooleanField(label='状态', required=False)
	class Meta:
		model = Project
		exclude = ['create_time']


class ModuleForm(forms.ModelForm):
	"""模块表单"""
	class Meta:
		model = Module
		exclude = ['create_time']