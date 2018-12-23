from django.db import models
from project_app.models import Module
from django.contrib.auth.models import User

task_status_choice = (
	('y0', '未执行'),
	('y1', '执行中'),
	('y2', '排队中'),
	('y3', '执行完成'),
	('y4', '故障中'),
)

class TestCase(models.Model):
	"""
	测试用例
	"""
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
		#return self.get_status_display()
		return self.name


class TestTask(models.Model):
	"""
	测试任务
	"""
	name = models.CharField(verbose_name="任务名称", max_length=100, blank=False)
	describe = models.TextField(verbose_name="任务描述", max_length=100, default="")
	status = models.CharField(verbose_name="任务状态", default="y0", max_length=10, choices=task_status_choice)
	creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="任务创建者" )
	create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
	case_id = models.ManyToManyField(TestCase)

	class Meta:
		verbose_name = "任务管理表"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name


class TestTaskRecord(models.Model):
	"""
	测试任务执行记录
	"""
	testtask_id = models.ForeignKey(TestTask, on_delete=models.CASCADE, verbose_name="测试任务id")
	operator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="任务执行者" )
	result =  models.BooleanField(verbose_name="任务执行结果")  # True:成功，False: 失败
	work_start_time = models.DateTimeField(verbose_name="任务开始时间")
	work_end_time = models.DateTimeField(verbose_name="任务结束时间")
	create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
	name = models.CharField(verbose_name="名称", max_length=100, blank=False, default="")
	error = models.IntegerField(verbose_name="错误用例")
	failure = models.IntegerField(verbose_name="失败用例")
	skipped = models.IntegerField(verbose_name="跳过用例")
	tests = models.IntegerField(verbose_name="总用例数")
	run_time = models.FloatField(verbose_name="运行时长")
	result_describle = models.TextField(verbose_name="详细", default="")


	class Meta:
		verbose_name = "任务执行记录表"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name