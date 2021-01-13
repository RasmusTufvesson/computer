import save
import pygame

objects, data = save.load()
cds = data["player"]["cds"]
inv = data["player"]["inv"]
money = data["player"]["money"]

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

save.save(data)
pygame.quit()