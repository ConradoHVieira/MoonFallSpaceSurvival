import pygame.image
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from Const import WIN_WIDTH, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW


class Menu:
    def __init__(self, window):
        # Load the menu background
        self.window = window
        self.surf = pygame.image.load("assets/MenuBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        # Start with the first menu option selected
        menu_option = 0

        # Start the menu background music
        pygame.mixer_music.load("assets/Menu.mp3")
        pygame.mixer_music.play(-1)

        while True:

            # Draw the background and menu titles
            self.window.blit(source=self.surf, dest=self.rect)

            self.menu_text(
                text_size=75,
                text="MoonFall",
                text_color=C_ORANGE,
                text_center_pos=((WIN_WIDTH / 2), 70)
            )

            self.menu_text(
                text_size=75,
                text="SpaceSurvival",
                text_color=C_ORANGE,
                text_center_pos=((WIN_WIDTH / 2), 120)
            )

            # Draw the menu options and highlight the selected one
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(
                        text_size=35,
                        text=MENU_OPTION[i],
                        text_color=C_YELLOW,
                        text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i)
                    )
                else:
                    self.menu_text(
                        text_size=35,
                        text=MENU_OPTION[i],
                        text_color=C_WHITE,
                        text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i)
                    )

            pygame.display.flip()

            # Process keyboard input
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    # Move the selection down
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    # Move the selection up
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    # Confirm the selected option
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    # Render centered text on the menu
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Roboto", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)