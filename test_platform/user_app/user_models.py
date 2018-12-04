from django.db import models

# Create your models here.


class UserInfo(models.Model):
	user = models.CharField(max_length=32)
	password = models.CharField(max_length=32)


class Department(models.Model):
	status_choice = (
		(True, '开启'),
		(False, '关闭'),
	)
	type_choice = (
		('0', '管理部门'),
		('1', '产品部门'),
		('2', '前端团队'),
		('3', '后端团队'),
		('4', '移动团队'),
		('5', '测试团队'),
	)
	name = models.CharField(max_length=20, verbose_name="部门名称")
	creator = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="创建者")
	describe = models.TextField("描述", max_length=100, default="")
	status = models.BooleanField("状态", default=True, choices=status_choice)
	create_time = models.DateTimeField("创建时间", auto_now=True)
	update_time = models.DateTimeField("更新时间", auto_now=True)
	department_type = models.CharField(max_length=2, choices=type_choice, verbose_name="部门类型")










