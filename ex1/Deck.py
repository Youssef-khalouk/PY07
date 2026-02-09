import random
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class Deck:
    def __init__(self) -> None:
        self.deck: list[Card] = []

    def add_card(self, card: Card) -> None:

        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:

        for card in self.deck:
            if card.name == card_name:
                self.deck.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        if len(self.deck) > 0:
            random.shuffle(self.deck)

    def draw_card(self) -> Card:

        if len(self.deck) > 0:
            card_to_draw: Card = self.deck.pop()
            return card_to_draw
        return None

    def get_deck_stats(self) -> dict:

        avg = sum(c.cost for c in self.deck) / (len(self.deck) or 1)
        return {
            "total_cards": len(self.deck),
            "creatures": sum(1 for card in self.deck if isinstance(
                card, CreatureCard)),
            "spells": sum(1 for card in self.deck if isinstance(
                card, SpellCard)),
            "artifacts": sum(1 for card in self.deck if isinstance(
                card, ArtifactCard)),
            "avg_cost": avg
        }

    def str_list(self) -> list[str]:
        return [f"{card.name} ({card.cost})" for card in self.deck]
