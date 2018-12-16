from django.views.generic.base import View
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from ..models import TestCase, TestTask, TestTaskRecord
from project_app.models import Project, Module
from test_platform import common


class SaveTaskData(View):
	"""
	保存任务视图
	"""
	def post(self, request):
		task_name = request.POST.get("task_name", "")
		task_describe = request.POST.get("task_describe", "")
		task_creator = request.POST.get("task_creator", "")
		task_cases= request.POST.get("task_cases", "")
		cases_id = list(task_cases.replace(',', ''))
		creator_id = User.objects.get(username=task_creator)
		if task_name=="":
			return common.response_failed("任务名称不能为空！")
		task = TestTask.objects.create(name=task_name,describe=task_describe, creator=creator_id)
		cases = TestCase.objects.filter(id__in=cases_id)
		for case in cases:
			task.case_id.add(case)
		if task is not None:
			return common.response_succeed(data=[])


class GetCaseList(View):
	"""
	获取全部用例
	"""
	def get(self, request):
		case_list = []
		projects = Project.objects.all()
		for project in projects:
			modules = Module.objects.filter(project_id=project.id)
			for module in modules:
				testcases = TestCase.objects.filter(module_id=module.id)
				for case in testcases:
					case_info = project.name + "->" + module.name + "->" + case.name
					case_dict = {
						"id" : case.id,
						"name" : case_info,
					}
					case_list.append(case_dict)
		return common.response_succeed(data=case_list)


class DeleteTask(View):
	"""
	删除任务
	"""
	def get(self, request, task_id):
		TestTask.objects.get(pk=task_id).delete()

		return HttpResponseRedirect("/interface/task_manage/")











