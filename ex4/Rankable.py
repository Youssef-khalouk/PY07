from abc import ABC, abstractmethod


class Rankable(ABC):
    """
    Abstract base class for objects that track wins, losses,
    and rating, with a customizable ranking calculation.
    """

    def __init__(self, br: int):
        self._wins = 0
        self._losses = 0
        self._rating = br

    @abstractmethod
    def calculate_rating(self) -> int:
        pass

    def update_wins(self, wins: int) -> None:
        if wins < 0:
            raise ValueError("wins must be >= 0")
        self._wins += wins

    def update_losses(self, losses: int) -> None:
        if losses < 0:
            raise ValueError("losses must be >= 0")
        self._losses += losses

    def get_rank_info(self) -> dict:
        return {
            "rating": self._rating,
            "wins": self._wins,
            "losses": self._losses
        }
