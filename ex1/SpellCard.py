from ex0.Card import Card
from enum import Enum


class Effect(Enum):
    damage = 1
    heal = 2
    buff = 3
    debuff = 4


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.type = "Spell"
        self.effect_type = Effect[effect_type]

    def play(self, game_state: dict) -> dict:
        effect = Effect(self.effect_type).name
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Deal {self.cost} {effect} to target"
        }

    def resolve_effect(self, targets: list) -> dict:
        return {
            "spell": self.name,
            "targets": targets,
            "effect_type": self.effect_type
        }
