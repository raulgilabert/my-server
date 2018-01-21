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
        self.inventory = json.load(open("inventory.json", "r"))

        self.render("inventory_modify.html", inventory=self.inventory)

    def post(self):
        self.inventory = json.load(open("inventory.json", "r"))

        name = self.get_argument("element", True)

        quantity = self.get_argument("quantity", True)

        quantity = int(quantity)

        found = False

        for category in self.inventory:
            for element in self.inventory[category]:
                if element == name:
                    found = True

                    self.inventory[category][element] = self.inventory[category][element] + quantity

        if not found:
            self.inventory.append({"name": name, "quantity": quantity})

        json.dump(self.inventory, open("inventory.json", "w"), indent=4, sort_keys=True)

        self.redirect_to_main()
