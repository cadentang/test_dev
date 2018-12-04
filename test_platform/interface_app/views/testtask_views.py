from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models import TestTask, TestTaskRecord


class TaskManage(View):
	"""
	任务管理列表
	"""
	def get(self, request):
		username = request.session.get("user1", "")
		task_all = TestTask.objects.all()
		creators = User.objects.all()
		paginator = Paginator(task_all, 10)
		page = request.GET.get("page", 1)
		start = (int(page) - 1) *10
		try:
			contacts = paginator.page(page)
		except PageNotAnInteger:
			contacts = paginator.page(1)
		except EmptyPage:
			contacts = paginator.page(paginator.num_pages)
		return render(request, "task_manage.html",
		              {"user": username, "testtasks": contacts, "type": "list", "start": start, "creators": creators})


class AddTask(View):
	"""创建任务页面"""
	def get(self, request):
		return render(request, "add_task.html", {"type": "add"})












