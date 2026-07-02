import sys
import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from Const import C_YELLOW, C_WHITE, C_RED, SCORE_POS


class Score:

    def __init__(self, window: Surface):
        # Load the background image for the result screen
        self.window = window
        self.surf = pygame.image.load("assets/ScoreBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def show(self, victory: bool):

        # Configure the screen according to the game result
        if victory:
            title = "YOU WIN!"
            color = C_YELLOW
            music = "Score_Victory.mp3"
        else:
            title = "GAME OVER"
            color = C_RED
            music = "Score_Loss.mp3"

        # Play the corresponding background music
        pygame.mixer_music.load(f"assets/{music}")
        pygame.mixer_music.play(-1)

        while True:

            # Draw the background and result messages
            self.window.blit(self.surf, self.rect)

            self.score_text(
                48,
                title,
                color,
                SCORE_POS["Title"]
            )

            self.score_text(
                20,
                "Press ENTER to return",
                C_WHITE,
                SCORE_POS["Label2"]
            )

            # Handle user input
            for event in pygame.event.get():

                # Close the application
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Return to the main menu when ENTER is pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return

            # Update the display
            pygame.display.flip()

    # Render centered text on the screen
    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Roboto", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)

        self.window.blit(text_surf, text_rect)