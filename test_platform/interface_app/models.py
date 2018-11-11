from django.db import models
from project_app.models import Module


# Create your models here.
class TestCase(models.Model):
	status_choice = (
		(True, '开启'),
		(False, '关闭'),
	)
	module = models.ForeignKey(Module, on_delete=models.CASCADE)
	name = models.CharField(verbose_name="名称", max_length=100, blank=True, null=True)
	response_url = models.TextField(verbose_name="URL",default="")
	response_method = models.TextField(verbose_name="方法", max_length=100, default="")
	response_type = models.TextField(verbose_name="参数类型", max_length=100, default="")
	response_header = models.TextField(verbose_name="header", default="")
	response_parameter = models.TextField(verbose_name="参数", default="")
	response_assert = models.TextField(verbose_name="断言", default="")
	status = models.BooleanField(verbose_name="状态", choices=status_choice)
	create_time = models.DateTimeField(verbose_name="创建时间", auto_now=True)

	class Meta:
		verbose_name = "用例管理列表"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.get_status_display()