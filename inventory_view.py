import tornado.web
import tornado.escape
import socket
import urllib.parse as parse

import json


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        inventory = json.load(open("inventory.json", "r"))

        self.render("inventory_view.html", inventory=inventory)
