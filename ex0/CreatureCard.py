from ex0.Card import Card


class CreatureCard(Card):

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):

        super().__init__(name, cost, rarity)
        self.attack = 0
        self.health = 0
        if attack <= 0:
            raise ValueError("attack must be a positive integer")
        if health <= 0:
            raise ValueError("health must be a positive integer")
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:

        return game_state | {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
        }

    def attack_target(self, target) -> dict:
        status = False
        if self.attack >= target.health:
            status = True
        return {
            'attacker': self.name,
            'target': target.name,
            "damage_dealt": self.attack,
            'combat_resolved': status
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["attack"] = self.attack
        info["health"] = self.health
        return info
