from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

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
				return render(request, "login_success.html")
			else:
				return render(request, "index.html", {"error": "用户名或者密码错误"})


