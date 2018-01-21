import tornado.web
import tornado.escape
import socket
import urllib.parse as parse

import json
import pprint


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        inventory = json.load(open("inventory.json", "r"))
        minimum = json.load(open("minimum.json", "r"))

        dict = {}

        for category in inventory:
            dict[category] = {}

            for min in minimum[category]:
                found = False

                for element in inventory[category]:
                    if element == min:
                        found = True

                        if inventory[category][element] < minimum[category][min]:
                            dict[category][element] = minimum[category][min] - inventory[category][element]

                if not found:
                    dict[category][min] = minimum[category][min]

        pprint.pprint(dict)

        self.render("inventory_list.html", inventory=inventory, list=dict)
