from django.contrib import admin
from .models import TestCase

# Register your models here.


class TestCaseAdmin(admin.ModelAdmin):
	"""测试用例"""
	list_display = ["module", "name", "response_url", "response_type", "response_header", "response_parameter", "response_assert", "status", "create_time"]
	list_filter = ["module", "name", "response_url", "response_type", "status", "create_time"]
	search_fields = ["module", "name", "response_url", "response_type", "status", "create_time"]

admin.site.register(TestCase, TestCaseAdmin)