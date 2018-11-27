from django.http import JsonResponse

def response_succeed(message="请求成功", data={}):
	"""
	响应成功
	:param message: 
	:param data: 
	:return: 
	"""
	content = {
		"success": "true",
		"message": message,
		"data": data,
	}
	return JsonResponse(content)


def response_failed(message="请求失败"):
	"""
	响应失败
	:param message: 
	:return: 
	"""
	content = {
		"success": "true",
		"message": message,
	}
	return JsonResponse(content)
