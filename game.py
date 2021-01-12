import json
import pygame

file = open("objects.json", "r")

stuff = json.load(file)

file.close()

print (stuff)