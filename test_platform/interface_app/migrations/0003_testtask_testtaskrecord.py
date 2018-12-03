# Generated by Django 2.1.1 on 2018-12-03 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0004_department'),
        ('interface_app', '0002_auto_20181110_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='任务名称')),
                ('describe', models.TextField(default='', max_length=100, verbose_name='任务描述')),
                ('status', models.CharField(choices=[('y0', '未执行'), ('y1', '执行中'), ('y2', '排队中'), ('y3', '执行完成'), ('y4', '故障中')], default='y0', max_length=10, verbose_name='任务状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('case_id', models.ManyToManyField(to='interface_app.TestCase')),
                ('creator', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user_app.UserInfo', verbose_name='任务创建者')),
            ],
            options={
                'verbose_name': '任务管理表',
                'verbose_name_plural': '任务管理表',
            },
        ),
        migrations.CreateModel(
            name='TestTaskRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.BooleanField(verbose_name='任务执行结果')),
                ('work_start_time', models.DateTimeField(verbose_name='任务开始时间')),
                ('work_end_time', models.DateTimeField(verbose_name='任务结束时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.UserInfo', verbose_name='任务执行者')),
                ('testtask_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface_app.TestTask', verbose_name='测试任务id')),
            ],
            options={
                'verbose_name': '任务执行记录表',
                'verbose_name_plural': '任务执行记录表',
            },
        ),
    ]