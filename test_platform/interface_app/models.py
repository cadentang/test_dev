from django.db import models


# Create your models here.
class Case(models.Model):
	status_choice = (
		(True, '开启'),
		(False, '关闭'),
	)
	name = models.CharField(verbose_name="名称", max_length=100, blank=True, null=True)
	describe = models.TextField(verbose_name="描述", max_length=100, default="")
	status = models.BooleanField(verbose_name="状态", choices=status_choice)
	create_time = models.DateTimeField(verbose_name="创建时间", auto_now=True)

	class Meta:
		verbose_name = "用例管理"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.get_status_display()