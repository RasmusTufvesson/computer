import json
from pygame import image

objects = json.load(open("objects.json", "r"))
data = json.load(open("savedata.json", "r"))

def save(data):
    with open("savedata.json", "w") as write:
        json.dump(data, write)

def load():
    return objects, data

def get_image(path):
    return image.load(path)

"""
this is where saving and loading functions are

any save load related functions go here
"""