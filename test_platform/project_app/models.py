from django.db import models


class Project(models.Model):
	status_choice = (
		(True, '开启'),
		(False, '关闭'),
	)
	name = models.CharField(verbose_name="名称", max_length=100, blank=True, null=True)
	describe = models.TextField(verbose_name="描述", max_length=100, default="")
	status = models.BooleanField(verbose_name="状态", choices=status_choice)
	create_time = models.DateTimeField(verbose_name="创建时间", auto_now=True)

	class Meta:
		verbose_name = "项目管理"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name
		#return self.get_status_display()


class Module(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="项目")
	name = models.CharField("名称", max_length=100, blank=True, null=True)
	describe = models.TextField("描述", max_length=100, default="")
	status = models.BooleanField("状态", default=True)
	create_time = models.DateTimeField("创建时间", auto_now=True)

	class Meta:
		verbose_name = "模块管理"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name