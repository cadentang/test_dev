from django.db import models

# Create your models here.
class Project(models.Model):
	name = models.CharField("名称", max_length=100, blank=True, null=True)
	describe = models.TextField("描述", max_length=100, default="")
	status = models.BooleanField("状态", default=True)
	create_time = models.DateTimeField("创建时间", auto_now=True)

	class Meta:
		verbose_name = "项目管理"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name


class Module(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	name = models.CharField("名称", max_length=100, blank=True, null=True)
	describe = models.TextField("描述", max_length=100, default="")
	status = models.BooleanField("状态", default=True)
	create_time = models.DateTimeField("创建时间", auto_now=True)

	class Meta:
		verbose_name = "模块管理"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name