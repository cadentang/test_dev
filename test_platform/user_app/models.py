from django.db import models

# Create your models here.


class UserInfo(models.Model):
	user = models.CharField(max_length=32)
	password = models.CharField(max_length=32)


class ProjectManage(models.Model):
	project_name = models.CharField(max_length=100)
	project_master = models.CharField(max_length=10)
	project_detail = models.CharField(max_length=200)
