import json
from zipfile import ZipFile
from sys import exit


class File:
    def __init__(self, name, cont, type):
        self.raw_name = name
        self.cont = cont
        self.type = type

        self.name = name + "." + type

test = {"owo":"print"}

cont = [File("testjson", json.dumps(test).encode(), "json"), File("testpng", open("test_game/clicker.png", "rb").read(), "png")]

def main(cont):
    tzip = ZipFile("test/game.caen", "w")
    for i in cont:
        temp = open(i.name, "wb")
        temp.write(i.cont)
        temp.close()
        tzip.write(i.name)


main(cont)