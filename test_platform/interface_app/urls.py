from django.urls import path, include
from .views import CaseManage, CaseApiDebug

urlpatterns = [
    # 用例管理
    path('case_manage/', CaseManage.as_view(), name="case_manage"),
    path('api_debug/', CaseApiDebug.as_view(), name="api_debug"),
    # path('add_case/', project_views.AddProject.as_view(), name="add_project"),
    # path('edit_case/<int:pid>', project_views.EditProject.as_view(), name="edit_project"),
    # path('delete_case/<int:pid>', project_views.DeleteProject.as_view(), name="delete_project"),
    # path('view_case/<int:pid>', project_views.ViewProject.as_view(), name="view_project"),
]