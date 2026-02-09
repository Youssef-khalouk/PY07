from ex0.Card import Card
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Strategy implementation focusing on aggressive play."""

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        total_mana: int = sum(card.cost for card in hand)

        prioritize_targets: list[Card] = self.prioritize_targets(battlefield)

        if not prioritize_targets:
            total_damage: int = 0
            prioritize_targets: list[Card] = ["No targets to be attacked!"]
        else:
            total_damage: int = sum(
                card.attack for card in hand if hasattr(card, "attack")
            )

        pretty_targets: list[str] = [
            getattr(target, "name", str(target))
            for target in prioritize_targets
        ]
        return {
            "cards_played": [card.name for card in hand],
            "mana": total_mana,
            "damage_dealt": total_damage,
            "targets_attacked": pretty_targets,
        }

    def get_strategy_name(self) -> str:
        """Retrieve the name of the strategy.

        Returns:
            str: The class name as the strategy name.
        """
        return self.__class__.__name__

    def prioritize_targets(self, available_targets: list) -> list:
        """Prioritize targets with the lowest health.

        Args:
            available_targets (list): List of potential targets.

        Returns:
            list: Targets sorted by health (ascending).
        """
        valid_targets: list[Card] = [
            target for target in available_targets if hasattr(target, "health")
        ]

        return sorted(valid_targets, key=lambda target: target.health)
