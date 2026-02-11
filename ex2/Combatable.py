from abc import ABC, abstractmethod


class Combatable(ABC):
    """
    Abstract base class for entities that can
    engage in combat with attack and defense mechanics.
    """
    @abstractmethod
    def attack(self, target) -> dict:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        pass
