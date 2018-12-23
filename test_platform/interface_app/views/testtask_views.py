import os, sys, json

from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models import TestTask, TestTaskRecord, TestCase
from test_platform import common
from ..apps import TASK_PATH, RUN_TASK_FILE

from ..extend.task_run import run_cases
from ..extend.task_thread import TaskThread


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
	"""
	创建任务页面
	"""
	def get(self, request):
		return render(request, "add_task.html", {"type": "add"})


class RunTask(View):
	"""
	运行测试任务视图
	"""
	def get(self, request, task_id):
		not_run_task_status_choice = ["y1", "y2", "y3"]
		queryset = TestTask.objects.get(id=task_id)
		task_cases = queryset.case_id.all()
		if queryset.status not in not_run_task_status_choice:
			TaskThread(task_id).new_run()
		else:
			return common.response_succeed(message="当前状态不能执行任务：%s" %(queryset.name))

		task_cases_dict = {}
		response_header_list = []
		for task_case in task_cases:
			task_case_header = dict(task_case.response_header)
			print(type(task_case_header))
			print(task_case_header)
			response_header_list.append(task_case_header.replace("'", ""))
			print(response_header_list)
			task_case_dict = {
				"response_url": task_case.response_url,
				"response_method": task_case.response_method,
				"response_type": task_case.response_type,
				"response_header": response_header_list,
				"response_parameter": task_case.response_parameter,
				"response_assert": task_case.response_assert,
			}
			case_id = str(task_case.id)
			print(case_id)
			task_cases_dict[case_id] = task_case_dict

		task_cases_json = json.dumps(task_cases_dict)
		case_data_file = TASK_PATH + "cases_data.json"
		print(">>>>存入json文件的数据类型:", type(task_cases_json))
		print("存于后端的数据-----", task_cases_json)
		with open(case_data_file, "w+") as f:
			f.write(task_cases_json)
		print(RUN_TASK_FILE)
		# os.popen("F:")
		# os.popen("cd F:/test_dev_env/test_dev_env/Scripts")
		# os.popen("python " + RUN_TASK_FILE)
		run_cases()

		return HttpResponseRedirect("/interface/task_manage")










