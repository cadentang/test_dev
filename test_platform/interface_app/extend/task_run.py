from ddt import ddt, data, unpack, file_data
import xmlrunner, json, requests
import sys, unittest
from os.path import dirname, abspath


BASE_DIR = dirname(dirname(dirname(abspath(__file__))))
BASE_PATH = BASE_DIR.replace("\\", "/")
sys.path.append(BASE_PATH)

TASK_PATH = BASE_PATH + "/resource/tasks/"


@ddt
class InterfaceTest(unittest.TestCase):

	@unpack
	@file_data(TASK_PATH + "cases_data.json")
	#@data(TASK_PATH + "cases_data.json")
	def test_cun_cases(self, url, method, type_, header, parameter, assert_):
		if header == "{}":
			header_dict = {}
		else:
			# aa = header.replace("\'", "\"")
			# print(aa)
			# header_dict = json.loads(aa)
			header_dict = header

		if parameter == "{}":
			parameter_dict = {}
		else:
			# bb = parameter.replace("\'", "\"")
			# print(bb)
			# parameter_dict = json.loads(bb)
			parameter_dict = parameter

		if method == "get":
			if type_ == "from":
				r = requests.get(url, headers=header_dict, params=parameter_dict)

		if method == "post":
			if type_ == "from":
				r = requests.post(url, headers=header_dict, data=parameter_dict)
			elif type_ == "json":
				r = requests.post(url, headers=header_dict, json=parameter_dict)


# 运行测试用例
def run_cases():
	# with open(TASK_PATH + "results.xml", "wb") as output:
	# 	unittest.main(
	# 		testRunner=xmlrunner.XMLTestRunner(output=output),
	# 		failfast=False, buffer=False, catchbreak=False
	# 	)
	pass

#
# if __name__ == "__main__":
# 	run_cases()


