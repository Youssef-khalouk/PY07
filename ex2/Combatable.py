from abc import ABC, abstractmethod


class Combatable(ABC):

    def __init__(self, name: str):
        self.name = name
        self.defense = 3
        self.attack_power = 5
        self.health = 10

    @abstractmethod
    def attack(self, target) -> dict:
        pass

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(self.defense, incoming_damage)
        taken = incoming_damage - blocked
        self.health -= taken

        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "defense": self.defense,
            "health": self.health
        }
