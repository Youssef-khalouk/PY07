from ex0.Card import Card, CardType
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """
    Represents a tournament card combining card, combat,
    and ranking features for gameplay and stats tracking.
    """

    def __init__(self, n: str, c: int, r: str, a: int, h: int, br: int = 1200):
        super().__init__(n, c, r)
        self.name = n
        self.attack_power = a
        self.health = h
        self._wins = 0
        self._losses = 0
        self._rating = br
        self.type = CardType["Tournament_Card"]

    def play(self, game_state: dict) -> dict:
        return game_state | {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card enters the battlefield"
        }

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "tournament"
        }

    def calculate_rating(self) -> int:
        return self._rating

    def get_tournament_stats(self) -> dict:
        info = self.get_rank_info()
        return {
            "name": self.name,
            "rating": info["rating"],
            "record": f'{info["wins"]}-{info["losses"]}',
            "combat": self.get_combat_stats()
        }

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

    def defend(self, incoming_damage: int) -> dict:
        self.health -= int(incoming_damage * 0.4)
        blocked = min(self.attack_power, incoming_damage)
        return {
            'defender': self.name,
            'damage_taken': incoming_damage - blocked,
            'damage_blocked': blocked,
            'still_alive': True if self.health > 0 else False
        }

    def get_combat_stats(self) -> dict:
        return {
            'attack': self.attack_power,
            'health': self.health
        }
