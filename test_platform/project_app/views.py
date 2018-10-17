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
	"""

@login_required
def edit_project(request, pid):
	"""编辑项目"""

	"""
	def post(self, request, *args, **kwargs):
        loc = self.kwargs['name']
        try:
            location = Location.objects.get(name=loc)
            form = locationForm (request.POST, instance=location)
            if form.is_valid():
                form.save()
            else:
                form = locationForm(request.POST, instance=location)
                return render(request, self.template_name, {'location': location, 'form': form})

        except (ValueError, ObjextDoesNotExist):
            return redirect(reverse('location_manager'))
        return redirect(reverse('location_manager'))
        """
	if request.method == 'POST':
		pass
		'''
		g = Project.objects.get(id=pid)
		g.status = 0
		g.save()
		Project.objects.select_for_update().filter(name__contains='项目').update(describe='')'''
	else:
		if pid:
			print(pid)
			project1 = Project.objects.filter(id=pid)
			print(project1)
			project_form = AddProjectForm(project1)
		else:
			project_form = AddProjectForm()
	return render(request, 'project_manage.html', {
		'form': project_form,
		"type": "edit",
	})


def delete_project(request, pid):
	"""删除项目"""
	Project.objects.get(name='xxx测试项目').delete()



class DeleteProject(View):
	"""删除项目"""
	def post(self, request):
		name = request.POST.get("name", "")
		Project.objects.get(name='yy').delete()
