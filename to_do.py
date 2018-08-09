import tornado.web
import tornado.escape
import socket
import urllib.parse as parse

import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            arguments = json.dumps({ k: self.get_argument(k) for k in self.request.arguments })
            print("ok")

#            json.dump(open("done.json", "w"), arguments)

        except:
            arguments = json.load(open("done.json"))


        self.render("to_do.html", list=json.load(open("to_do.json","r")), done=arguments)
