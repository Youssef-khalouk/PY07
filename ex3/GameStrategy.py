from abc import ABC, abstractmethod


class GameStrategy(ABC):
    """
    Abstract base class defining a game strategy with turn
    execution and target prioritization.
    """

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        pass
