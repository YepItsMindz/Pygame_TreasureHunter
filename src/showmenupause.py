from posixpath import join
from setUp.settings import *
from showmenu import show
import pygame
import sys
import os

class showMenuPause:
    def __init__(self):
        self.showMenuBack = show()
        self.display_surface = pygame.display.get_surface()
        self.paused = False
        self.overworldback = False

    def show_pause_menu(self):
        # Load the background image
        background_path = join('..', 'graphics', 'ui', 'Paused-Screen.png')
        background_image = pygame.image.load(background_path).convert()

        # Draw the background image onto the display surface
        self.display_surface.blit(background_image, (0, 0))

        # Create menu text using Pygame font rendering
        font = pygame.font.Font(join('..', 'graphics', 'ui', 'runescape_uf.ttf'), 22)
        color = (51,50,61)
        # Use a font (None means the default)
        resume_text = font.render('Press R to resume', True, color = color)
        quit_text = font.render('Press O to go to overworld', True, color = color)
        overworld_text = font.render('Press Q to quit', True, color = color)

        # Positions for the text
        resume_rect = resume_text.get_rect(center = (640, 324))
        quit_rect = quit_text.get_rect(center = (640, 390))
        overworld_rect = overworld_text.get_rect(center = (640, 455))

        # Draw the menu text on top of the background
        self.display_surface.blit(resume_text, resume_rect)
        self.display_surface.blit(quit_text, quit_rect)
        self.display_surface.blit(overworld_text, overworld_rect)

        pygame.display.update()

    # Menu event loop
        while self.paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.resume_game()
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_o:
                        self.overworldback = True
                        self.paused = False


    def get_overworldback(self):
        return self.overworldback

    def resume_game(self):
        # Resume the game and go back to the current level
        self.paused = False
        # dont change anything here

    def get_pause(self):
        return self.paused

    def pause_game(self):
        self.paused = True
        self.show_pause_menu()