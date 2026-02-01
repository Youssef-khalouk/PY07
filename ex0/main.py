
from ex0.CreatureCard import CreatureCard

if __name__ == "__main__":
    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print("CreatureCard Info:")
    print(dragon.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")

    print("Playable:", dragon.is_playable(6))
    print("Play result:", dragon.play({"mana": 6}))

    print("\nFire Dragon attacks Goblin Warrior:")
    goblin = CreatureCard('Goblin Warrior', 5, 'Legendary', 7, 5)
    print(f'Attack result: {dragon.attack_target(goblin)}')

    available_mana = 3
    print(f'\nTesting insufficient mana ({available_mana} available)')
    print(f"Playable: {dragon.is_playable(available_mana)}")

    print('\nAbstract pattern successfully demonstrated!')
