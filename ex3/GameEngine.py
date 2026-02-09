from typing import Any
from abc import ABC, abstractmethod
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine(ABC):

    @abstractmethod
    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        ...

    @abstractmethod
    def simulate_turn(self) -> dict:
        ...

    @abstractmethod
    def get_engine_status(self) -> dict:
        ...


class MegaSuperEngine(ABC):

    def __init__(self) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.turns_simulated: int = 0
        self.total_damage: int = 0
        self.cards_created: int = 0

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self.factory = factory
        self.strategy = strategy
        print("Factory:", factory.__class__.__name__)
        print("Strategy:", strategy.__class__.__name__)

    def simulate_turn(self) -> dict:
        if not self.factory or not self.strategy:
            raise ValueError("Engine not configured!")

        self.turns_simulated += 1
        hand: dict[Any, Any] = self.factory.create_themed_deck(size=5)
        hand2: dict[Any, Any] = self.factory.create_themed_deck(size=5)
        print("Hand:", end=" [")
        print(*hand.str_list(), sep=", ", end="]\n")
        self.total_damage = sum(
            card.attack for card in hand.deck if hasattr(card, "attack")
        )
        self.cards_created = len(hand.deck)
        print()
        print("Turn execution:")
        print("Strategy:", self.strategy.get_strategy_name())
        turn_result = self.strategy.execute_turn(hand.deck, hand2.deck)
        print("Actions:", turn_result)
        return turn_result

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
