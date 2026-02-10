from ex0.Card import Card
from typing import List
import random


class Deck:
    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        creatures = [card for card in self.cards if card.type == "Creature"]
        spells = [card for card in self.cards if card.type == "Spell"]
        artifacts = [card for card in self.cards if card.type == "Artifact"]
        cost = 0
        for card in self.cards:
            cost += card.cost
        return {
            'total_cards': len(self.cards),
            'creatures': len(creatures),
            'spells': len(spells),
            'artifacts': len(artifacts),
            'avg_cost': round(cost / len(self.cards), 1)
        }
