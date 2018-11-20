from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

from ..models import Module, Project
from ..forms import ModuleForm


class ModuleManage(View):
	"""
	模块管理列表
	"""
	def get(self, request):
		username = request.session.get("user1", "")
		module_all = Module.objects.all()
		return render(request, "module_manage.html", {"user": username, "modules": module_all, "type": "list"})


class AddModule(View):
	"""
	添加模块
	"""
	def post(self, request):
		add_module_form = ModuleForm(request.POST)
		if add_module_form.is_valid():
			project = add_module_form.cleaned_data['project']
			name = add_module_form.cleaned_data['name']
			if Module.objects.filter(name=name):
				return render(request, "module_manage.html", {
					"type": 'add',
					"form": add_module_form,
					"msg": "模块已经存在!",
				})
			describe = add_module_form.cleaned_data['describe']
			status = add_module_form.cleaned_data['status']
			Module.objects.create(name=name, describe=describe, status=status, project=project)
			return HttpResponseRedirect('/manage/module_manage/')

	def get(self, request):
		add_module_form = ModuleForm(request.GET)
		return render(request, 'module_manage.html', {
			'form': add_module_form,
			'type': 'add',
		})


class EditModule(View):
	"""编辑模块"""
	def post(self, request, mid):
		form = ModuleForm(request.POST)
		if form.is_valid():
			data = Module.objects.get(id=mid)
			data.name = form.cleaned_data["name"]
			data.describe = form.cleaned_data["describe"]
			data.status = form.cleaned_data["status"]
			data.save()
			return HttpResponseRedirect("/manage/module_manage/")

	def get(self, request, mid):
		if mid:
			module1 = Module.objects.get(id=mid)
			module_form = ModuleForm(instance=module1)
		else:
			module_form = ModuleForm()
		return render(request, 'module_manage.html', {
			'form': module_form,
			"type": "edit",
		})


class DeleteModule(View):
	"""删除模块"""
	def get(self, request, mid):
		Module.objects.get(id=mid).delete()
		return HttpResponseRedirect("/manage/module_manage/")


class ViewModule(View):
	"""查看模块"""
	def get(self, request, mid):
		pass


class SearchModuleName(View):
	"""搜索模块，维度：项目名称、模块名称、模块状态"""
	def get(self, request):
		module_name = request.GET.get("module_name", "")
		project_name = request.GET.get("project_name", "")
		status = request.GET.get("status", "")
		project_all = Project.objects.filter(name__contains=project_name)

		module_all = Module.objects.filter(name__contains=module_name)

		paginator = Paginator(module_all, 10)
		page = request.GET.get('page', 1)
		start = (int(page) - 1) *10
		try:
			modules = paginator.page(page)
		except PageNotAnInteger:
			modules = paginator.page(1)
		except EmptyPage:
			modules = paginator.page(paginator.num_pages)
		return render(request, "module_manage.html", {
			"modules": modules,
			"type": "list",
			"start": start,
		})