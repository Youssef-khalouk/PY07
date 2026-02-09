#!/usr/bin/env python3
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import MegaSuperEngine


def main() -> None:
    """Execute the main demonstration of the Game Engine."""
    try:
        print()
        print("=== DataDeck Game Engine ===")
        print()
        print("Configuring Fantasy Card Game...")
        strategy: AggressiveStrategy = AggressiveStrategy()
        factory: FantasyCardFactory = FantasyCardFactory()
        engine: MegaSuperEngine = MegaSuperEngine()
        engine.configure_engine(factory, strategy)
        print("Available types:", factory.get_supported_types())
        print()
        print("Simulating aggressive turn...")
        engine.simulate_turn()
        print()
        print("Game Report:")
        print(engine.get_engine_status())
        print()
        print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
