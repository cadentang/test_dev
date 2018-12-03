# Generated by Django 2.1.1 on 2018-12-01 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_auto_20181012_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='部门名称')),
                ('describe', models.TextField(default='', max_length=100, verbose_name='描述')),
                ('status', models.BooleanField(choices=[(True, '开启'), (False, '关闭')], default=True, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('department_type', models.CharField(choices=[('0', '管理部门'), ('1', '产品部门'), ('2', '前端团队'), ('3', '后端团队'), ('4', '移动团队'), ('5', '测试团队')], max_length=2, verbose_name='部门类型')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.UserInfo', verbose_name='创建者')),
            ],
        ),
    ]