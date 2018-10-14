# -*- coding utf-8 -*-

import tornado.web
import tornado.escape
import socket
import urllib.parse as parse

import json
import datetime
import pprint


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

        now_day = int(day)

        month = int(month)

        day = open("day.txt", "r")

        dat = day.readline()

        print(dat)

        day = dat

        if day != today:
            print(day)

            print("day: ", day[6:], day[3:5], day[:2])

            print(datetime.date(date.year, month, now_day) - datetime.date(int(day[6:]), int(day[3:5]), int(day[:2])))

            file = open("day.txt", "w")
            file.write(today)
            file.close()

            data = json.load(open("to_do.json", "r"))

            days = datetime.date(date.year, month, now_day) - datetime.date(int(day[6:]), int(day[3:5]), int(day[:2]))

            for dat in data:
                print(days.days)

                data[dat] = [0, data[dat][1] + days.days]

            json.dump(data, open("to_do.json", "w"), indent=4, sort_keys=True)

        data = json.load(open("to_do.json", "r"))

        for arg in args:
            print(arg.encode("ISO-8859-1"))

            value = args[arg][0].decode("utf-8")

            print(value)

            arg = parse.unquote(arg)

            pos = arg.find("Ã±")

            if pos != -1:
                arg = arg[:pos] + "ñ" + arg[pos+2:]

            if value == "on":
                data[arg] = [1,0]

            json.dump(data, open("to_do.json", "w"), indent=4, sort_keys=True)

        if args != {}:
            self.redirect_to_main()

        else:
            data = json.load(open("to_do.json", "r"))

            done = []
            to_do = {}

            for element in data:
                print(element)

                if data[element][0] == 0:
                    to_do[element] = data[element][1] - 1
                else:
                    done.append(element)

            self.render("to_do.html", done=done, to_do=to_do)
