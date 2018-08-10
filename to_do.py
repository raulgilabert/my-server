import tornado.web
import tornado.escape
import socket
import urllib.parse as parse

import json
import datetime

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
        args = self.request.arguments

        date = datetime.datetime.now()

        if len(str(date.day)) == 1:
            day = "0" + str(date.day)

        else:
            day = date.day

        if len(str(date.month)) == 1:
            month = "0" + str(date.month)

        else:
            month = date.month

        today = str(day) + "/" + str(month) + "/" + str(date.year)

        print(today)

        day = open("day.txt", "r")

        if day.readline() != today:
            file = open("day.txt", "w")
            file.write(today)
            file.close()

            data = json.load(open("to_do.json", "r"))

            for dat in data:
                data[dat] = 0

            json.dump(data, open("to_do.json", "w"), indent=4, sort_keys=True)

        data = json.load(open("to_do.json", "r"))

        for arg in args:
            value = args[arg][0].decode("utf-8")

            print(value)

            if value == "on":
                data[arg] = 1

            json.dump(data, open("to_do.json", "w"), indent=4, sort_keys=True)

        if args != {}:
            self.redirect_to_main()

        else:
            data = json.load(open("to_do.json", "r"))

            done = []
            to_do = []

            for element in data:
                if data[element] == 0:
                    to_do.append(element)
                else:
                    done.append(element)

            self.render("to_do.html", done=done, to_do=to_do)
