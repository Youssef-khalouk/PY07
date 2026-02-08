from abc import ABC, abstractmethod


class Magical(ABC):

    def __init__(self, name: str):
        self.name = name
        self.mana = 4

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> dict:
        return {
            "mana": self.mana
        }
