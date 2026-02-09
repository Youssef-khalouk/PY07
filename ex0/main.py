#!/usr/bin/env python3
from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print("CreatureCard Info:")
    print(dragon.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")

    game_state = {}

    print("Playable:", dragon.is_playable(6))
    print("Play result:", dragon.play(game_state))

    print("\nFire Dragon attacks Goblin Warrior:")
    goblin = CreatureCard("Goblin Warrior", 5, 'Legendary', 7, 5)
    print(f'Attack result: {dragon.attack_target(goblin)}')

    available_mana = 3
    print(f'\nTesting insufficient mana ({available_mana} available)')
    print(f"Playable: {dragon.is_playable(available_mana)}")

    print('\nAbstract pattern successfully demonstrated!')


if __name__ == "__main__":
    main()
