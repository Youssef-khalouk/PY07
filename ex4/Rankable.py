from abc import ABC, abstractmethod


class Rankable(ABC):
    """Abstract base class for rankable entities."""

    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculate the current rating.

        Returns:
            int: The calculated rating.
        """
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Update the win count.

        Args:
            wins (int): The number of wins to add.
        """
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Update the loss count.

        Args:
            losses (int): The number of losses to add.
        """
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        """Retrieve ranking information.

        Returns:
            dict: A dictionary containing ranking details.
        """
        pass
