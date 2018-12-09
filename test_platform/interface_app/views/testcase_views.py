import json, requests
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..forms import TestCaseForm
from ..models import TestCase
from project_app.models import Project, Module

class CaseManage(View):
	"""
	用例管理列表
	"""
	def get(self, request):
		username = request.session.get("user1", "")
		case_all = TestCase.objects.all()
		return render(request, "case_manage.html",
		              {"user": username, "modules": case_all, "type": "list"})


class AddCase(View):
	"""
	创建用例
	"""
	def get(self, request):
		return render(request, "add_case.html", {"type": "add"})


class DebugCase(View):
	"""
	调试用例
	"""
	def post(self, request):
		url = request.POST.get("response_url")
		method = request.POST.get("response_method")
		parameter = request.POST.get("response_parameter")
		headers = request.POST.get("response_header")
		if method == "get":
			result = requests.get(url, headers=json.loads(headers))
		if method == "post":
			result = requests.post(url, data=parameter)
		return HttpResponse(result.text)


class SaveCase(View):
	"""
	保存用例
	"""
	def post(self, request):
		module_name = request.POST.get("module_name")
		name = request.POST.get("name", "")
		response_url = request.POST.get("response_url", "")
		response_method = request.POST.get("response_method", "")
		response_type = request.POST.get("response_type", "")
		response_header = request.POST.get("response_header", "")
		response_parameter = request.POST.get("response_parameter", "")
		response_assert = request.POST.get("response_assert", "")
		status = request.POST.get("status", "")
		if response_url=="":
			return HttpResponse("URL该字段不能为空")
		if response_method=="":
			return HttpResponse("请求方法该字段不能为空")
		if response_type=="":
			return HttpResponse("该字段不能为空")
		if module_name=="":
			return HttpResponse("module_name该字段不能为空")
		if status=="":
			return HttpResponse("status该字段不能为空")
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


class GetProjectList(View):
	"""
	获取项目模块列表
	"""
	def get(self, request):
		project_list = Project.objects.all()
		datalist = []
		for project in project_list:
			project_dict = {
				"name": project.name
			}
			module_list = Module.objects.filter(project_id=project.id)
			if len(module_list) != 0:
				module_name = []
				for module in module_list:
					module_name.append(module.name)
					project_dict["modulelist"] = module_name
					datalist.append(project_dict)
		return JsonResponse({"success":"true", "data": datalist})


class CaseManage(View):
	"""
	获取用例列表
	"""
	def get(self, request):
		testcases = TestCase.objects.all()
		modules = Module.objects.all()
		projects = Project.objects.all()
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
			"modules":modules,
			"projects":projects,
			"type": "list",
			"start": start,
		})


class SearchCaseName(View):
	"""
	测试用例搜索
	"""
	def get(self, request):
		case_name = request.GET.get("case_name", "")
		cases = TestCase.objects.filter(name__contains=case_name)
		modules = Module.objects.all()
		projects = Project.objects.all()
		paginator = Paginator(cases, 10)
		page = request.GET.get("page", 1)
		start = (int(page) - 1) * 10
		try:
			contacts = paginator.page(page)
		except PageNotAnInteger:
			# 如果页数不是整型, 取第一页.
			contacts = paginator.page(1)
		except EmptyPage:
			# 如果页数超出查询范围，取最后一页
			contacts = paginator.page(paginator.num_pages)
		return render(request, "case_manage.html", {
			"type": "list",
			"start": start,
			"modules": modules,
			"projects": projects,
			"testcases": contacts,
			"case_name": case_name,
		})


class GetCase(View):
	"""
	获取单个用例信息
	"""
	def post(self, request):
		case_id = request.POST.get("case_id", "")
		if case_id == "":
			return JsonResponse({"success": "false","message": "case id is null!"})
		case = TestCase.objects.get(pk=case_id)
		module_obj = Module.objects.get(pk=case.module_id)
		module_name = module_obj.name
		project_obj = Project.objects.get(pk=module_obj.project_id)
		project_name = project_obj.name
		case_info = {
			"project_name": project_name,
			"module_name": module_name,
			"name": case.name,
			"response_url": case.response_url,
			"response_method": case.response_method,
			"response_type": case.response_type,
			"response_header": case.response_header,
			"response_parameter": case.response_parameter,
			"response_assert": case.response_assert,
			"response_status": case.status,
		}
		return JsonResponse({"success": "true", "message": "ok", "data": case_info})


class EditCase(View):
	"""
	进入用例调试页面
	"""
	def get(self, request, case_id):
		form = TestCaseForm()
		return render(request, "debug_case.html", {
			"form": form,
			"type": "debug"
		})


class ApiAssert(View):
	"""
	验证测试用例结果
	"""
	def post(self, request):
		assert_message = request.POST.get("assert_message", "")
		response_result = request.POST.get("response_result", "")
		if assert_message == "" or response_result == "":
			return JsonResponse({"success": "false", "message": "断言或者响应结果不能为空！"})
		try:
			assert assert_message in response_result
		except AssertionError:
			return JsonResponse({"success": "false", "message": "断言失败！"})
		else:
			return JsonResponse({"success": "True", "message": "断言成功！"})


class EditSaveCase(View):
	"""
	用例调试页面保存用例
	"""
	def post(self, request):
		case_id = request.POST.get("case_id", "")
		if case_id == "":
			return JsonResponse({"success": "false","message": "case id is null!"})
		module_name = request.POST.get("module_name", "")
		name = request.POST.get("name", "")
		response_url = request.POST.get("response_url", "")
		response_method = request.POST.get("response_method", "")
		response_type = request.POST.get("response_type", "")
		response_header = request.POST.get("response_header", "")
		response_parameter = request.POST.get("response_parameter", "")
		response_assert = request.POST.get("response_assert", "")
		status = request.POST.get("status", "")
		module_id = Module.objects.get(name=module_name)
		dic = {
			"name": name,
			"response_url": response_url,
			"response_method": response_method,
			"response_type": response_type,
			"response_header": response_header,
			"response_parameter": response_parameter,
			"response_assert": response_assert,
			"status": status,
			"module_id": module_id,
		}
		TestCase.objects.filter(id=case_id).update(**dic)
		return HttpResponse("保存成功!")


class DeleteCase(View):
	"""
	删除用例
	"""
	def get(self, request, case_id):
		TestCase.objects.get(pk=case_id).delete()
		return HttpResponseRedirect("/interface/case_manage/")











