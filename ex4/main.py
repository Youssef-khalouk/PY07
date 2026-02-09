#!/usr/bin/env python3
from ex2.EliteCard import Rarity
from ex3.CardFactory import CreaturesType
from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard


def main() -> None:
    """Execute the main demonstration of the Tournament Platform."""
    try:
        print()
        print("=== DataDeck Tournament Platform ===")
        print()
        board_game: TournamentPlatform = TournamentPlatform()
        print("Registering Tournament Cards...")
        print()
        fire_dragon: TournamentCard = TournamentCard(
            CreaturesType.DRAGON.value, 10, Rarity.EPIC.value, 10, 50,
            "dragon_001", 1200)
        first_id: str = board_game.register_card(fire_dragon)
        print(fire_dragon)
        print()
        wizard: TournamentCard = TournamentCard(
            CreaturesType.WIZARD.value, 9, Rarity.COMMON.value, 8, 60,
            "wizard_001", 1150)
        print(wizard)
        second_id: str = board_game.register_card(wizard)
        print()
        print("Creating tournament match...")
        print(board_game.create_match(first_id, second_id))
        print()
        board_game.print_leaderboard()
        print()
        board_game.print_report()
        print()
    except Exception as e:
        print(f"Something went wrong -> {e}")
    finally:
        print("=== Tournament Platform Successfully Deployed! ===")
        print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
