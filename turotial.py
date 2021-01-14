import json

file = open("objects.json", "r")

stuff = json.load(file)

file.close()

print (stuff)

sting = "hej\njag är cool\nokay"

print (sting.split('\n'))

"""
a place i put stuff so that viggo can look at how you do it
"""