from map.menu import Menu, aboutMenu, tutorialMenu
from setUp.settings import *
class show():
    def showMenuAction(self):
        self.menu = Menu()
        self.menu.run()
        
        if self.menu.selected_action == "Quit":
            pygame.quit()
            sys.exit()
        elif self.menu.selected_action == "About":
            about_menu = aboutMenu()
            about_menu.run()
            if about_menu.back:
                self.showMenuAction()
        elif self.menu.selected_action == "Tutorial":
            tutorial_menu = tutorialMenu()
            tutorial_menu.run()
            if tutorial_menu.back:
                self.showMenuAction()
    def get_overworld(self):
        return True if self.menu.selected_action == "Play" else False
        