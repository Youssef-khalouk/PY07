import random
from typing import Any

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """Class representing the tournament platform."""

    def __init__(self) -> None:
        """Initialize the tournament platform."""
        self.participators: list[TournamentCard] = []
        self.player_map: dict[str, TournamentCard] = {
            p.card_id: p for p in self.participators
        }
        self.match_count: int = 0
        self.activity: bool = False

    def register_card(self, card: TournamentCard) -> str:
        """Register a card in the tournament.

        Args:
            card (TournamentCard): The card to register.

        Returns:
            str: The card ID.
        """
        self.participators.append(card)
        self.player_map[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """Create and resolve a match between two cards.

        Args:
            card1_id (str): The ID of the first card.
            card2_id (str): The ID of the second card.

        Raises:
            ValueError: If a card ID is not found.

        Returns:
            dict: The match result.
        """
        self.match_count += 1

        card1: TournamentCard | None = self.player_map.get(card1_id)
        card2: TournamentCard | None = self.player_map.get(card2_id)

        if not card1 or not card2:
            raise ValueError("ID not found")
        first_player: TournamentCard = random.choice(seq=[card1, card2])
        second_player: TournamentCard = (
            card2 if first_player == card1 else card1
        )
        self.activity = True
        while first_player.health > 0 and second_player.health > 0:
            _ = first_player.attack(second_player)
            _ = second_player.defend(first_player.damage)
            if second_player.health > 0:
                _ = second_player.attack(first_player)
                _ = first_player.defend(second_player.damage)

        if first_player.health > 0:
            winner: TournamentCard = first_player
            loser: TournamentCard = second_player
        else:
            winner: TournamentCard = second_player
            loser: TournamentCard = first_player
        winner.update_wins(1)
        loser.update_losses(1)
        return {
            "winner": winner.name,
            "loser": loser.name,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }

    def get_leaderboard(self) -> list:
        """Retrieve the tournament leaderboard.

        Returns:
            list: A list of cards sorted by rating.
        """
        return sorted(
            self.participators,
            key=lambda target: target.calculate_rating(),
            reverse=True,
        )

    def generate_tournament_report(self) -> dict:
        """Generate a report of the tournament status.

        Returns:
            dict: A dictionary containing tournament statistics.
        """
        return {
            "total_cards": len(self.participators),
            "matches_played": self.match_count,
            "avg_rating": sum(p.calculate_rating() for p in self.participators)
            / len(self.participators),
            "platform_status": self.activity,
        }

    def print_leaderboard(self) -> None:
        """Print the tournament leaderboard to stdout."""
        leaderboard: list[TournamentCard] = self.get_leaderboard()
        print("Tournament Leaderboard:")
        for i, player in enumerate[TournamentCard](leaderboard, 1):
            players_record: dict = player.get_rank_info()
            rating: int = player.calculate_rating()
            record: Any | None = players_record.get("Record")
            print(f"{i}. {player.name} - Rating: {rating} ({record})")

    def print_report(self) -> None:
        """Print the tournament report to stdout."""
        print("Platform Report:")
        print(self.generate_tournament_report())
