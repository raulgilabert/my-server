import os

import hue
import web
import tornado.ioloop
import tornado.web


class Application(tornado.web.Application):
    def __init__(self):
        base_dir = os.path.dirname(__file__)
        settings = {
            "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
            "login_url": "/login",
            'template_path': os.path.join(base_dir, "templates"),
            'static_path': os.path.join(base_dir, "static"),
            'debug': True,
            "xsrf_cookies": True,
        }

        tornado.web.Application.__init__(self, [
            tornado.web.url(r"/", web.MainWeb),
            tornado.web.url(r"/hue", hue.MainHandler),
            (r"/(off.jpg)", tornado.web.StaticFileHandler, {'path': 'static/images/'}),
            (r"/(on.jpg)", tornado.web.StaticFileHandler, {'path': 'static/images/'}),
            (r"/(level_4.json)", tornado.web.StaticFileHandler, {'path': 'static/json/'}),
        ], **settings)


if __name__ == "__main__":
    global V
    V = 0

    Application().listen(8888)
    tornado.ioloop.IOLoop.instance().start()