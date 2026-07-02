from abc import ABC, abstractmethod

import pygame.image

from Const import ENTITY_HEALTH, ENTITY_DAMAGE


class Entity(ABC):

    def __init__(self, name: str, position: tuple):
        # Load the entity sprite and initialize its attributes
        self.name = name
        self.surf = pygame.image.load('assets/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])

        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]

    # Abstract method implemented by every game entity
    @abstractmethod
    def move(self):
        pass

    # Render the entity on the game window
    def draw(self, window):
        window.blit(self.surf, self.rect)