__author__ = 'caden'
__data__ = ' 22:15'

from django.urls import path, include
from . import views
from .views import AddProject

urlpatterns = [
    path('project_manage/', views.project_manage, name="project_manage"),
    path('add_project/', views.add_project, name="add_project"),
    path('submit_project/', AddProject.as_view(), name="submit_project"),
    path('edit_project/<int:pid>', views.edit_project, name="edit_project"),
    path('delete_project/<int:pid>', views.delete_project, name="delete_project")
]