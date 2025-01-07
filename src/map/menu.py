from setUp.settings import *
from os.path import join
import pygame
import sys

pygame.init()
# from game import Game
class Menu:
    def __init__(self):
        # Tạo màn hình hiển thị
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Treasure Hunter")
        pygame.display.set_icon(pygame.image.load(join('..', 'graphics', 'ui', 'logo.png')))
        
        # Font và nút
        self.font = pygame.font.Font(join('..', 'graphics', 'ui', 'runescape_uf.ttf'), 50)
        self.buttons = [
            {'text': 'Play', 'rect': pygame.Rect(0, 0, 200, 50), 'clicked': False},  # Thêm trạng thái clicked
            {'text': 'Tutorial', 'rect': pygame.Rect(0, 0, 200, 50), 'clicked': False},
            {'text': 'About', 'rect': pygame.Rect(0, 0, 200, 50), 'clicked': False},
            {'text': 'Quit', 'rect': pygame.Rect(0, 0, 200, 50), 'clicked': False},
        ]
        self.bg_color = (0, 0, 0)
        self.text_color = (51, 50, 61)
        self.text_color_on_click = (255, 0, 0)  # Màu sắc thay đổi khi nút được nhấn
        self.border_color = (0, 255, 0)  # Màu viền khi bấm (màu xanh lá)
        self.border_width = 5  # Độ dày viền khi bấm
        self.running = True
        self.selected_action = None

        # Load background image
        path = join('..', 'graphics', 'ui', 'bgmain.png')
        self.bg = pygame.image.load(path)
        self.bg = pygame.transform.scale(self.bg, (WINDOW_WIDTH, WINDOW_HEIGHT))

        # Vị trí các nút
        self.pos = [[645, 285], [645, 387], [645, 490], [645, 593]]

       
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




class aboutMenu:
    def __init__(self):
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.font = pygame.font.Font(join('..', 'graphics', 'ui', 'runescape_uf.ttf'), 50)
        self.bg_color = (0, 0, 0)
        self.text_color = (51, 50, 61)
        self.running = True
        self.back = False
        
        self.back_button = pygame.Rect(WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 + 150, 200, 50)
        self.highlight_color = (100, 100, 100)

        path = join('..', 'graphics', 'ui', 'bgfeature.png')
        self.bg = pygame.image.load(path)
        self.bg = pygame.transform.scale(self.bg, (WINDOW_WIDTH, WINDOW_HEIGHT))
        

    def draw_text(self):
        
        text = "Nguyen Duong Thu - B22DCCN839\nNguyen Viet Tu - B22DCCN748 \nTran Trong Thai - B22DCCN784 \nNguyen Trung Hieu - B22DCCN316 \nDang Quan Bao - B22DCCN060 "
        text_surface = self.font.render(text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(645, 380))
        self.display_surface.blit(text_surface, text_rect)

        
        back_text_surface = self.font.render("Back", True, self.text_color)
        back_text_rect = back_text_surface.get_rect(center=(645, 670))
        self.back_button = pygame.Rect(back_text_rect.x - 10, back_text_rect.y - 10, back_text_rect.width + 20, back_text_rect.height + 20)
        button_color = (51, 50, 61)  
        pygame.draw.rect(self.display_surface, button_color, self.back_button, border_radius=10)
        back_text_surface = self.font.render("Back", True, (255, 255, 255))
        back_text_rect = back_text_surface.get_rect(center=self.back_button.center)
        self.display_surface.blit(back_text_surface, back_text_rect)



    def run(self):
        while self.running:
            self.display_surface.blit(self.bg, (0, 0))
            self.draw_text()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_button.collidepoint(event.pos):  # Nhấn vào nút "Back"
                        self.running = False
                        self.back = True
                        
                        
class tutorialMenu:
    def __init__(self):
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.font = pygame.font.Font(join('..', 'graphics', 'ui', 'runescape_uf.ttf'), 50)
        self.bg_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.running = True
        self.back = False

        back_text_surface = self.font.render("Back", True, self.text_color)
        back_text_rect = back_text_surface.get_rect(center=(645, 670))
        self.back_button = pygame.Rect(back_text_rect.x - 10, back_text_rect.y - 10, back_text_rect.width + 20, back_text_rect.height + 20)
        button_color = (51, 50, 61)  
        pygame.draw.rect(self.display_surface, button_color, self.back_button, border_radius=10)
        back_text_surface = self.font.render("Back", True, (255, 255, 255))
        back_text_rect = back_text_surface.get_rect(center=self.back_button.center)
        self.display_surface.blit(back_text_surface, back_text_rect)
        
        # Load background image
        path = join('..', 'graphics', 'ui', 'tutorial.png')
        self.bg = pygame.image.load(path)
        self.bg = pygame.transform.scale(self.bg, (WINDOW_WIDTH, WINDOW_HEIGHT))
        

        

    def draw_text(self):
        back_text_surface = self.font.render("Back", True, self.text_color)
        back_text_rect = back_text_surface.get_rect(center=(645, 670))
        self.back_button = pygame.Rect(back_text_rect.x - 10, back_text_rect.y - 10, back_text_rect.width + 20, back_text_rect.height + 20)
        button_color = (51, 50, 61)  
        pygame.draw.rect(self.display_surface, button_color, self.back_button, border_radius=10)
        back_text_surface = self.font.render("Back", True, (255, 255, 255))
        back_text_rect = back_text_surface.get_rect(center=self.back_button.center)
        self.display_surface.blit(back_text_surface, back_text_rect)

    def run(self):
        while self.running:
            self.display_surface.blit(self.bg, (0, 0))
            self.draw_text()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_button.collidepoint(event.pos):  # Nhấn vào nút "Back"
                        self.running = False
                        self.back = True


                        
        
                        
