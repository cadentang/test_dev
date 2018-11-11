from django.urls import path, include
from .views import testcase_views


urlpatterns = [
    # 用例管理URL路径
    path('case_manage/', testcase_views.CaseManage.as_view(), name="case_manage"),
    path('debug/', testcase_views.Debug.as_view(), name="debug"),
    path('api_debug/', testcase_views.CaseApiDebug.as_view(), name="api_debug"),
    path('save_case/', testcase_views.SaveCase.as_view(), name="save_case"),
    path('get_project_list/', testcase_views.GetProjectList.as_view(), name="project_list"),
    # path('add_case/', project_views.AddProject.as_view(), name="add_project"),
    # path('edit_case/<int:pid>', project_views.EditProject.as_view(), name="edit_project"),
    # path('delete_case/<int:pid>', project_views.DeleteProject.as_view(), name="delete_project"),
    # path('view_case/<int:pid>', project_views.ViewProject.as_view(), name="view_project"),
]
