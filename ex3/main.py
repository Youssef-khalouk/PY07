from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main() -> None:
    """
    Demonstrates the GameEngine using a FantasyCardFactory
    and AggressiveStrategy to simulate a game turn.
    """

    print("\n=== DataDeck Game Engine ===")

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

    try:
        turn = engine.simulate_turn()
    except Exception as e:
        print("Error:", e)
        return
    print("Turn execution:")
    print(f"Strategy: {turn['strategy']}")
    print(f"Actions: {turn['actions']}")

    print(f"\nGame Report: {engine.get_engine_status()}")

    print()
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
