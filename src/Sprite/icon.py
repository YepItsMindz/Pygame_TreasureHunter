from setUp.settings import *


class Icon(pygame.sprite.Sprite):
    def __init__(self, pos, groups, frames):
        super().__init__(groups)
        self.icon = True
        self.path = None
        self.direction = vector()
        self.speed = 400

        # image
        self.frames, self.frame_index = frames, 0
        self.state = 'idle'
        self.image = self.frames[self.state][self.frame_index]
        self.z = Z_LAYER['main']

        # rect
        self.rect = self.image.get_rect(center=pos)

    def start_move(self, path):
        self.rect.center = path[0]
        self.path = path[1:]
        self.find_path()

    def find_path(self):
        if self.path:
            if self.rect.centerx == self.path[0][0]:  # vertical
                self.direction = vector(0, 1 if self.path[0][1] > self.rect.centery else - 1)
            else:  # horizontal
                self.direction = vector(1 if self.path[0][0] > self.rect.centerx else - 1, 0)
        else:
            self.direction = vector()

    def point_collision(self):
        if self.direction.y == 1 and self.rect.centery >= self.path[0][1] or \
                self.direction.y == -1 and self.rect.centery <= self.path[0][1]:
            self.rect.centery = self.path[0][1]
            del self.path[0]
            self.find_path()

        if self.direction.x == 1 and self.rect.centerx >= self.path[0][0] or \
                self.direction.x == -1 and self.rect.centerx <= self.path[0][0]:
            self.rect.centerx = self.path[0][0]
            del self.path[0]
            self.find_path()

    def animate(self, dt):
        self.frame_index += ANIMATION_SPEED * dt
        self.image = self.frames[self.state][int(self.frame_index % len(self.frames[self.state]))]

    def get_state(self):
        self.state = 'idle'
        if self.direction == vector(1, 0):  self.state = 'right'
        if self.direction == vector(-1, 0): self.state = 'left'
        if self.direction == vector(0, 1):  self.state = 'down'
        if self.direction == vector(0, -1): self.state = 'up'

    def update(self, dt):
        if self.path:
            self.point_collision()
            self.rect.center += self.direction * self.speed * dt
        self.get_state()
        self.animate(dt)
