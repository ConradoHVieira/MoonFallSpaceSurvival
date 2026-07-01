import random

from code.Background import Background
from code.Obstacle import Obstacle

from code.Obstacle import Obstacle
from code.Player import Player
from Const import WIN_WIDTH, WIN_HEIGHT


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(5):  # bg images number
                    list_bg.append(Background(f'Level1Bg{i}', position=(0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', position=(WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (25, WIN_HEIGHT / 2))
            case 'Obstacle1':
                return Obstacle('Obstacle1', (random.randint(WIN_WIDTH // 2, WIN_WIDTH + 50), random.randint(-80, 0)))
            case 'Obstacle2':
                return Obstacle('Obstacle2', (random.randint(WIN_WIDTH // 2, WIN_WIDTH + 50), random.randint(-80, 0)))
