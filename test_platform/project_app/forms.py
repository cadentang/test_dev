__author__ = 'caden'
__data__ = ' 14:53'
from django import forms
from .models import Project


class AddProjectForm(forms.ModelForm):
	#name = forms.CharField(label="项目名称", required=True)
	#describe = forms.CharField(label='项目描述', required=True, widget=forms.Textarea)
	#status = forms.BooleanField(label='状态', required=False)
	class Meta:
		model = Project
		exclude = ['create_time']
