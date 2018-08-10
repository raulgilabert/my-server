import tornado.web
import tornado.escape
import socket
import urllib.parse as parse

import json

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
        try:
            task = self.get_argument("task")

            if isinstance(task, str):
                task = parse.unquote(task)

            if task != "":
                data = json.load(open("to_do.json", "r"))

                data[task] = 0

                json.dump(data, open("to_do.json", "w"), indent=4, sort_keys=True)

            self.redirect_to_main()

        except tornado.web.MissingArgumentError:
            self.render("add_to_do.html")
