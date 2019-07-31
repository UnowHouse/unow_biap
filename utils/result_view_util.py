
from models.result_model import code_msg

def get_require_data():
	request_type = {
		'device': {
			'model': False,
			'plat': False,
			'version': False,
		},
		'file': {
			'type': False,
			'data': False,
		},
		'person_id': False,
		'request_id': False,
	}
	return request_type

def is_valid_json(require_data,data):
	tag = True
	for key in require_data:
		if key in data.keys():
			if require_data[key] != False:
				tag = is_valid_json(require_data[key], data[key])
		else:
			return False
		if not tag:
			return False
	return True

def get_result_model():

	return 	{
				'code': '',
				'msg': '',
			    'request_id': '0',
			    'data': {},
			    'response_id': '0',
			    'detect_cost_time': 0
			}

def success(data):
	result = get_result_model()
	result['code'] = '0'
	result['msg'] = code_msg['0']
	result['data'] = data
	return result

def error(status_code):
	result = get_result_model()
	result['code'] = status_code
	result['msg'] = code_msg[status_code]
	return result


