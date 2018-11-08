from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from .models import Case
#from .forms import ModuleForm


class CaseManage(View):
	"""
	用例管理列表
	"""
	def get(self, request):
		username = request.session.get("user1", "")
		case_all = Case.objects.all()
		return render(request, "case_manage.html", {"user": username, "modules": case_all, "type": "list"})


class CaseApiDebug(View):
	"""用例调试"""
	def get(self, request):
		return render(request, "api_debug.html", {"type":"debug"})


class AddModule(View):
	"""
	添加用例
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
