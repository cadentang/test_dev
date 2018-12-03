from django.contrib import admin
from .models import TestCase, TestTask


class TestCaseAdmin(admin.ModelAdmin):
	"""测试用例"""
	list_display = ["module", "name", "response_url", "response_type", "response_header", "response_parameter", "response_assert", "status", "create_time"]
	list_filter = ["module", "name", "response_url", "response_type", "status", "create_time"]
	search_fields = ["module", "name", "response_url", "response_type", "status", "create_time"]


class TestTaskAdmin(admin.ModelAdmin):
	"""任务管理"""
	list_display = ["name", "describe", "status", "creator", "create_time"]
	#list_filter = ["name", "describe", "status", "creator"]
	search_fields = ["name", "describe", "status", "creator"]


admin.site.register(TestCase, TestCaseAdmin)
admin.site.register(TestTask, TestTaskAdmin)