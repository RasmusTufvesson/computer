import json

objects = json.load(open("objects.json", "r"))
data = json.load(open("savedata.json", "r"))

def save(data):
    with open("savedata.json", "w") as write:
        json.dump(data, write)

def load():
    return objects, data