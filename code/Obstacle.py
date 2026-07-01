import random

from code.Entity import Entity
from Const import ENTITY_SPEED


class Obstacle(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        # Cai para baixo
        self.speed_y = ENTITY_SPEED[self.name]

        # Anda para a esquerda
        self.speed_x = random.randint(1, ENTITY_SPEED[self.name] * 4)

    def move(self):
        self.rect.centerx -= self.speed_x
        self.rect.centery += self.speed_y
