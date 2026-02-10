from ex4.TournamentCard import TournamentCard
import random


class TournamentPlatform():
    """
    Manages tournament cards, matches, and leaderboards,
    tracking ratings and match outcomes.
    """

    def __init__(self):
        self._cards: dict[str, TournamentCard] = {}
        self._matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        name = card.name.lower().replace(' ', '_')
        card_id = f"{name}_{len(self._cards)+1:03d}"
        self._cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id not in self._cards or card2_id not in self._cards:
            raise KeyError("card id not found")
        if card1_id == card2_id:
            raise ValueError("cannot match a card against itself")
        c1 = self._cards[card1_id]
        c2 = self._cards[card2_id]
        self._matches_played += 1
        r1 = c1.calculate_rating()
        r2 = c2.calculate_rating()
        p1_score = r1 + c1.attack_power * 10 + random.randint(-25, 25)
        p2_score = r2 + c2.attack_power * 10 + random.randint(-25, 25)
        if p1_score >= p2_score:
            winner_id, loser_id = card1_id, card2_id
        else:
            winner_id, loser_id = card2_id, card1_id
        winner = self._cards[winner_id]
        loser = self._cards[loser_id]
        winner.update_wins(1)
        loser.update_losses(1)
        winner._rating += 16
        loser._rating -= 16
        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }

    def get_leaderboard(self) -> list:
        items = []
        for card_id, card in self._cards.items():
            info = card.get_rank_info()
            rating = info["rating"]
            wins = info["wins"]
            losses = info["losses"]
            items.append((card_id, card.name, rating, wins, losses))
        items.sort(key=lambda x: x[2], reverse=True)
        return items

    def generate_tournament_report(self) -> dict:
        total = len(self._cards)
        average = 0
        if total:
            s = sum(c.calculate_rating() for c in self._cards.values())
            average = int(round(s / total))
        return {
            "total_cards": total,
            "matches_played": self._matches_played,
            "avg_rating": average,
            "platform_status": "active" if total else "empty",
        }
