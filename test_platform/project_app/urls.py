__author__ = 'caden'
__data__ = ' 22:15'

from django.urls import path, include
from .views import project_views, module_views

# 项目管理
urlpatterns = [
    # path('project_manage/', project_views.project_manage, name="project_manage"),
    path('project_manage/', project_views.ProjectManage.as_view(), name="project_manage"),
    # path('add_project/', project_views.add_project, name="add_project"),
    path('add_project/', project_views.AddProject.as_view(), name="add_project"),
    # path('edit_project/<int:pid>', project_views.edit_project, name="edit_project"),
    path('edit_project/<int:pid>', project_views.EditProject.as_view(), name="edit_project"),
    # path('delete_project/<int:pid>', project_views.delete_project, name="delete_project")
    path('delete_project/<int:pid>', project_views.DeleteProject.as_view(), name="delete_project")
]

# # 模块管理
# urlpatterns = [
#     path('module_manage/', module_views.module_manage, name="module_manage"),
#     path('add_module/', module_views.add_module, name="add_module"),
#     #path('submit_project/', module_views.AddProject.as_view(), name="submit_project"),
#     path('edit_module/<int:mid>', module_views.edit_module, name="edit_module"),
#     path('delete_module/<int:mid>', module_views.delete_project, name="delete_project")
# ]