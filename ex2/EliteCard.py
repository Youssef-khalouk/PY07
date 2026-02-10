from ex0.Card import Card, CardType
from ex2 import Combatable, Magical


class EliteCard(Card, Combatable, Magical):
    """
    Represents a powerful elite card combining combat and
    magical abilities that can be played, attack, and cast spells.
    """
    def __init__(self, name: str, cost: int, rarity: str):
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, name, 5, 10)
        Magical.__init__(self, cost)

        self.type = CardType["Elite_Card"]
        self.effect = "Elite card enters the battlefield"

    def play(self, game_state: dict) -> dict:
        return game_state | {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect
        }

    def attack(self, target) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.attack_power,
            'combat_type': 'melee'
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': self.cost
        }
