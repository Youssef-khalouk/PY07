from ex3 import GameEngine, FantasyCardFactory, AggressiveStrategy


if __name__ == "__main__":
    print("=== DataDeck Game Engine ===")

    engine = GameEngine()
    print("\nConfiguring Fantasy Card Game...")
    factory = FantasyCardFactory()
    print("Factory: FantasyCardFactory")
    strategy = AggressiveStrategy()
    print("Strategy: AggressiveStrategy")
    engine.configure_engine(factory, strategy)
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    print("Hand:", [f"{c.name} ({c.cost})" for c in engine.hand])

    turn = engine.simulate_turn()
    print("Turn execution:")
    print(f"Strategy: {turn['strategy']}")
    print(f"Actions: {turn['actions']}")

    print(f"\nGame Report: {engine.get_engine_status()}")

    print()
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")
