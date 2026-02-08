import random
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: str):
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, name)
        Magical.__init__(self, name)

        self.mana = 4

    # -------- Card --------
    def play(self, game_state: dict) -> dict:
        game_state["battlefield"] = game_state.get("battlefield", [])
        game_state["battlefield"].append(self.name)
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"health: {self.health}"
        }

    # -------- Combatable --------
    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    # -------- Magical --------
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_cost = random.randint(2, 4)
        self.mana -= mana_cost

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_cost
        }
