import tornado.web
import tornado.escape
from urllib import parse

import phue


class MainHandler(tornado.web.RequestHandler):
    def redirect_to_main(self):
        txt = ""

        for character in self.request.uri:
            if character != "?":
                txt += character

            else:
                break

        self.redirect(txt)

    def get(self):
        bridge = phue.Bridge(ip="10.135.1.167")

        bridge.connect()

        function = self.get_argument("function", True)
        name = self.get_argument("light", True)
        value = self.get_argument("value", True)

        print(name)

        if isinstance(function, str):
            function = parse.unquote(function)

        else:
            self.render("lights.html", groups=bridge.groups)

        if isinstance(name, str):
            name = parse.unquote(name)

        light = phue.Group(bridge, name)

        if function == "Turn-on":
            light.on = True

            self.redirect_to_main()

        elif function == "Turn-off":
            light.on = False

            self.redirect_to_main()

        elif function == "Brightness":
            light.brightness = int(value)

            self.redirect_to_main()
