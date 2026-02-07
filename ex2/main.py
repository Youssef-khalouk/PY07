from ex2.EliteCard import EliteCard


def main():
    print("=== DataDeck Ability System ===")

    card = EliteCard("Arcane Warrior", 7, "rar")

    print("EliteCard capabilities:")
    print("- Card:", [
        method for method in dir(card) if method in
        ["play", "get_card_info", "is_playable"]
    ])
    print("- Combatable:", ["attack", "defend", "get_combat_stats"])
    print("- Magical:", ["cast_spell", "channel_mana", "get_magic_stats"])

    print("\nPlaying Arcane Warrior (Elite Card):")

    print("\nCombat phase:")
    attack_result = card.attack("Enemy")
    print("Attack result:", attack_result)

    defense_result = card.defend(5)
    print("Defense result:", defense_result)

    print("\nMagic phase:")
    spell_result = card.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print("Spell cast:", spell_result)

    mana_result = card.channel_mana(3)
    print("Mana channel:", mana_result)

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
