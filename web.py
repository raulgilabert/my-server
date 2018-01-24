import tornado.web
import tornado.escape
import socket
from urllib import parse

import json

class MainWeb(tornado.web.RequestHandler):
    def get(self):
        self.render("main.html")