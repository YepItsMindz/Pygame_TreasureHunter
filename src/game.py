from debug import debug
from setUp.settings import *
from map.level import Level
from pytmx.util_pygame import load_pygame
from os.path import join
from setUp.support import *
from map.overworld import Overworld
from data import Data
from ui.ui import UI
from map.menu import Menu, aboutMenu, tutorialMenu
from gameover import Over
from showmenu import show
from win import Win


class Game:
    def __init__(self):
        #self.switch_stage = None????
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Platformer")

        self.clock = pygame.time.Clock()
        self.import_assets()

        self.ui = UI(self.font, self.ui_frames)
        self.data = Data(self.ui)
        
        self.playAgain = False

        self.tmx_overworld = load_pygame(join('..',  'data', 'overworld', 'overworld.tmx'))
        self.tmx_maps = {
            0: load_pygame(join('..', 'data', 'levels', '0.tmx')),
            1: load_pygame(join('..',  'data', 'levels', '1.tmx')),
            2: load_pygame(join('..',  'data', 'levels', '2.tmx')),
            3: load_pygame(join('..',  'data', 'levels', '3.tmx')),
            4: load_pygame(join('..',  'data', 'levels', '4.tmx')),
            5: load_pygame(join('..',  'data', 'levels', '5.tmx')),
        }

        self.bg_music.play(-1)
        self.current_stage = None
        self.paused = False
        self.can_play = True

    def switch_stage(self, target, unlock=0, saved_pos = None):
        if target == 'level':
            self.current_stage = Level(self.tmx_maps[self.data.current_level], self.level_frames, self.audio_files,
                                       self.data, self.switch_stage, saved_pos)
        
            
            
            
        elif target == 'menu':
            self.show_menu()
        elif target == 'overworld':
            if unlock >= 0:
                self.data.unlocked_level = unlock
            else:
                self.data.health -= 1
            self.current_stage = Overworld(self.tmx_overworld, self.data, self.overworld_frames, self.switch_stage)
        else:
            pygame.quit()
            sys.exit()

    def import_assets(self):
        self.level_frames = {
            'flag': import_folder( '..', 'graphics', 'level', 'flag'),
            'palms': import_sub_folders ('..', 'graphics', 'level', 'palms'),
            'candle': import_folder( '..', 'graphics', 'level', 'candle'),
            'window': import_folder( '..', 'graphics', 'level', 'window'),
            'small_chain': import_folder ('..', 'graphics', 'level', 'small_chains'),
            'big_chain': import_folder( '..', 'graphics', 'level', 'big_chains'),
            'candle_light': import_folder( '..', 'graphics', 'level', 'candle light'),
            'helicopter': import_folder( '..', 'graphics', 'level', 'helicopter'),
            'water_top': import_folder( '..', 'graphics', 'level', 'water', 'top'),
            'water_body': import_image ('..', 'graphics', 'level', 'water', 'body'),
            'bg_tiles': import_folder_dict( '..', 'graphics', 'level', 'bg', 'tiles'),
            'cloud_small': import_folder( '..', 'graphics', 'level', 'clouds', 'small'),
            'cloud_large': import_image( '..', 'graphics', 'level', 'clouds', 'large_cloud'),
            'saw': import_folder( '..', 'graphics', 'enemies', 'saw', 'animation'),
            'floor_spike': import_folder( '..', 'graphics', 'enemies', 'floor_spikes'),
            'player': import_sub_folders( '..', 'graphics', 'player'),
            'saw_chain': import_image( '..', 'graphics', 'enemies', 'saw', 'saw_chain'),
            'boat': import_folder( '..', 'graphics', 'objects', 'boat'),
            'spike': import_image( '..', 'graphics', 'enemies', 'spike_ball', 'Spiked Ball'),
            'spike_chain': import_image( '..', 'graphics', 'enemies', 'spike_ball', 'spiked_chain'),
            'tooth': import_folder( '..', 'graphics', 'enemies', 'tooth', 'run'),
            'shell': import_sub_folders( '..', 'graphics', 'enemies', 'shell'),
            'pearl': import_image( '..', 'graphics', 'enemies', 'bullets', 'pearl'),
            'items': import_sub_folders( '..', 'graphics', 'items'),
            'particle': import_folder ( '..', 'graphics', 'effects', 'particle'),
        }

        self.font = pygame.font.Font(join('..',  'graphics', 'ui', 'runescape_uf.ttf'), 40)
        self.ui_frames = {
            'heart': import_folder( '..', 'graphics', 'ui', 'heart'),
            'coin': import_image( '..', 'graphics', 'ui', 'coin')
        }

        self.overworld_frames = {
            'palms': import_folder( '..', 'graphics', 'overworld', 'palm'),
            'water': import_folder( '..', 'graphics', 'overworld', 'water'),
            'path': import_folder_dict( '..', 'graphics', 'overworld', 'path'),
            'icon': import_sub_folders( '..', 'graphics', 'overworld', 'icon'),
        }

        self.audio_files = {
            'coin': pygame.mixer.Sound(join('..', 'audio', 'coin.wav')),
            'attack': pygame.mixer.Sound(join( '..', 'audio', 'attack.wav')),
            'jump': pygame.mixer.Sound(join('..',  'audio', 'jump.wav')),
            'damage': pygame.mixer.Sound(join('..',  'audio', 'damage.wav')),
            'pearl': pygame.mixer.Sound(join ('..', 'audio', 'pearl.wav')),
        }
        self.bg_music = pygame.mixer.Sound(join( '..', 'audio', 'starlight_city.mp3'))
        self.bg_music.set_volume(0.5)

    def check_game_over(self):
        game_over = Over()
        if self.data.health <= 0:
            self.can_play = False
            
    def gameOver(self):
        game_over = Over()
        game_over.run()
        if game_over.selected_action == "Play Again":
            self.data.health = 5
            level_unlocked = self.data.current_level
            self.switch_stage("overworld", level_unlocked)
        elif game_over.selected_action == "Quit":
            pygame.quit()
            
    def check_win(self):
        if all(self.data.level_finished):
            return True
    
    
    def win(self):
        win = Win()
        win.run()
        if win.selected_action == "Play Again":
            self.playAgain = True
        elif win.selected_action == "Quit":
            pygame.quit()
    

    def run(self):
        showMenu = show()
        showMenu.showMenuAction()
        if showMenu.get_overworld():
            self.switch_stage('overworld')
        while True:
            dt = self.clock.tick() / 1000  # Đảm bảo FPS không quá nhanh (60 FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            if self.data.health <= 0: 
                self.gameOver()
            
            if self.check_win():
                self.win()
                if self.playAgain:
                    showMenu.showMenuAction()
                    for i in range(6):
                        self.data.level_finished[i] = False
            self.current_stage.run(dt)  # Chạy màn chơi hiện tại
            self.ui.update(dt)  # Cập nhật UI
            pygame.display.update()  # Cập nhật màn hình
    



