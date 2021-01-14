import save
import classes

objects, data = save.load()

objs = []
def new_obj(im, name="", pos=classes.Vector2()):
    obj = classes.Object(png=im, name=name, pos=pos)
    objs.append(obj)#{"obj": obj, "name": name, "on": True})

#new_obj(objs, save.get_image(object["cd"]), name="cd")

def get_objs():
    return objs

def get_id_by_name(name):
    res = None
    for ob in range(len(objs)):
        if objs[ob]["name"]==name:
            res = ob
            break
    return res

def get_name_by_id(i):
    res = None
    try:
        res = objs[i]["name"]
    except:
        pass
    return res

def set_on(i, val):
    objs[i]["on"]==val

def set_image(i, im):
    objs[i]["obj"].image = im

"""
this is where the objects list is kept

any functions related to the object list goes here
"""