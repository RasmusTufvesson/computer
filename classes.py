class Vector2:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def get(self):
        return self.x, self.y
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Vector2(self.x * other.x, self.y * other.y)
    def __truediv__(self, other):
        return Vector2(self.x / other.x, self.y / other.y)
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)
    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)
    def __ne__(self, other):
        return not self.__eq__(other)
    def __iadd__(self, other):
        self = Vector2(self.x + other.x, self.y + other.y)
    def __isub__(self, other):
        self = Vector2(self.x - other.x, self.y - other.y)
    def __imul__(self, other):
        self = Vector2(self.x * other.x, self.y * other.y)
    def __itruediv__(self, other):
        self = Vector2(self.x / other.x, self.y / other.y)

class Object:
    def __init__(self, png, name="", pos=Vector2(), on=True):
        self.image = png
        self.pos = pos
        self.name = name
        self.on = on
    def move(self, vector):
        self.pos += vector
    def get_box(self):
        box = self.image.get_rect()
        box.center = self.pos.get()#(self.pos.get()[0]-box.width/2, self.pos.get()[1]-box.height/2)
        return box