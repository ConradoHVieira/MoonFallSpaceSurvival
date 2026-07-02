import random

from code.Background import Background
from code.Obstacle import Obstacle
from code.Player import Player
from Const import WIN_WIDTH, WIN_HEIGHT


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:

            # Create the background layers used for the parallax effect
            case 'Level1Bg':
                list_bg = []

                for i in range(5):  # Number of background layers
                    # First image displayed on screen
                    list_bg.append(
                        Background(f'Level1Bg{i}', position=(0, 0))
                    )

                    # Second image positioned to create a seamless scrolling effect
                    list_bg.append(
                        Background(f'Level1Bg{i}', position=(WIN_WIDTH, 0))
                    )

                return list_bg

            # Create the player on the left side of the screen
            case 'Player1':
                return Player('Player1', (25, WIN_HEIGHT / 2))

            # Create an obstacle at a random position in the upper-right region,
            # outside the visible screen
            case 'Obstacle1':
                return Obstacle(
                    'Obstacle1',
                    (
                        random.randint(WIN_WIDTH // 2, WIN_WIDTH + 50),
                        random.randint(-80, 0)
                    )
                )

            # Create a second obstacle using the same spawn logic
            case 'Obstacle2':
                return Obstacle(
                    'Obstacle2',
                    (
                        random.randint(WIN_WIDTH // 2, WIN_WIDTH + 50),
                        random.randint(-80, 0)
                    )
                )