import pygame.key

from code.Entity import Entity
from Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT


class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        # Load the player animation frames
        self.frames = []

        for i in range(5):
            self.frames.append(
                pygame.image.load(f'assets/{name}_{i}.png').convert_alpha()
            )

        self.current_frame = 0
        self.animation_counter = 0

        # Number of updates before switching to the next animation frame
        self.animation_speed = 5

        # Load exhaust animations
        self.exhaust_frames = []

        # Idle animation
        self.exhaust_idle = [
            pygame.image.load("assets/exhaust_idle_0.png").convert_alpha(),
            pygame.image.load("assets/exhaust_idle_1.png").convert_alpha()
        ]

        # Exhaust animation while moving left
        self.exhaust_left = [
            pygame.image.load("assets/exhaust_low_0.png").convert_alpha(),
            pygame.image.load("assets/exhaust_low_1.png").convert_alpha()
        ]

        # Exhaust animation while moving right
        self.exhaust_right = [
            pygame.image.load("assets/exhaust_high_0.png").convert_alpha(),
            pygame.image.load("assets/exhaust_high_1.png").convert_alpha()
        ]

        # Set the default exhaust animation
        self.exhaust_frames = self.exhaust_idle
        self.exhaust_frame = 0
        self.exhaust_counter = 0
        self.exhaust_speed = 6
        self.exhaust = self.exhaust_frames[0]

    # Draw the exhaust and the player sprite
    def draw(self, window):

        exhaust_x = self.rect.left - 20
        exhaust_y = self.rect.centery - self.exhaust.get_height() // 2

        window.blit(self.exhaust, (exhaust_x, exhaust_y))
        window.blit(self.surf, self.rect)

    # Handle player movement and animations
    def move(self):
        self.exhaust_frames = self.exhaust_idle
        pressed_key = pygame.key.get_pressed()

        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
            self.exhaust_frames = self.exhaust_left

        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
            self.exhaust_frames = self.exhaust_right

        self.animate()
        self.animate_exhaust()

    # Update the player animation
    def animate(self):
        self.animation_counter += 1

        if self.animation_counter >= self.animation_speed:
            self.animation_counter = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.surf = self.frames[self.current_frame]

    # Update the exhaust animation
    def animate_exhaust(self):
        self.exhaust_counter += 1

        if self.exhaust_counter >= self.exhaust_speed:
            self.exhaust_counter = 0
            self.exhaust_frame = (self.exhaust_frame + 1) % len(self.exhaust_frames)

        self.exhaust = self.exhaust_frames[self.exhaust_frame]