
from enum import Enum
from ex0.CreatureCard import CreatureCard


class Players(Enum):
    DRAGON = "Fire Dragon"
    GOBLIN = "Goblin Warrior"


if __name__ == "__main__":

    dragon = CreatureCard(Players.DRAGON.value, 5, "Legendary", 7, 5)
    print("CreatureCard Info:")
    print(dragon.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")

    game_state = {"mana": 6}

    print("Playable:", dragon.is_playable(6))
    print("Play result:", dragon.play(game_state))

    print("\nFire Dragon attacks Goblin Warrior:")
    goblin = CreatureCard(Players.GOBLIN.value, 5, 'Legendary', 7, 5)
    print(f'Attack result: {dragon.attack_target(goblin)}')

    available_mana = 3
    print(f'\nTesting insufficient mana ({available_mana} available)')
    print(f"Playable: {dragon.is_playable(available_mana)}")

    print('\nAbstract pattern successfully demonstrated!')
