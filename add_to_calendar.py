import tornado.web
import tornado.escape
import socket
import urllib.parse as parse

import json
import pprint
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
        self.render("add_to_calendar.html")

    def post(self):
        file = open("calendar.json", "r")

        events = json.load(file)

        date = self.get_argument("date", True)
        time = self.get_argument("time", True)
        extra = self.get_argument("extra", True)

        name = self.get_argument("name", True)

        name = parse.unquote(name)

        print(extra)

        extra_hours = int(extra[:2]) + int(time[:2])
        extra_minutes = int(extra[3:]) + int(time[3:])

        if extra_minutes > 59:
            extra_hours += 1
            extra_minutes -= 60

        extra_hours = str(extra_hours)
        extra_minutes = str(extra_minutes)

        if len(extra_minutes) == 1:
            extra_minutes += '0'

        year = date[:4]
        month = date[5:7]
        day = date[8:]

        if month[:1] == '0':
            month = month[1:]

        if day[:1] == '0':
            day = day[1:]

        try:
            events[year][month][day] = []

            events[year][month][day].append({
                "duration": {
                    "init": time,
                    "final": extra_hours + ':' + extra_minutes
                },
                "name": name})

        except:
            try:
                events[year][month] = {day: []}

                minutes = time[2:] + extra[2:]

                events[year][month][day].append({
                    "duration": {
                        "init": time,
                        "final": extra_hours + ':' + extra_minutes
                    },
                    "name": name})

            except:
                events[year] = {month: {day: []}}

                events[year][month][day].append({
                    "duration": {
                        "init": time,
                        "final": extra_hours + ':' + extra_minutes
                    },
                    "name": name})


        json.dump(events, open("calendar.json", "w"), indent=4, sort_keys=True)

        pprint.pprint(events)

        self.redirect_to_main()
