from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from .models import Project, Module
from .forms import AddProjectForm

# Create your views here.


@login_required
def project_manage(request):
	"""
	项目管理视图
	"""
	username = request.session.get("user1", "")
	project_all = Project.objects.all()
	return render(request, "project_manage.html", {"user": username, "projects": project_all, "type": "list"})


@login_required
def add_project(request):
	"""
	添加项目视图 
	"""
	add_project_form = AddProjectForm(request.POST)
	if add_project_form.is_valid():
		name = request.POST.get("name", "")
		describe = request.POST.get("describe", "")
		status = request.POST.getlist("status", "")
		s = status[0]
		if Project.objects.filter(name=name):
			return render(request, "project_manage.html", {"add_project_form": add_project_form, "msg": "项目已经存在"})
		project = Project()
		project.name = name  # 接收表单传过来的数据
		project.describe = describe
		project.status = s
		project.save()  # 保存到数据库
		username = request.session.get("user1", "")
		project_all = Project.objects.all()
		return render(request, "project_manage.html", {"user": username, "projects": project_all, "type": "list"})
	else:
		return render(request, "project_manage.html", {"type": "add"})


class AddProject(View):
	"""
	用类实现视图，功能还未完善
	"""
	def post(self, request):
		add_project_form = AddProjectForm(request.POST)
		if add_project_form.is_valid():
			name = request.POST.get("name", "")
			if Project.objects.filter(name=name):
				return render(request, "project_manage.html", {"add_project_form": add_project_form, "msg":"项目已经存在！"})
			describe = request.POST.get("describe", "")
			status = request.POST.get("status", "")
			project = Project()
			project.name = name
			project.describe = describe
			project.status = status
			project.save()
		return render(request, "project_manage.html", {"type": "add"}, {"add_project_form": AddProjectForm})

	def get(self, request):
		pass



