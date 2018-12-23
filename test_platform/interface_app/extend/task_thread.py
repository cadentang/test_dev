import os, json, threading
from time import sleep
from xml.dom import minidom

from ..models import TestTask, TestCase, TestTaskRecord
from ..apps import TASK_PATH, RUN_TASK_FILE
from test_platform import common


class TaskThread:
	"""
	实现测试任务的多线程执行
	"""
	def __init__(self, task_id):
		self.task_id = task_id

	def run_cases(self):
		not_run_task_status_choice = ["y1", "y2", "y3"]
		queryset = TestTask.objects.get(id=self.task_id)
		task_cases = queryset.case_id.all()

		if queryset.status not in not_run_task_status_choice:
			queryset.status = "y1"
			queryset.save()
		else:
			return common.response_succeed(message="当前状态不能执行任务：%s" % (queryset.name))

		task_cases_dict = {}
		for task_case in task_cases:
			task_case_dict = {
				"response_url": task_case.response_url,
				"response_method": task_case.response_method,
				"response_type": task_case.response_type,
				"response_header": task_case.response_header,
				"response_parameter": task_case.response_parameter,
				"response_assert": task_case.response_assert,
			}
			task_cases_dict[task_case.id] = task_case_dict

		task_cases_json = json.dumps(task_cases_dict)
		case_data_file = TASK_PATH + "cases_data.json"
		with open(case_data_file, "w+") as f:
			f.write(task_cases_json)

	def save_result(self):
		"""保存测试结果，将xml报告中的数据存放在数据库中"""
		dom = minidom.parse(TASK_PATH + "results.xml")
		root = dom.documentElement
		ts = root.getElementsByTagName("testsuite")
		errors = ts[0].getAttribute("errors")
		failures = ts[0].getAttribute("failures")
		skipped = ts[0].getAttribute("skipped")
		tests = ts[0].getAttribute("tests")
		name = ts[0].getAttribute("name")
		run_time = ts[0].getAttribute("time")

		with(open(TASK_PATH + 'results.xml', "r", encoding="utf-8")) as f:
			result_text = f.read()

		results = TestTaskRecord.objects.create(name=name,
		                                        errors=errors,
		                                        failures=failures,
		                                        skipped=skipped,
		                                        tests=tests,
		                                        run_time=run_time,
		                                        result_describle=result_text)

	def run(self):
		threads = []
		t = threading.Thread(target=self.run_cases(), args=(self.task_id,))
		threads.append(t)

		for t in threads:
			t.start()

		for t in threads:
			t.join()
		sleep(2)
		print("当任务运行完成之后...")
		self.save_result()
		testtask = TestTask.objects.get(id=self.task_id)
		testtask.status = "y3"
		testtask.save()

	def new_run(self):
		threads = []
		t = threading.Thread(target=self.run())
		threads.append(t)

		for t in threads:
			t.start()