from abc import ABC, abstractmethod


class Magical(ABC):
    """
    Abstract base class for entities with magical abilities,
    mana management, and spellcasting.
    """
    def __init__(self, mana: int):
        self.mana = mana

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    def channel_mana(self, amount: int) -> dict:
        return {
            'channeled': amount,
            'total_mana': 7
        }

    def get_magic_stats(self) -> dict:
        return {
            'mana': self.mana
        }
