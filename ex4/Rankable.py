from abc import ABC, abstractmethod


class Rankable(ABC):
    """
    Abstract base class for objects that track wins, losses,
    and rating, with a customizable ranking calculation.
    """
    @abstractmethod
    def calculate_rating(self) -> int:
        pass

    def update_wins(self, wins: int) -> None:
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        pass
