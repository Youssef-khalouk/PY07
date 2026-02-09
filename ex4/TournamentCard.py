from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """Class representing a card used in tournaments."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        damage: int,
        health: int,
        card_id: str,
        rating: int,
    ) -> None:
        """Initialize the tournament card.

        Args:
            name (str): The name of the card.
            cost (int): The mana cost.
            rarity (str): The rarity level.
            damage (int): The damage value.
            health (int): The health points.
            card_id (str): The unique identifier for the card.
            rating (int): The initial rating.
        """
        super().__init__(name, cost, rarity)
        self.wins: int = 0
        self.losses: int = 0
        self.__rating: int = rating
        self.damage: int = damage
        self.health: int = health
        self.card_id: str = card_id

    def play(self, game_state: dict) -> dict:
        """Play the tournament card.

        Args:
            game_state (dict): The current game state.

        Returns:
            dict: The updated game state.
        """
        return game_state | {
            "name": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def attack(self, target) -> dict:
        """Attack a target.

        Args:
            target: The target entity.

        Returns:
            dict: The combat result.
        """
        target.health -= self.damage
        if self.damage >= target.health:
            status = True
        else:
            status = False
        return {
            "attacker": self.name,
            "target": target.name,
            "combat_resolved": status,
        }

    def defend(self, incoming_damage: int) -> dict:
        """Defend against incoming damage.

        Args:
            incoming_damage (int): The amount of damage received.

        Returns:
            dict: The defense result.
        """
        damage_taken: int = incoming_damage
        self.health -= damage_taken
        return {
            "defender": self.name,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict:
        """Retrieve combat statistics.

        Returns:
            dict: A dictionary containing combat stats.
        """
        return {"damage": self.damage}

    def calculate_rating(self) -> int:
        """Calculate the tournament rating.

        Returns:
            int: The calculated rating based on wins and losses.
        """
        return self.__rating + (self.wins * 16) - (self.losses * 16)

    def update_losses(self, losses: int) -> None:
        """Update the number of losses.

        Args:
            losses (int): The number of losses to add.
        """
        self.losses += losses

    def update_wins(self, wins: int) -> None:
        """Update the number of wins.

        Args:
            wins (int): The number of wins to add.
        """
        self.wins += wins

    def get_tournament_stats(self) -> dict:
        """Retrieve tournament-specific statistics.

        Returns:
            dict: A dictionary containing inheritance info.
        """
        parents: list[str] = [cls.__name__ for cls in self.__class__.__bases__]
        return {"Interfaces": parents}

    def get_rank_info(self) -> dict:
        """Retrieve ranking information.

        Returns:
            dict: A dictionary with rating and record.
        """
        return {
            "Rating": self.calculate_rating(),
            "Record": f"{self.wins}-{self.losses}",
        }

    def __str__(self) -> str:
        """Return a string representation of the tournament card.

        Returns:
            str: The formatted string representation.
        """
        lines: list[str] = [f"{self.name} (ID: {self.card_id}):"]

        all_stats: dict = {
            **self.get_tournament_stats(),
            **self.get_rank_info(),
        }

        for label, value in all_stats.items():
            if isinstance(value, list):
                display_value = ", ".join(value)
            else:
                display_value = value
            lines.append(f"- {label}: {display_value}")

        return "\n".join(lines)
