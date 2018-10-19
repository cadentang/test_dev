from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from ..models import Project, Module
from ..forms import AddProjectForm


class ProjectManage(View):
	"""
	项目管理
	"""
	def get(self, request):
		username = request.session.get("user1", "")
		project_all = Project.objects.all()
		return render(request, "project_manage.html", {"user": username, "projects": project_all, "type": "list"})


class AddProject(View):
	"""
	添加项目
	"""
	def post(self, request):
		add_project_form = AddProjectForm(request.POST)
		if add_project_form.is_valid():
			name = add_project_form.cleaned_data['name']
			if Project.objects.filter(name=name):
				return render(request, "project_manage.html", {
					"type": 'add',
					"form": add_project_form,
					"msg": "项目已经存在!",
				})
			describe = add_project_form.cleaned_data['describe']
			status = add_project_form.cleaned_data['status']
			Project.objects.create(name=name, describe=describe, status=status)
			return HttpResponseRedirect('/manage/project_manage/')

	def get(self, request):
		add_project_form = AddProjectForm(request.GET)
		return render(request, 'project_manage.html', {
			'form': add_project_form,
			'type': 'add',
		})


class EditProject(View):
	"""编辑项目"""
	def post(self, request, pid):
		form = AddProjectForm(request.POST)
		if form.is_valid():
			data = Project.objects.get(id=pid)
			data.name = form.cleaned_data["name"]
			data.describe = form.cleaned_data["describe"]
			data.status = form.cleaned_data["status"]
			data.save()
			return HttpResponseRedirect("/manage/project_manage/")

	def get(self, request, pid):
		if pid:
			project1 = Project.objects.get(id=pid)
			project_form = AddProjectForm(instance=project1)
		else:
			project_form = AddProjectForm()
		return render(request, 'project_manage.html', {
			'form': project_form,
			"type": "edit",
		})


class DeleteProject(View):
	"""删除项目"""
	def get(self, request, pid):
		Project.objects.get(id=pid).delete()
		return HttpResponseRedirect("/manage/project_manage/")

