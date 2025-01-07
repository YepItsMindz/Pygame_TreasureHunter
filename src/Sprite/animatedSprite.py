from setUp.settings import *
from Sprite.sprites import Sprite


class AnimatedSprite(Sprite):
    def __init__(self, pos, frames, groups, z=Z_LAYER['main'], animation_speed=ANIMATION_SPEED):
        self.frames, self.frame_index = frames, 0

        super().__init__(pos, self.frames[self.frame_index], groups, z)

        self.animation_speed = animation_speed

    def animate(self, dt):
        self.frame_index += self.animation_speed * dt
        self.image = self.frames[int(self.frame_index % len(self.frames))]

    def update(self, dt):
        self.animate(dt)

