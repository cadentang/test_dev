from django.apps import AppConfig
from test_platform.settings import BASE_DIR


class InterfaceAppConfig(AppConfig):
    name = 'interface_app'
    verbose_name = "用例管理"

# 配置任务运行目录
BASE_PATH = BASE_DIR.replace("\\", "/")
TASK_PATH = BASE_PATH + "/resource/tasks/"
RUN_TASK_FILE = BASE_PATH + "/interface_app/extend/task_run.py"