from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
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
        if to_play.type == 'Creature':
            battlefield.append(to_play)
        targets = self.prioritize_targets(['Enemy'])
        damage = 0
        if battlefield:
            for c in battlefield:
                attack = getattr(c, "attack", None)
                if isinstance(attack, int):
                    damage += attack
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
