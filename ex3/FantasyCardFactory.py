from typing import Any
import random

from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex2.EliteCard import SpellsType
from ex3.CardFactory import (
    ArtifactsType,
    CardFactory,
    SpellsStats,
    CreaturesStats,
    ArtifactStats,
    CreaturesType,
)


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:

        key: str = str(name_or_power).upper().replace(" ", "_")

        if key in CreaturesStats.__members__:
            stats: CreaturesStats = CreaturesStats[key]

            return CreatureCard(
                name=stats.card_name,
                cost=stats.cost,
                rarity=stats.rarity,
                attack=stats.attack,
                health=stats.health,
            )

        raise ValueError(f"Unknown creature: {name_or_power}")

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        key: str = str(name_or_power).upper().replace(" ", "_")

        if key in SpellsStats.__members__:
            stats: SpellsStats = SpellsStats[key]

            return SpellCard(
                name=stats.card_name,
                cost=stats.cost,
                rarity=stats.rarity,
                effect_type=stats.effect_type,
            )

        raise ValueError(f"Unknown spell: {name_or_power}")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        key: str = str(name_or_power).upper().replace(" ", "_")

        if key in ArtifactStats.__members__:
            stats: ArtifactStats = ArtifactStats[key]

            return ArtifactCard(
                name=stats.card_name,
                cost=stats.cost,
                rarity=stats.rarity,
                durability=stats.durability,
                effect=stats.effect,
            )

        raise ValueError(f"Unknown artifact: {name_or_power}")

    def get_supported_types(self) -> dict:
        return (
            CreaturesType.get_values()
            | SpellsType.get_values()
            | ArtifactsType.get_values()
        )

    def create_themed_deck(self, size: int) -> dict:
        new_deck: Deck = Deck()
        options = [
            (self.create_creature, CreaturesType),
            (self.create_spell, SpellsType),
            (self.create_artifact, ArtifactsType),
        ]
        for _ in range(size):
            method, source_enum = random.choice(seq=options)
            random_blueprint: Any = random.choice(seq=list[Any](source_enum))
            card: Card = method(name_or_power=random_blueprint.value)
            new_deck.add_card(card)
        return new_deck
