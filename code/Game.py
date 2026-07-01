from code.Level import Level
from Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
import pygame
import pygame.mixer_music
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:

                level = Level(self.window, "Level1", menu_return)
                result = level.run()

                Score(self.window).show(result)

            elif menu_return == MENU_OPTION[1]:
                pygame.quit()
                quit()
