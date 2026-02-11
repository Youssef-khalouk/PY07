from abc import ABC, abstractmethod
from enum import Enum


class CardType(Enum):
    """Enumeration of all possible card types in the game."""
    Spell = "Spell"
    Creature = "Creature"
    Artifact = "Artifact"
    Elite_Card = "Elite Card"
    Tournament_Card = "Tournament Card"


class Card(ABC):
    """
    Abstract base class representing a generic
    game card with core attributes and behavior.
    """
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity,
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
