#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

from code.Entity import Entity
from Const import ENTITY_SPEED


class Obstacle(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        # Velocidade horizontal (para a esquerda)
        self.speed_x = ENTITY_SPEED[self.name]

        # Velocidade vertical aleatória (sempre para baixo)
        self.speed_y = random.randint(1, self.speed_x // 4)

    def move(self):
        self.rect.centerx -= self.speed_x
        self.rect.centery += self.speed_y
        print(self.rect.size)

        from Const import WIN_HEIGHT
