import json
from zipfile import ZipFile
from sys import exit


class File:
    def __init__(self, name, cont, type):
        self.raw_name = name
        self.cont = cont
        self.type = type

        self.name = name + "." + type

file = open("test/game.caen", "wb")
test = {"owo":"print"}

cont = [json.dumps(test).encode(), open("test_game/clicker.png", "rb").read()]

def main(cont):
    for i in cont:
        file.write("--FILE SEPERATOR--\n".encode())
        file.write(i)
        file.write("\n".encode())


def main2(cont):
    tzip = ZipFile("test.caen", "w")
    for i in cont:
        temp = open(i.name, "wb")
        temp.write(i.cont)
        temp.close()
        tzip.write(i.name)


main(cont)
main2([File("testjson", cont[0], "json"), File("testpng", cont[1], "png")])
file.close()