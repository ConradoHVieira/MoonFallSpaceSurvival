#   C
import pygame

C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (242, 197, 92)
C_GREEN = (0, 128, 0)
C_RED = (255, 0, 0)



#  E


ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Player1': 100,
    'Obstacle1': 5,
    'Obstacle2': 10,
}

EVENT_OBSTACLE = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Player1': 100,
    'Obstacle1': 50,
    'Obstacle2': 60,
}

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 4,
    'Level1Bg4': 5,
    'Level1Bg5': 6,
    'Player1': 3,
    'Obstacle1': 6,
    'Obstacle2': 7,

}

#   M

MENU_OPTION = ('NEW SURVIVAL GAME',
               'EXIT'
               )

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP}

PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN}

PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT}

PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT}



# S

SPAWN_TIME = 750

# T

TIMEOUT_STEP = 100  # 100ms
TIMEOUT_LEVEL = 60000  # 60s S

#   W
WIN_WIDTH = 640
WIN_HEIGHT = 360

CONTROLS_POS = (10, WIN_HEIGHT - 10)

SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'Subtitle': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Label2': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }
