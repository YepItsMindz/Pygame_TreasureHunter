from setUp.settings import *
from Sprite.sprites import Sprite
from random import randint as ranint


class Cloud(Sprite):
    def __init__(self, pos, surf, groups, z=Z_LAYER['clouds']):
        super().__init__(pos, surf, groups, z)
        self.speed = ranint(50, 120)
        self.direction = -1
        self.rect.midbottom = pos

    def update(self, dt):
        self.rect.x += self.speed * dt * self.direction
        if self.rect.right <= 0:
            self.kill()
