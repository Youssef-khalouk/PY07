from ex0.Card import Card, CardType
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """
    Represents a tournament card combining card, combat,
    and ranking features for gameplay and stats tracking.
    """

    def __init__(self, n: str, c: int, r: str, a: int, h: int, br: int = 1200):
        Card.__init__(self, n, c, r)
        Combatable.__init__(self, n, a, h)
        Rankable.__init__(self, br)
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

    def defend(self, incoming_damage: int) -> dict:
        result = super().defend(incoming_damage)
        blocked = min(self.attack_power, incoming_damage)
        result["damage_taken"] = incoming_damage - blocked
        result["damage_blocked"] = blocked
        return result

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
