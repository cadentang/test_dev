from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
	return render(request, "index.html")


def login(request):

	if request.method =='GET':
		username = request.GET.get("username")
		password = request.GET.get("password")

		if username == "" or password == "":
			return render(request, "index.html", {"error": "用户名或密码不能为空!"})



