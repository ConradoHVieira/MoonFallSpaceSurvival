from code.Level import Level
from Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
import pygame
import pygame.mixer_music
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):
        # Initialize Pygame and create the game window
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        # Main application loop
        while True:

            # Display the menu and wait for the player's choice
            menu = Menu(self.window)
            menu_return = menu.run()

            # Start Survival mode
            if menu_return == MENU_OPTION[0]:

                level = Level(self.window, "Level1", menu_return)
                result = level.run()

                # Display the victory or defeat screen
                Score(self.window).show(result)

            # Exit the game
            elif menu_return == MENU_OPTION[1]:
                pygame.quit()
                quit()