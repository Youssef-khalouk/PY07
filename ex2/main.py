from ex2.EliteCard import CombatType, EliteCard, Rarity
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.Card import Card


def get_public_methods(cls) -> list[str]:
    return [
        meth
        for meth in dir(cls)
        if callable(getattr(cls, meth)) and not meth.startswith("__")
    ]


def main() -> None:
    try:
        print()
        print("=== DataDeck Ability System ===")
        print()
        print(EliteCard.__qualname__, "capabilities:")
        classes_to_check = [Card, Combatable, Magical]

        for cls in classes_to_check:
            methods: list[str] = get_public_methods(cls)
            print(f"- {cls.__name__}: {methods}")

        warrior1: EliteCard = EliteCard("Arcane warrior", 2,
                                        Rarity.RARE.value, 5, 10,
                                        CombatType.MELEE.value)
        warrior2: EliteCard = EliteCard("Arcane warrior", 2,
                                        Rarity.RARE.value, 5, 10,
                                        CombatType.MELEE.value)
        print()
        print(f"Playing {warrior1.name} ({EliteCard.__qualname__})")
        warrior1.play({})
        print()
        print("Combat phase:")
        print("Attack result:", warrior1.attack(warrior2))
        defend: dict = warrior2.defend(warrior1.damage)
        print("Defense result:", defend)
        print()
        print("Magic phase:")
        enemies: list = ["Enemy1", "Enemy2"]
        cast: dict = warrior1.cast_spell("Fireball", enemies)
        print("Spell cast:", cast)
        print("Mana channel:", warrior1.channel_mana(3))
        print()
        print("Multiple interface implementation successful!")
    except Exception as e:
        print(f"Something went wrong -> {e}")


if __name__ == "__main__":
    main()
