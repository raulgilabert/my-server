import tornado.web
import tornado.escape
import socket
import urllib.parse as parse

import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("to_do.html", list=json.load("to_do.json"))
