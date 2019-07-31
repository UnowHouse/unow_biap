#coding=utf-8
import cv2
import numpy as np
import base64

def valid_file_size(base64_data, limited_size):
	data = base64_data[:base64_data.find('=')]
	data_len = len(data)
	file_size = data_len-((data_len/8) * 2)

	return (file_size/1024/1024) <= limited_size

def base64_2_array(base64_data):
    im_data = base64.b64decode(base64_data)
    im_array = np.frombuffer(im_data, np.uint8)
    im_array = cv2.imdecode(im_array, cv2.COLOR_RGB2BGR)
    return im_array