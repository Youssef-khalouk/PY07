from abc import ABC, abstractmethod
from enum import Enum
from ex0.Card import Card


class EnumAPI:

    @classmethod
    def get_values(cls) -> dict[str, list[str]]:
        return {cls.__name__: [member.value for member in cls]}


class Rarity(EnumAPI, Enum):
    COMMON = "common"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"


class SpellsType(EnumAPI, Enum):
    FIREBALL = "Fireball"
    LIGHTNING_BOLT = "Lightning bolt"
    DOOM = "Doom"
    ICE = "Ice"


class CreaturesType(EnumAPI, Enum):
    GOBLIN = "Goblin"
    DRAGON = "Dragon"
    PEKKA = "Pekka"
    WIZARD = "Wizard"
    DOOM = "Doom"
    AXE = "Axe"
    ANTI_MAGE = "Anti mage"


class ArtifactsType(EnumAPI, Enum):
    BLACK_KING_BAR = "Black King Bar"
    SATANIC = "Satanic"
    BLINK_DAGGER = "Blink Dagger"
    BOTTLE = "Bottle"
    DIVINE_RAPIER = "Divine Rapier"
    HEART_OF_TARRASQUE = "Heart of Tarrasque"
    ARCANE_RING = "Arcane ring"


class CreaturesStats(EnumAPI, Enum):
    """Enum containing statistics for different creatures."""
    DRAGON = (CreaturesType.DRAGON.value, 5, Rarity.LEGENDARY.value, 3, 10)
    GOBLIN = (CreaturesType.GOBLIN.value, 2, Rarity.COMMON.value, 2, 5)
    PEKKA = (CreaturesType.PEKKA.value, 4, Rarity.RARE.value, 4, 8)
    DOOM = (CreaturesType.DOOM.value, 6, Rarity.EPIC.value, 5, 9)
    AXE = (CreaturesType.AXE.value, 1, Rarity.COMMON.value, 1, 4)
    ANTI_MAGE = (CreaturesType.ANTI_MAGE.value, 3, Rarity.RARE.value, 2, 6)

    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ) -> None:
        self.card_name: str = name
        self.cost: int = cost
        self.rarity: str = rarity
        self.attack: int = attack
        self.health: int = health


class SpellsStats(EnumAPI, Enum):
    FIREBALL = (SpellsType.FIREBALL.value, 5, Rarity.RARE.value, "Causes fire")
    LIGHTNING_BOLT = (
        SpellsType.LIGHTNING_BOLT.value,
        4,
        Rarity.EPIC.value,
        "Zeus is on rage!",
    )
    DOOM = (
        SpellsType.DOOM.value,
        10,
        Rarity.LEGENDARY.value,
        "DooooooooOOOOOOOOOO0OOOOOOM!",
    )
    ICE = (
        SpellsType.ICE.value,
        3,
        Rarity.RARE.value,
        "FROOOOOOOOOOOOOOOOOOOOST!",
    )

    def __init__(
        self, name: str, cost: int, rarity: str, effect_type: str
    ) -> None:
        self.card_name: str = name
        self.cost: int = cost
        self.rarity: str = rarity
        self.effect_type: str = effect_type


class ArtifactStats(EnumAPI, Enum):
    BLACK_KING_BAR = (
        ArtifactsType.BLACK_KING_BAR.value,
        4,
        Rarity.EPIC.value,
        3,
        "Gain Magic Immunity and dispel negative effects",
    )

    SATANIC = (
        ArtifactsType.SATANIC.value,
        6,
        Rarity.LEGENDARY.value,
        2,
        "Gain 200% Lifesteal on attacks",
    )

    BLINK_DAGGER = (
        ArtifactsType.BLINK_DAGGER.value,
        3,
        Rarity.RARE.value,
        5,
        "Teleport to any location on the battlefield",
    )

    BOTTLE = (
        ArtifactsType.BOTTLE.value,
        1,
        Rarity.COMMON.value,
        3,
        "Restore 5 Health and Mana",
    )

    DIVINE_RAPIER = (
        ArtifactsType.DIVINE_RAPIER.value,
        10,
        Rarity.LEGENDARY.value,
        1,
        "Deal +300 damage. Drops to enemy if destroyed.",
    )

    HEART_OF_TARRASQUE = (
        ArtifactsType.HEART_OF_TARRASQUE.value,
        7,
        Rarity.EPIC.value,
        10,
        "Regenerate 5% max health per turn",
    )

    ARCANE_RING = (
        ArtifactsType.ARCANE_RING.value,
        1,
        Rarity.COMMON.value,
        2,
        "Regenerate 5 mana every 60s",
    )

    def __init__(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ) -> None:
        self.card_name: str = name
        self.cost: int = cost
        self.rarity: str = rarity
        self.effect: str = effect
        self.durability: int = durability


class CardFactory(ABC):

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:

        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        pass
