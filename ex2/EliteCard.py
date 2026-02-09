from ex0.Card import Card
from ex2.Magical import Magical
from ex2.Combatable import Combatable
from enum import Enum


class EnumAPI:
    """Mixin class to provide API-like access to Enum values."""

    @classmethod
    def get_values(cls) -> dict[str, list[str]]:
        """Retrieve all values of the enum.

        Returns:
            dict[str, list[str]]: A dictionary with the class name and values.
        """
        return {cls.__name__: [member.value for member in cls]}


class Rarity(EnumAPI, Enum):
    """Enum representing card rarity levels."""
    COMMON = "common"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"


class CombatType(EnumAPI, Enum):
    """Enum representing different combat types."""
    MELEE = "melee"
    RANGED = "ranged"
    MAGIC = "magic"


class SpellsType(EnumAPI, Enum):
    """Enum representing available spell types."""
    FIREBALL = "Fireball"
    LIGHTNING_BOLT = "Lightning bolt"
    DOOM = "Doom"
    ICE = "Ice"


class EliteCard(Card, Combatable, Magical):
    SPELL_COSTS: dict[str, int] = {
        SpellsType.FIREBALL.value: 4,
        SpellsType.LIGHTNING_BOLT.value: 3,
        SpellsType.DOOM.value: 10,
    }

    DEFENSE_REDUCTION: float = 0.40

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        damage: int,
        health: int,
        combat_type: str,
    ) -> None:
        try:
            Rarity(rarity)
        except ValueError:
            raise ValueError(f"Invalid rarity: {rarity}")

        try:
            CombatType(combat_type)
        except ValueError:
            raise ValueError(f"Invalid combat_type: {combat_type}")
        super().__init__(name, cost, rarity)
        if health <= 0 or damage < 0 or cost < 0:
            raise ValueError("Invalid card stats")
        self.combat_type: str = combat_type
        self.damage: int = damage
        self.health: int = health
        self.total_mana: int = 10

    def play(self, game_state: dict) -> dict:
        return game_state | {
            "card_played": self.name,
            "mana_used": self.cost,
        }

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.damage,
            "combat_type": self.combat_type,
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_taken: int = int(incoming_damage * self.DEFENSE_REDUCTION)
        damage_blocked: int = incoming_damage - damage_taken
        self.health -= damage_taken
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict:
        return {"combat_type": self.combat_type, "damage": self.damage}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        clean_name = spell_name.title()

        if clean_name not in self.SPELL_COSTS:
            raise ValueError(f"Unknown spell: '{spell_name}'")

        spell_cost = self.SPELL_COSTS[clean_name]

        if spell_cost > self.total_mana:
            raise ValueError(
                "Can't cast spell, no mana left "
                + f"(Required: {spell_cost}, Has: {self.total_mana})"
            )

        self.total_mana -= spell_cost
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": spell_cost,
        }

    def channel_mana(self, amount: int) -> dict:
        if amount < 0:
            raise ValueError(f"Can't channel negative amount of mana {amount}")
        self.total_mana += amount
        return {"channeled": amount, "total_mana": self.total_mana}

    def get_magic_stats(self) -> dict:
        return {"total_mana": self.total_mana}
