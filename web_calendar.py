import tornado.web
import tornado.escape
import socket
import urllib.parse as parse

import json

import datetime


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        now = datetime.datetime.now()

        week_day = datetime.datetime.today().weekday()

        month_31 = [1, 3, 5, 7, 8, 10, 12]

        months = ["Enero", "Febrero", "Marzo",
                  "Abril", "Mayo", "Junio",
                  "Julio", "Agosto", "Septiembre",
                  "Octubre", "Noviembre", "Diciembre"]

        month = months[now.month - 1]

        events = json.load(open("calendar.json", "r"))

        days_blank = int((((now.day - week_day) / 7) - int((now.day - week_day) / 7))*7)

        self.render("calendar.html", datetime=now, month_31=month_31, events=events, days_blank=days_blank, month=month, year=now.year)
