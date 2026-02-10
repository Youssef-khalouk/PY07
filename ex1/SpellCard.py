from ex0.Card import Card, CardType


class SpellCard(Card):
    """
    Represents a spell card with a specific effect type that
    can be played and applied to targets.
    """
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.type = CardType["Spell"]
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        effect = self.effect_type
        return game_state | {
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
