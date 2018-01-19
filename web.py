import tornado.web
import tornado.escape
import socket
from urllib import parse

class MainWeb(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")