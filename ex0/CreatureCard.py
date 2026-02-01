
from ex0.Card import Card


class CreatureCard(Card):

    def __init__(
                self,
                name: str,
                cost: int,
                rarity: str,
                attack: int,
                health: int) -> None:
        super().__init__(name, cost, rarity)

        if attack <= 0:
            raise ValueError("attack must be a positive integer")
        if health <= 0:
            raise ValueError("health must be a positive integer")

        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        game_state["battlefield"] = game_state.get("battlefield", [])
        game_state["battlefield"].append(self.name)
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["attack"] = self.attack
        info["health"] = self.health
        return info
