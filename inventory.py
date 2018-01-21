import tornado.web
import tornado.escape
import socket
import urllib.parse as parse


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("inventory_main.html")
