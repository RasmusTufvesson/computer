import save
import pygame
import classes
import object_handeler as obj_hand

objects, data = save.load()
cds = data["player"]["cds"]
inv = data["player"]["inv"]
money = data["player"]["money"]

## images
cd_im = save.get_image(objects["cd"])

## objects
obj_hand.new_obj(cd_im, "cd", classes.Vector2(400, 300))

##pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(objects["name"])
pygame.display.set_icon(save.get_image(objects["icon"]))
clock = pygame.time.Clock()

pygame.mixer.music.load(objects["music"])
pygame.mixer.music.play(-1)

running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
    
    for ob in obj_hand.get_objs():
        screen.blit(ob["obj"].image, ob["obj"].get_box())

    pygame.display.update()
    clock.tick(30)

save.save(data)
pygame.quit()