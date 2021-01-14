import save
import pygame
import classes
import object_handeler as obj_hand
import assets

objects, data = save.load()
cds = data["player"]["cds"]
inv = data["player"]["inv"]
money = data["player"]["money"]

##pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(objects["name"])
pygame.display.set_icon(save.get_image(objects["icon"]))
clock = pygame.time.Clock()

pygame.mixer.music.load(objects["music"])
pygame.mixer.music.play(-1)

running = True
timer = 60
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
    
    screen.fill(assets.colors.white)

    for ob in obj_hand.get_objs():
        #print (ob.on)
        if ob.on:
            screen.blit(ob.image, ob.get_box())

    if timer != 0:
        timer -= 1
    else:
        timer = 60
        obj_hand.objs[0].on = not obj_hand.objs[0].on
        #print ("change")
        #print (obj_hand.objs[0].on)
    pygame.display.update()
    clock.tick(30)

save.save(data)
pygame.quit()

"""
this is where the mainloop is

any mainloop logic is here
"""