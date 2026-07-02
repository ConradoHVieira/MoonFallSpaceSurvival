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
from Const import C_WHITE, EVENT_OBSTACLE, SPAWN_TIME, C_GREEN, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL
from code.Score import Score


class Level:
    def __init__(self, window: Surface, name: str, play_option: str):
        self.timeout = TIMEOUT_LEVEL  # Total survival time
        self.window = window
        self.name = name
        self.play_option = play_option
        self.entity_list: list[Entity] = []  # List containing all entities in the level

        self.entity_list.extend(
            EntityFactory.get_entity(self.name + 'Bg')
        )  # Add background layers for the parallax effect

        player = EntityFactory.get_entity('Player1')  # Create the player
        self.entity_list.append(player)

        pygame.time.set_timer(
            EVENT_OBSTACLE,
            SPAWN_TIME
        )  # Obstacle spawn timer

        pygame.time.set_timer(
            EVENT_TIMEOUT,
            TIMEOUT_STEP
        )  # Countdown timer

    def run(self):
        pygame.mixer_music.load(f'assets/{self.name}.mp3')  # Start level music
        pygame.mixer_music.play(-1)

        clock = pygame.time.Clock()

        while True:
            clock.tick(60)  # Limit the game to 60 FPS

            # Update and draw every entity
            for ent in self.entity_list:
                ent.draw(self.window)
                ent.move()

                # Display the player's health
                if ent.name == 'Player1':
                    self.level_text(
                        25,
                        f'Player Health: {ent.health}',
                        C_GREEN,
                        (10, 25)
                    )

            # Process game events
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Spawn a random obstacle
                if event.type == EVENT_OBSTACLE:
                    choice = random.choice(('Obstacle1', 'Obstacle2'))
                    self.entity_list.append(
                        EntityFactory.get_entity(choice)
                    )

                # Update the countdown timer
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP

            # Draw the player's HUD
            self.level_text(
                20,
                f'Timeout: {self.timeout / 1000:.1f}s',
                C_WHITE,
                (10, 5)
            )

            self.level_text_info(
                50,
                'SURVIVE!',
                C_RED,
                (WIN_WIDTH / 2, 50)
            )

            pygame.display.flip()

            # Check collisions and remove destroyed entities
            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)

            # Retrieve the player reference
            player = next(
                (ent for ent in self.entity_list if isinstance(ent, Player)),
                None
            )

            # Defeat condition: the player has no health remaining
            if player is None or player.health <= 0:
                return False

            # Victory condition: survive until the timer reaches zero
            if self.timeout <= 0:
                Score(self.window).show(True)
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