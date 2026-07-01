from code.Entity import Entity
from code.Obstacle import Obstacle
from code.Player import Player
from Const import WIN_HEIGHT


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Obstacle):
            # Remove o obstáculo quando sair da tela
            if ent.rect.right <= 0 or ent.rect.top >= WIN_HEIGHT:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1: Entity, ent2: Entity):
        valid_interaction = (
                (isinstance(ent1, Obstacle) and isinstance(ent2, Player)) or
                (isinstance(ent1, Player) and isinstance(ent2, Obstacle))
        )

        if not valid_interaction:
            return

        # Colisão utilizando a função do Pygame
        if ent1.rect.colliderect(ent2.rect):
            ent1.health -= ent2.damage
            ent2.health -= ent1.damage
            ent1.last_dmg = ent2.name
            ent2.last_dmg = ent1.name

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]

            EntityMediator.__verify_collision_window(entity1)

            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
