__author__ = 'caden'
__data__ = ' 22:15'

from django.urls import path, include
from .views import project_views, module_views

urlpatterns = [
    # 项目管理
    path('project_manage/', project_views.ProjectManage.as_view(), name="project_manage"),
    path('add_project/', project_views.AddProject.as_view(), name="add_project"),
    path('edit_project/<int:pid>', project_views.EditProject.as_view(), name="edit_project"),
    path('delete_project/<int:pid>', project_views.DeleteProject.as_view(), name="delete_project"),
    path('view_project/<int:pid>', project_views.ViewProject.as_view(), name="view_project"),
    path('search_project_name/', project_views.SearchProjectName.as_view(), name="search_project_name"),

    # 模块管理
    path('module_manage/', module_views.ModuleManage.as_view(), name="module_manage"),
    path('add_module/', module_views.AddModule.as_view(), name="add_module"),
    path('edit_module/<int:mid>', module_views.EditModule.as_view(), name="edit_module"),
    path('delete_module/<int:mid>', module_views.DeleteModule.as_view(), name="delete_project"),
    path('search_module_name/', module_views.SearchModuleName.as_view(), name="search_module_name"),
]