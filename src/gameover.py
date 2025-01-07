from setUp.settings import *
from os.path import join
import pygame
import sys 

class Over: 
    def __init__(self):
        # Tạo màn hình hiển thị
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Main Menu")
        
        # Font và nút
        self.font = pygame.font.Font(join('..', 'graphics', 'ui', 'runescape_uf.ttf'), 50)
        self.buttons = [
            {'text': 'Play Again', 'rect': pygame.Rect(0, 0, 200, 50), 'clicked': False},
            {'text': 'Quit', 'rect': pygame.Rect(0, 0, 200, 50), 'clicked': False},
        ]
        self.bg_color = (0, 0, 0)
        self.text_color = (51, 50, 61)
        self.text_color_on_click = (255, 0, 0)  # Màu sắc thay đổi khi nút được nhấn
        self.border_color = (0, 255, 0)  # Màu viền khi bấm (màu xanh lá)
        self.border_width = 5  # Độ dày viền khi bấm
        self.running = True
        self.selected_action = None
        self.play = True

        # Load background image
        path = join('..', 'graphics', 'ui', 'gameover.png')
        self.bg = pygame.image.load(path)
        self.bg = pygame.transform.scale(self.bg, (WINDOW_WIDTH, WINDOW_HEIGHT))

        # Vị trí các nút
        self.pos = [[640, 500], [640, 605]]

       
        for i, button in enumerate(self.buttons):
            button['rect'].center = self.pos[i] 
    
    def draw_buttons(self):
        for button in self.buttons:
            
            text_color = self.text_color_on_click if button['clicked'] else self.text_color
        
            text_surface = self.font.render(button['text'], True, text_color)
            text_rect = text_surface.get_rect(center=button['rect'].center)
            self.display_surface.blit(text_surface, text_rect)

            if button['clicked']:
                pygame.draw.rect(self.display_surface, self.border_color, button['rect'], self.border_width)

    def run(self):
        while self.running:
            # Vẽ nền
            self.display_surface.blit(self.bg, (0, 0))
            self.draw_buttons()  
            pygame.display.update()

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        if button['rect'].collidepoint(event.pos):
                            button['clicked'] = True  
                            self.selected_action = button['text']
                            self.running = False
                            break

                if event.type == pygame.MOUSEBUTTONUP:
                    for button in self.buttons:
                        button['clicked'] = False 
                        
