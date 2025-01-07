from random import randint

from Sprite.animatedSprite import AnimatedSprite
from setUp.settings import *
from setUp.timer import Timer
from ui.heart import Heart


class UI:
    def __init__(self, font, frames):
        self.display_surface = pygame.display.get_surface()
        self.sprites = pygame.sprite.Group()
        self.font = font

        # health / hearts
        self.heart_frames = frames['heart']
        self.heart_surf_width = self.heart_frames[0].get_width()
        self.heart_padding = 6

        # coins
        self.coin_amount = 0
        self.coin_timer = Timer(1000)
        self.coin_surf = frames['coin']

    def create_hearts(self, amount):
        for sprite in self.sprites:
            sprite.kill()
        for heart in range(amount):
            x = 10 + heart * (self.heart_surf_width + self.heart_padding)
            y = 10
            Heart((x, y), self.heart_frames, self.sprites)

    def display_text(self):
     
        text_surf = self.font.render(str(self.coin_amount), False, '#33323d')
        text_rect = text_surf.get_frect(topleft=(16, 40))
        self.display_surface.blit(text_surf, text_rect)
        coin_rect = self.coin_surf.get_frect(center=text_rect.bottomright).move(0, -6)
        self.display_surface.blit(self.coin_surf, coin_rect)

    def show_coins(self, amount):
        self.coin_amount = amount

    def update(self, dt):
        self.coin_timer.update()
        self.sprites.update(dt)
        self.sprites.draw(self.display_surface)
        self.display_text()



