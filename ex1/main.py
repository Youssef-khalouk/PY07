
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck
from enum import Enum


class Players(Enum):
    DRAGON = "Fire Dragon"
    L_BOLT = "Lightning Bolt"
    CRYSTAL = "Mana Crystal"


def main():
    dragon = CreatureCard(Players.DRAGON.value, 5, "Legendary", 7, 5)
    l_bolt = SpellCard(
        Players.L_BOLT.value, 3, "Legendary", "Deal 3 damage to target")
    crystal = ArtifactCard(
        Players.CRYSTAL.value, 4, "Legendary", 5, "+1 mana per turn")

    deck = Deck()
    deck.add_card(dragon)
    deck.add_card(l_bolt)
    deck.add_card(crystal)

    print("\n=== DataDeck Deck Builder ===")
    print("\nBuilding deck with different card types...")
    print("Deck stats:", deck.get_deck_stats())

    print("\nDrawing and playing cards:")
    print("\nDrew: Lightning Bolt (Spell)")

    game_state = {}
    print("Play result:", l_bolt.play(game_state))

    print("\nDrew: Mana Crystal (Artifact)")
    print("Play result:", crystal.play(game_state))

    print("\nDrew: Fire Dragon (Creature)")
    print("Play result:", dragon.play(game_state))

    print(
        "\nPolymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
