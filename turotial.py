import json

file = open("objects.json", "r")

stuff = json.load(file)

file.close()

print (stuff)

sting = "hej\njag är cool\nokay"

print (sting.split('\n'))