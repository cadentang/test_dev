from django.contrib import admin
from .models import Project, Module

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
	"项目管理model"
	list_display = ["name", "describe", "status", "create_time", "id"]
	list_filter = ['name', 'status']
	search_fields = ['name', 'status']


class ModuleAdmin(admin.ModelAdmin):
	"模块管理model"
	list_display = ["project", "name", "describe", "status", "create_time", "id"]
	list_filter = ["project", "name", "status"]
	search_fields = ['project', 'name', 'status']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Module, ModuleAdmin)
