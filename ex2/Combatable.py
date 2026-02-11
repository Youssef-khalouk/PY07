from abc import ABC, abstractmethod


class Combatable(ABC):
    """
    Abstract base class for entities that can
    engage in combat with attack and defense mechanics.
    """
    def __init__(self, name: str, attack_power: int, health: int):
        self.name = name
        self.attack_power = attack_power
        self.health = health

    @abstractmethod
    def attack(self, target) -> dict:
        pass

    def defend(self, incoming_damage: int) -> dict:
        self.health -= int(incoming_damage * 0.4)
        return {
            'defender': self.name,
            'damage_taken': int(incoming_damage * 0.4),
            'damage_blocked': int(incoming_damage * 0.6),
            'still_alive': True if self.health > 0 else False
        }

    def get_combat_stats(self) -> dict:
        return {
            'attack': self.attack_power,
            'health': self.health
        }
