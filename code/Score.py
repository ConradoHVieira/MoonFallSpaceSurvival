import sys
import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from Const import C_YELLOW, C_WHITE, C_RED, SCORE_POS


class Score:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load("assets/ScoreBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def show(self, victory: bool):

        if victory:
            title = "YOU WIN!"
            color = C_YELLOW
            music = "Score_Victory.mp3"
        else:
            title = "GAME OVER"
            color = C_RED
            music = "Score_Loss.mp3"

        pygame.mixer_music.load(f"assets/{music}")
        pygame.mixer_music.play(-1)

        while True:
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

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return

            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Roboto", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)

        self.window.blit(text_surf, text_rect)
