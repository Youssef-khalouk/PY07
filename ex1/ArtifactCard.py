from ex0.Card import Card, CardType


class ArtifactCard(Card):
    """
    Represents an artifact card with durability and a
    permanent effect that can be played and activated.
    """
    def __init__(self, name: str, cost: int, rarity: str, dur: int, eff: str):
        super().__init__(name, cost, rarity)
        self.type = CardType["Artifact"]
        self.effect = f"Permanent: {eff}"
        self.durability = dur

    def play(self, game_state: dict) -> dict:
        return game_state | {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect
        }

    def activate_ability(self) -> dict:
        return {
            "artifact": self.name,
            "effect": self.effect
        }
