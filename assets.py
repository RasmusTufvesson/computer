import save
import object_handeler as obj_hand
import classes
from collections import namedtuple

objects, data = save.load()

## images
cd_im = save.get_image(objects["cd"])

## objects
obj_hand.new_obj(cd_im, "cd", classes.Vector2(400, 300))

## colors
_colors = objects["colors"]
colors = namedtuple('Colors', _colors.keys())(*_colors.values())