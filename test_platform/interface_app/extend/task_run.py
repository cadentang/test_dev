import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_platform.settings")
import django  # 加载django

django.setup()  # 启动django

from ddt import ddt, data, unpack, file_data
import xmlrunner, json, requests
import sys, unittest
from os.path import dirname, abspath
from ..models import TestTask

BASE_DIR = dirname(dirname(dirname(abspath(__file__))))
BASE_PATH = BASE_DIR.replace("\\", "/")
sys.path.append(BASE_PATH)

TASK_PATH = BASE_PATH + "/resource/tasks/"
cases_data =[]

def get_case_data(task_id):
	queryset = TestTask.objects.get(id=task_id)
	task_cases = queryset.case_id.all()
	task_cases_list = []
	for task_case in task_cases:
		task_case_dict = {
			"case_id": task_case.id,
			"response_url": task_case.response_url,
			"response_method": task_case.response_method,
			"response_type": task_case.response_type,
			"response_header": task_case.response_header,
			"response_parameter": task_case.response_parameter,
			"response_assert": task_case.response_assert,
		}
		task_cases_list.append(task_case_dict)
	return task_cases_list

@ddt
class InterfaceTest(unittest.TestCase):

	@unpack
	@file_data(TASK_PATH + "cases_data.json")
	#@data(*cases_data)
	def test_cun_cases(self, response_url, response_method,
	                   response_type, response_header, response_parameter, response_assert):
		print(">>>请求url：", response_url)
		print(">>>请求方法：", response_method)
		print(">>>请求数据类型：", response_type)
		print(">>>请求头部：", response_header)
		print(">>>请求参数：", response_parameter)
		print(">>>用例断言：", response_assert)
		if response_parameter == "{}":
			header_dict = {}
		else:
			aa = response_parameter.replace("\'", "\"")
			header_dict = json.loads(aa)

		if response_parameter == "{}":
			parameter_dict = {}
		else:
			aa = response_parameter.replace("\'", "\"")
			parameter_dict = json.loads(aa)

		if response_method == "get":
			if response_type == "from":
				r = requests.get(response_url, headers=header_dict, params=parameter_dict)

		if response_method == "post":
			if response_type == "from":
				r = requests.post(response_url, headers=header_dict, data=parameter_dict)
			elif response_type == "json":
				r = requests.post(response_url, headers=header_dict, json=parameter_dict)


# 运行测试用例
def run_cases():
	#ases_data = get_case_data(id)
	with open(TASK_PATH + "results.xml", "w") as output:
		# unittest.main(
		# 	testRunner=xmlrunner.XMLTestRunner(output=output),
		# 	failfast=False, buffer=True, catchbreak=False,argv = sys.argv[:1],exit = False
		# )
		test_suite = unittest.TestSuite()
		test_suite.addTest(unittest.makeSuite(InterfaceTest))
		runner = xmlrunner.XMLTestRunner(output=output)
		runner.run(test_suite)

#
# if __name__ == "__main__":
# 	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_platform.settings")
# 	import django  # 加载django
#
# 	django.setup() # 启动django
# 	run_cases()


