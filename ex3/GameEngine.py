from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex0.Card import Card


class GameEngine():
    """
    Simulates game turns using a card factory and strategy,
    tracking battlefield state, damage, and created cards.
    """

    def __init__(self):
        self.hand: list[Card] = []
        self.battlefield: list = []
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, fac: CardFactory, stg: GameStrategy) -> None:
        self.factory = fac
        self.strategy = stg
        self.hand = fac.create_themed_deck(3)['cards']
        self.cards_created = len(self.hand)

    def simulate_turn(self) -> dict:
        if not self.factory or not self.strategy:
            raise RuntimeError("Engine not configured")
        self.turns_simulated += 1
        result = self.strategy.execute_turn(self.hand, self.battlefield)
        dmg = result.get("actions", {}).get("damage_dealt", 0)
        if isinstance(dmg, int):
            self.total_damage += dmg
        return result

    def get_engine_status(self) -> dict:
        strategy = None
        if self.strategy:
            strategy = self.strategy.get_strategy_name()
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': strategy,
            'total_damage': self.total_damage,
            'cards_created': self.cards_created
        }
