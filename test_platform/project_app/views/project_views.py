from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from ..models import Project
from ..forms import AddProjectForm


@login_required
def project_manage(request):
	"""
	项目管理视图
	"""
	username = request.session.get("user1", "")
	project_all = Project.objects.all()
	return render(request, "project_manage.html", {"user": username, "projects": project_all, "type": "list"})


class ProjectManage(View):
	"""
	项目管理
	"""
	def get(self, request):
		username = request.session.get("user1", "")
		project_all = Project.objects.all()
		paginator = Paginator(project_all, 10)
		page = request.GET.get('page', 1)
		start = (int(page) - 1) *10
		try:
			projects = paginator.page(page)
		except PageNotAnInteger:
			projects = paginator.page(1)
		except EmptyPage:
			projects = paginator.page(paginator.num_pages)
		return render(request, "project_manage.html", {
			"user": username,
			"projects": projects,
			"type": "list",
			"start": start,
		})


@login_required
def add_project(request):
	"""
	添加项目视图 
	"""
	if request.method == 'POST':
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
	else:
		add_project_form = AddProjectForm()
	return render(request, 'project_manage.html', {
		'form': add_project_form,
		'type': 'add',
	})


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


@login_required
def edit_project(request, pid):
	"""编辑项目"""
	if request.method == 'POST':
		form = AddProjectForm(request.POST)
		if form.is_valid():
			data = Project.objects.get(id=pid)
			print(type(data))
			data.name = form.cleaned_data["name"]
			data.describe = form.cleaned_data["describe"]
			data.status = form.cleaned_data["status"]
			data.save()
			return HttpResponseRedirect("/manage/project_manage/")
	else:
		if pid:
			print(pid)
			project1 = Project.objects.get(id=pid)
			print(project1)
			project_form = AddProjectForm(instance=project1)
		else:
			project_form = AddProjectForm()
	return render(request, 'project_manage.html', {
		'form': project_form,
		"type": "edit",
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


class ViewProject(View):
	"""查看视图"""
	def get(self, request, pid):
		if pid:
			project1 = Project.objects.get(id=pid)
			project_form = AddProjectForm(instance=project1)
		else:
			project_form = AddProjectForm()
		return render(request, 'project_manage.html', {
			'form': project_form,
			"type": "view",
		})


class DeleteProject(View):
	"""删除项目"""
	def get(self, request, pid):
		Project.objects.get(id=pid).delete()
		return HttpResponseRedirect("/manage/project_manage/")


class SearchProjectName(View):
	"""搜索项目，维度：项目名称、项目状态"""
	def get(self, request):
		project_name = request.GET.get("project_name", "")
		status = request.GET.get("status", "")
		project_all = Project.objects.filter(name__contains=project_name)
		paginator = Paginator(project_all, 10)
		page = request.GET.get('page', 1)
		start = (int(page) - 1) *10
		try:
			projects = paginator.page(page)
		except PageNotAnInteger:
			projects = paginator.page(1)
		except EmptyPage:
			projects = paginator.page(paginator.num_pages)
		return render(request, "project_manage.html", {
			"user": username,
			"projects": projects,
			"type": "list",
			"start": start,
		})

