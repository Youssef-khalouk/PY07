from ex0.Card import Card, CardType
from ex2 import Combatable, Magical


class EliteCard(Card, Combatable, Magical):
    """
    Represents a powerful elite card combining combat and
    magical abilities that can be played, attack, and cast spells.
    """
    def __init__(self, name: str, cost: int, rarity: str):
        super().__init__(name, cost, rarity)
        self.attack_power = 5
        self.health = 10
        self.mana = cost
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

    def channel_mana(self, amount: int) -> dict:
        return {
            'channeled': amount,
            'total_mana': 7
        }

    def get_magic_stats(self) -> dict:
        return {
            'mana': self.mana
        }
