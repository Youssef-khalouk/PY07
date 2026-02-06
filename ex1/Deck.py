
from ex0 import Card
from ex0 import CreatureCard
from ex1 import SpellCard
from ex1 import ArtifactCard
import random


class Deck:
    def __init__(self):
        self._cards = []

    def add_card(self, card: Card) -> None:
        self._cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for i in len(self._cards):
            if self._cards[i].name == card_name:
                self._cards.pop(i)
                return 1
        return 0

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def draw_card(self) -> Card:
        if self._cards:
            card = self._cards[0]
            self._cards.pop(0)
            return card
        return None

    def get_deck_stats(self) -> dict:
        stats = {}
        stats["total_cards"] = len(self._cards)
        stats["creatures"] = sum(
            1 for card in self._cards if isinstance(card, CreatureCard))
        stats["spells"] = sum(
            1 for card in self._cards if isinstance(card, SpellCard))
        stats["artifacts"] = sum(
            1 for card in self._cards if isinstance(card, ArtifactCard))
        stats["avg_cost"] = sum(
            card.cost for card in self._cards) / len(self._cards)
        return stats
