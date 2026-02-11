from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck


def main() -> None:
    """
    Demonstrates building, shuffling, drawing,
    and playing various card types in a Deck.
    """
    deck = Deck()
    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 5, 10))
    deck.add_card(ArtifactCard(
        "Mana Crystal", 2, "Common", 4, "+1 mana per turn"))
    deck.add_card(SpellCard("Lightning Bolt", 3, "Usual", "damage"))
    deck.shuffle()
    print("=== DataDeck Deck Builder ===")
    print("\nBuilding deck with different card types...")
    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:")

    card = deck.draw_card()
    deck.remove_card(card.name)
    print(f"\nDrew: {card.name} ({card.type})")
    print(f"Play result: {card.play({})}")

    card = deck.draw_card()
    deck.remove_card(card.name)
    print(f"\nDrew: {card.name} ({card.type})")
    print(f"Play result: {card.play({})}")

    card = deck.draw_card()
    deck.remove_card(card.name)
    print(f"\nDrew: {card.name} ({card.type})")
    print(f"Play result: {card.play({})}")

    print("\nPolymorphism in action:", end=" ")
    print("Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
