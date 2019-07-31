#coding=utf-8

from handlers.main_handlers import FaceCountHandler,ErrorHandler
from tornado.web import StaticFileHandler

handlers = [
	(r'/biap/face/v1/bodycount', FaceCountHandler),
	(r'/(.*)', ErrorHandler),
]