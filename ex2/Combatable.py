from abc import ABC, abstractmethod


class Combatable(ABC):

    @abstractmethod
    def attack(self, target) -> dict:
        pass

    def defend(self, incoming_damage: int) -> dict:
        pass

    def get_combat_stats(self) -> dict:
        pass
