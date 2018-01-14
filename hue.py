import tornado.web
import tornado.escape
import socket
from urllib import parse

import phue


class MainHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

    def get(self):
        bridge = phue.Bridge(ip="192.168.1.56")

        bridge.connect()

        hostname = parse.urlparse("%s://%s" % (self.request.protocol, self.request.host)).hostname
        host_ip = socket.gethostbyname(hostname)
        client_ip = self.request.remote_ip

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

        if host_ip != client_ip or not isinstance(function, str):
            self.redirect("/login")
        else:
            self.write("""
            <!DOCTYPE html>
            <html lang="es-es">
            <head>
            <meta charset="UTF-8">
            <title>Light controller</title>

            <style>
                    """)

            with open('static/css/main.css', 'r') as myfile:
                data = myfile.read().replace('\n', '')

                self.write(data)

            self.write("""
            </style>
            </head>
            <body>
            """)

            global V

            V += 1

            self.write('<p style="text-align: right">Hello. Page viewed %d times.</p>' % (V,))

            self.write("<table>")

            num = 0

            for group in bridge.groups:
                num += 1

                if group.name != "Everything":
                    self.write("<tr>")

                    if group.on:
                        self.write('<td class="nameGroup">' + group.name + "</td>")

                        self.write('<td><img src="on.jpg" id="' + group.name +
                                   '" height="32" onclick="apagar(this.id)"></img></td>')

                    else:
                        self.write('<td class="nameGroup">' + group.name + "</td>")

                        self.write('<td><img src="off.jpg" id="' + group.name +
                                   '" height="32" onclick="encender(this.id)"></img></td>')

                    self.write('<td><button type="button" id="' + group.name +
                               '" onclick="encender(this.id)">On</button></td>')

                    self.write('<td><button type="button" id="' + group.name +
                               '" onclick="apagar(this.id)">Off</button></td>')

                    self.write('<td><input type="range" min="1" max="255" value="' +
                               str(group.brightness) + '" ' + 'class="slider" id="' +
                               group.name + '" oninput="update_label(this.value, this.id)"' +
                               ' onchange="brightness(this.value, this.id)"></td>')

                    self.write('<td><p id="label_' + group.name + '"></p></td>')

                    self.write("</tr>")

                if num == 2:
                    num = 0

            self.write("</table>")

            self.write("<script>")

            with open('static/js/controller.js', 'r') as myfile:
                data = myfile.read().replace('\n', '')

                self.write(data)

            self.write("""
            </script>
            </body>
            </html>
            """)

class PasswordHandler(tornado.web.RequestHandler):
    def get(self):
        hostname = parse.urlparse("%s://%s" % (self.request.protocol, self.request.host)).hostname
        host_ip = socket.gethostbyname(hostname)
        client_ip = self.request.remote_ip

        self.write(host_ip + " // " + client_ip)
