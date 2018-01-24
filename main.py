import os

import tornado.ioloop
import tornado.web

import hue
import web

import web_calendar as calendar
import add_to_calendar as calendar_add

import inventory
import inventory_view
import inventory_list
import inventory_modify

class NotFoundHandler(tornado.web.RequestHandler):
    def prepare(self):
        self.render("error.html")


class Application(tornado.web.Application):
    def __init__(self):
        base_dir = os.path.dirname(__file__)
        settings = {
            "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
            'template_path': os.path.join(base_dir, "templates"),
            'static_path': os.path.join(base_dir, "static"),
            'debug': True,
            "xsrf_cookies": False,
        }

        tornado.web.Application.__init__(self, [
            tornado.web.url(r"/", web.MainWeb),

            tornado.web.url(r"/hue", hue.MainHandler),

            tornado.web.url(r"/inventory", inventory.MainHandler),
            tornado.web.url(r"/inventory/view", inventory_view.MainHandler),
            tornado.web.url(r"/inventory/list", inventory_list.MainHandler),
            tornado.web.url(r"/inventory/modify", inventory_modify.MainHandler),

            tornado.web.url(r"/calendar", calendar.MainHandler),
            tornado.web.url(r"/calendar/add", calendar_add.MainHandler),
        ], default_handler_class=NotFoundHandler, **settings)


if __name__ == "__main__":
    global V
    V = 0

    Application().listen(8888)
    tornado.ioloop.IOLoop.instance().start()