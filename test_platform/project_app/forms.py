__author__ = 'caden'
__data__ = ' 14:53'
from django import forms
from .models import Project


class AddProjectForm(forms.Form):
	name = forms.CharField(required=True)
	describe = forms.CharField(required=True)
	status = forms.BooleanField(required=True)