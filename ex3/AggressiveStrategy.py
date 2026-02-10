from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """
    Implements an aggressive game strategy that prioritizes
    playing the first card and attacking enemies first.
    """
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        if not hand:
            return {
                "strategy": self.get_strategy_name(),
                "actions": {
                    "cards_played": [],
                    "mana_used": 0
                }
            }
        to_play = hand[0]
        play_result = to_play.play({})
        cards_played = [to_play.name]
        mana_used = play_result.get('mana_used', 0)
        if to_play.type.name == 'Creature':
            battlefield.append(to_play)
        targets = self.prioritize_targets(['Enemy'])
        damage = 0
        if battlefield:  # if there is somone in battlefield atack them
            for c in battlefield:
                if hasattr(c, "attack_power"):
                    damage += c.attack_power
        return {
            "strategy": self.get_strategy_name(),
            "actions": {
                "cards_played": cards_played,
                "mana_used": mana_used,
                "targets_attacked": targets[:1],
                "damage_dealt": damage,
            },
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        if "Enemy" in available_targets:
            return ["Enemy"] + [t for t in available_targets if t != "Enemy"]
        return available_targets
