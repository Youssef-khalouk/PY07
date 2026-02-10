from ex2 import EliteCard


def main() -> None:
    """
    Demonstrates EliteCard’s combined card, combat,
    and magicalabilities in action.
    """

    print("\n=== DataDeck Ability System ===")

    print("\nEliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    elitecard = EliteCard("Arcane Warrior", 5, "Elite")
    print("\nPlaying Arcane Warrior (Elite Card):")
    print("\nCombat phase:")
    print(f"Attack result: {elitecard.attack("Enemy")}")
    print(f"Defense result: {elitecard.defend(5)}")

    targets = ['Enemy1', 'Enemy2']
    print("\nMagic phase:")
    print(f"Spell cast: {elitecard.cast_spell("Fireball", targets)}")
    print(f"Mana channel: {elitecard.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
