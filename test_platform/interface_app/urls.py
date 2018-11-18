from django.urls import path, include
from .views import testcase_views

urlpatterns = [
    # 用例管理URL路径
    path('case_manage/', testcase_views.CaseManage.as_view(), name="case_manage"),
    path('debug_case/<int:case_id>/', testcase_views.EditCase.as_view(), name="edit_case"),
    path('api_debug/', testcase_views.DebugCase.as_view(), name="api_debug"),
    path('add_case/', testcase_views.AddCase.as_view(), name="add_case"),
    path('save_case/', testcase_views.SaveCase.as_view(), name="save_case"),
    path('edit_save_case/', testcase_views.EditSaveCase.as_view(), name="edit_save_case"),
    path('get_project_list/', testcase_views.GetProjectList.as_view(), name="project_list"),
    path('search_case_name/', testcase_views.SearchCaseName.as_view(), name="search_case_name"),
    path('get_case_info/', testcase_views.GetCase.as_view(), name="get_case_info"),
    path('api_assert/', testcase_views.ApiAssert.as_view(), name="api_assert"),
    path('delete_case/<int:case_id>/', testcase_views.DeleteCase.as_view(), name="delete_case"),
]
