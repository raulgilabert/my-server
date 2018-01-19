import tornado.web
import tornado.escape
import socket
from urllib import parse

import phue


class MainHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

    def get(self):
        bridge = phue.Bridge(ip="10.135.1.167")

        bridge.connect()

        function = self.get_argument("function", True)
        name = self.get_argument("light", True)
        value = self.get_argument("value", True)

        print(name)

        if isinstance(function, str):
            function = parse.unquote(function)

        if isinstance(name, str):
            name = parse.unquote(name)

        light = phue.Group(bridge, name)

        if function == "Turn-on":
            light.on = True

        elif function == "Turn-off":
            light.on = False

        elif function == "Brightness":
            light.brightness = int(value)

        self.render("lights.html", groups=bridge.groups)
