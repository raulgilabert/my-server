import tornado.web
import tornado.escape
import socket
import urllib.parse as parse

import json

import datetime


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        now = datetime.datetime.now()
        try:
            month = int(self.get_argument("month"))
        except:
            month = now.month

        try:
            year = int(self.get_argument("year"))
        except:
            year = now.year

        try:
            control = self.get_argument("control")

            if control == "back":
                month -= 1

                if month == 0:
                    month = 12
                    year -= 1

            elif control == "next":
                month += 1

                if month == 13:
                    month = 1

                    year += 1

            print(month)

        except:
                pass

        week_day = datetime.date(year, month, 1).weekday()

        day = 1

        month_31 = [1, 3, 5, 7, 8, 10, 12]

        months = ["Enero", "Febrero", "Marzo",
                  "Abril", "Mayo", "Junio",
                  "Julio", "Agosto", "Septiembre",
                  "Octubre", "Noviembre", "Diciembre"]

        month_name = months[month - 1]

        events = json.load(open("calendar.json", "r"))

        print("---------------------")

        print(day, week_day)

        if day < week_day:
            day += 7

        print(day, week_day)

        week_day += 2

        days_blank = week_day

        print(days_blank)

        self.render("calendar.html", datetime=now, month_31=month_31, events=events, days_blank=days_blank, month_name=month_name, year=year, month=month)
