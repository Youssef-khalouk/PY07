from ex0.Card import Card, CardType


class CreatureCard(Card):
    """
    Represents a creature card with attack and
    health that can be played and attack targets.
    """
    def __init__(self, name: str, cost: int, rarity: str, att: int, hp: int):
        if att <= 0 or hp <= 0:
            raise ValueError("attack and health must be positive")
        super().__init__(name, cost, rarity)
        self.type = CardType["Creature"]
        self.attack = att
        self.health = hp

    def play(self, game_state: dict) -> dict:
        return game_state | {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': "Creature summoned to battlefield"
        }

    def attack_target(self, target) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage_dealt': self.attack,
            'combat_resolved': True
        }

    def get_card_info(self) -> dict:
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity,
            'type': self.type.name,
            'attack': self.attack,
            'health': self.health
        }
