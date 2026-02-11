
from ex0.CreatureCard import CreatureCard


def main() -> None:
    """
    Demonstrates the creation, playability,
    and attack actions of a CreatureCard instance.
    """
    print("\n=== DataDeck Card Foundation ===")
    print("\nTesting Abstract Base Class Design:\n")

    creature_card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print("\nCreatureCard Info:")
    print(creature_card.get_card_info())

    name = creature_card.name
    print(f"\nPlaying {name} with 6 mana available:")
    print(f"Playable: {creature_card.is_playable(6)}")
    print(f"Play result: {creature_card.play({})}")

    target = "Goblin Warrior"
    print(f"\n{name} attacks {target}:")
    print(f"Attack result: {creature_card.attack_target(target)}")

    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {creature_card.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == '__main__':
    main()
