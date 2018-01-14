import tornado.web
import tornado.escape
import socket
from urllib import parse

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        level = self.get_argument("level")

