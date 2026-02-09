#!/usr/bin/env python3
from ex0.Card import Card
from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


def main() -> None:
    try:
        print("\n=== DataDeck Deck Builder ===\n")

        my_deck: Deck = Deck()
        lightning_bolt: SpellCard = SpellCard(
            "Lightning Bolt", 3, "rare",
            'Deal 3 damage to target')
        mana_crystal: ArtifactCard = ArtifactCard(
            "Mana Crystal", 2, "common", 5, "Permanent: +1 mana per turn"
        )
        fire_dragon: CreatureCard = CreatureCard(
            "Fire Dragon", 5, "Legendary", 7, 5)
        for card_to_add in (lightning_bolt, mana_crystal, fire_dragon):
            my_deck.add_card(card=card_to_add)
        my_deck.shuffle()
        print("Building deck with different card types...")
        print("Deck stats:", my_deck.get_deck_stats())

        print("\nDrawing and playing cards:\n")
        while len(my_deck.deck) > 0:
            card: Card = my_deck.draw_card()
            card_data: dict = card.get_card_info()
            print(f"Drew: {card.name} ({card_data['type']})")
            print("Play result:", card.play({}))
            print()
        print(
            "Polymorphism in action: Same interface, different card behaviors!"
            )
    except Exception as e:
        print(f"Something went wrong -> {e}")


if __name__ == "__main__":
    main()
