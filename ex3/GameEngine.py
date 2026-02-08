from abc import ABC, abstractmethod
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine(ABC):

    @abstractmethod
    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        pass

    @abstractmethod
    def simulate_turn(self) -> dict:
        pass

    @abstractmethod
    def get_engine_status(self) -> dict:
        pass
