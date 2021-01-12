import json
import pygame

objects = json.load(open("objects.json", "r"))
data = json.load(open("savedata.json", "r"))

def save(data):
    with open("savedata.json", "w") as write:
        json.dump(data, write)

##pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(objects["game"]["name"])
clock = pygame.time.Clock()

pygame.mixer.music.load(objects["game"]["music"])
pygame.mixer.music.play(-1)

running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
    
    #print ('hello')

    pygame.display.update()
    clock.tick(30)

save(data)
pygame.quit()