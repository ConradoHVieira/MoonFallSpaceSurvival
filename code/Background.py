#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Entity import Entity
from Const import WIN_WIDTH, ENTITY_SPEED


class Background(Entity):

    def __init__(self, name: str, position: tuple):
        # Initialize the background layer
        super().__init__(name, position)

    # Move the background continuously to the left
    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

        # Reposition the image on the right side of the screen
        # to create an infinite scrolling effect
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH