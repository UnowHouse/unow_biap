#coding=utf-8

import tornado.web
from tornado.escape import json_encode,json_decode
from utils.common_util import valid_file_size
import utils.result_view_util as result_utils 
# 导入人数检测模块
# import ....


class FaceCountHandler(tornado.web.RequestHandler):
	

	def set_default_headers(self):
        # 设置请求头
		self.set_header('Content-Type', 'application/json')

	def post(self):
		request_body = json_decode(self.request.body)
		if not result_utils.is_valid_json(result_utils.get_require_data(),request_body):
			self.write(json_encode(result_utils.error('20004')))
			return
		if valid_file_size(request_body['file']['data'],2):	
			img_arr = common_util.base64_2_array(request_body['file']['data'])
			# 
			# 将img_arr 传入 ’检测函数‘
			# 将输出的检测结果(假如名为detect_result)作为参数 传入下方success函数
			#  result = result_utils.success(detect_result)
			#
			detect_result = {}
			result = result_utils.success(detect_result)

			self.write(json_encode(result))
		else:
			self.write(json_encode(result_utils.error('20006')))


class ErrorHandler(tornado.web.RequestHandler):

	def set_default_headers(self):
        # 设置请求头
		self.set_header('Content-Type', 'application/json')

	def get(self,_):
		# self.set_statues(404)
		self.write(json_encode(result_utils.error('20009')))


