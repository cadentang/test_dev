from django.urls import path, include
from .views import testcase_views


urlpatterns = [
    # 用例管理URL路径
    path('case_manage/', testcase_views.CaseManage.as_view(), name="case_manage"),
    path('debug_case/<int:case_id>/', testcase_views.EditCase.as_view(), name="edit_case"),
    path('add_case/', testcase_views.AddCase.as_view(), name="add_case"),
    path('save_case/', testcase_views.SaveCase.as_view(), name="save_case"),
    path('get_project_list/', testcase_views.GetProjectList.as_view(), name="project_list"),
    path('search_case_name/', testcase_views.SearchCaseName.as_view(), name="search_case_name"),
    path('get_case_info/', testcase_views.GetCase.as_view(), name="get_case_info"),
    # path('add_case/', project_views.AddProject.as_view(), name="add_project"),
    # path('edit_case/<int:pid>', project_views.EditProject.as_view(), name="edit_project"),
    # path('delete_case/<int:pid>', project_views.DeleteProject.as_view(), name="delete_project"),
    # path('view_case/<int:pid>', project_views.ViewProject.as_view(), name="view_project"),
]
