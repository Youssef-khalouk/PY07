from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name, cost, rarity):
        Card.__init__(name, cost, rarity)

    def play(self, game_state: dict) -> dict:
        game_state["battlefield"] = game_state.get("battlefield", [])
        game_state["battlefield"].append(self.name)
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect_type
        }

    def attack(self, target):
        pass

    def cast_spell(self, spell_name, targets):
        pass
