import json, requests
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from interface_app.models import TestCase
from project_app.models import Project, Module
from ..forms import TestCaseForm


class CaseManage(View):
	"""
	用例管理列表
	"""
	def get(self, request):
		username = request.session.get("user1", "")
		case_all = TestCase.objects.all()
		return render(request, "case_manage.html", {"user": username, "modules": case_all, "type": "list"})


class Debug(View):
	"""创建、调试接口"""
	def get(self, request):
		return render(request, "api_debug.html", {"type": "debug"})


class CaseApiDebug(View):
	"""用例调试"""
	def post(self, request):
		url = request.POST.get("response_url")
		method = request.POST.get("response_method")
		parameter = request.POST.get("response_parameter")
		headers = request.POST.get("response_header")
		print(headers)
		# payload = json.loads(parameter.replace("'", "\""))
		if method == "get":
			result = requests.get(url, headers=json.loads(headers))
			print(result.text)
		if method == "post":
			result = requests.post(url, data=parameter)
		return HttpResponse(result.text)


class SaveCase(View):
	"""创建用例"""
	def post(self, request):
		module_name = request.POST.get("module")
		name = request.POST.get("name", "")
		response_url = request.POST.get("response_url", "")
		response_method = request.POST.get("response_method", "")
		response_type = request.POST.get("response_type", "")
		response_header = request.POST.get("response_header", "")
		response_parameter = request.POST.get("response_parameter", "")
		response_assert = request.POST.get("response_assert", "")
		status = request.POST.get("status", "")

		if response_url==""or response_method==""or response_type==""or module_name=="" or status=="":
			return HttpResponse("该字段不能为空")

		if response_header == "":
			response_header = "{}"

		if response_parameter == "":
			response_parameter = "{}"

		module_obj = Module.objects.get(name=module_name)
		case = TestCase.objects.create(name=name,module=module_obj, response_url=response_url,
		                               response_method=response_method, response_type=response_type,
		                               response_header=response_header, response_parameter=response_parameter,
		                               response_assert=response_assert, status=status)
		if case is not None:
			return HttpResponse("保存成功!")


# 获取项目模块列表
class GetProjectList(View):
	def get(self, request):
		project_list = Project.objects.all()
		datalist = []
		for project in project_list:
			project_dict = {
				"name", project.name
			}
			module_list = Module.objects.filter(project_id=project.id)
			if len(module_list) != 0:
				module_name = []
				for module in module_list:
					module_name.append(module.name)
					project_dict["modulelist"] = module_name
					datalist = datalist.append(project_dict).json()
		return JsonResponse({"success":"true", "data": datalist})


# 获取用例列表
class CaseManage(View):
	def get(self, request):
		testcases = TestCase.objects.all()
		paginator = Paginator(testcases, 10)
		page = request.GET.get("page", 1)
		start = (int(page) - 1) *10
		try:
			contacts = paginator.page(page)
		except PageNotAnInteger:
			# 如果页数不是整型, 取第一页.
			contacts = paginator.page(1)
		except EmptyPage:
			# 如果页数超出查询范围，取最后一页
			contacts = paginator.page(paginator.num_pages)
		return render(request, "case_manage.html", {
			#"user": username,
			"testcases": contacts,
			"type": "list",
			"start": start,
		})


















