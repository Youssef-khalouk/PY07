from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard


def main() -> None:
    """
    Demonstrates registering TournamentCards, running matches,
    and viewing leaderboard and platform reports.
    """

    print("\n=== DataDeck Tournament Platform ===")

    platform = TournamentPlatform()
    print("\nRegistering Tournament Cards...")
    dragon = TournamentCard("Dragon", 5, "Legend", a=7, h=5, br=1200)
    wizard = TournamentCard("Wizard", 4, "Epic", a=5, h=6, br=1150)
    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)
    dragon_result = dragon.get_rank_info()
    print(f"\n{dragon.name} (ID: {dragon_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {dragon_result['rating']}")
    print(f"- Record: ({dragon_result['wins']} - {dragon_result['losses']})")

    wizard_result = wizard.get_rank_info()
    print(f"\n{wizard.name} (ID: {wizard_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {wizard_result['rating']}")
    print(f"- Record: ({wizard_result['wins']} - {wizard_result['losses']})")

    print("\nCreating tournament match...")
    print("Match result:", platform.create_match(dragon_id, wizard_id))

    print("\nTournament Leaderboard:")
    rank = 0
    for _, name, rating, wins, losses in platform.get_leaderboard():
        rank += 1
        print(f"{rank}. {name} - Rating: {rating} ({wins}-{losses})")

    print("\nPlatform Report:", platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print('All abstract patterns working together harmoniously!')


if __name__ == '__main__':
    main()
