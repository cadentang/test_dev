from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Project, Module

# Create your views here.


def index(request):
	return render(request, "index.html")


def login_action(request):

	if request.method == 'POST':
		username = request.POST.get("username", "")
		password = request.POST.get("password", "")
		if username == "" or password == "":
			return render(request, "index.html", {"error": "用户名或密码不能为空!"})
		else:
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				request.session["user1"] = username
				return HttpResponseRedirect("/project_manage/")
			else:
				return render(request, "index.html", {"error": "用户名或者密码错误"})
	else:
		return render(request, "index.html")


@login_required
def project_manage(request):
	username = request.session.get("user1", "")
	project_all = Project.objects.all()
	return render(request, "project_manage.html", {"user": username, "projects": project_all})


@login_required()
def logout_view(request):
	#退去登录
	logout(request)
	return HttpResponseRedirect("/login_action/")





