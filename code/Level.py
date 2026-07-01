import sys
import random

import pygame.display
import pygame.time
from pygame.rect import Rect
from pygame.surface import Surface
from pygame.font import Font

from Const import WIN_WIDTH, C_RED
from code.EntityMediator import EntityMediator
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player
from Const import C_WHITE,  EVENT_OBSTACLE, SPAWN_TIME, C_GREEN, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL
from code.Score import Score


class Level:
    def __init__(self, window: Surface, name: str, play_option: str):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.play_option = play_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity('Player1')
        self.entity_list.append(player)


        pygame.time.set_timer(EVENT_OBSTACLE, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self):
        pygame.mixer_music.load(f'assets/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                ent.draw(self.window)
                ent.move()

                if ent.name == 'Player1':
                    self.level_text(25, f'Player Health: {ent.health}', C_GREEN, (10, 25))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_OBSTACLE:
                    choice = random.choice(('Obstacle1', 'Obstacle2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                if self.timeout == 0:
                    return True

            self.level_text(20, f'Timeout: {self.timeout / 1000:.1f}s', C_WHITE, (10, 5))
            # self.level_text(14, f'fps: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            # self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
            self.level_text_info(50, 'SURVIVE!', C_RED, ((WIN_WIDTH / 2), 50))

            pygame.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            player = next(
                (ent for ent in self.entity_list if isinstance(ent, Player)),
                None
            )

            # Derrota
            if player is None or player.health <= 0:
                return False

            # Vitória
            if self.timeout <= 0:
                Score(self.window).show()
                return True

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Roboto", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

    def level_text_info(self, text_size: int, text: str, text_color: tuple, text_center_pos=tuple):
        text_font: Font = pygame.font.SysFont(name="Roboto", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
