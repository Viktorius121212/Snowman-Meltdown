"""Module for ship data analysis."""
from collections import Counter
from load_data import load_data


def main():
    """Main CLI function."""
    all_data = load_data()
    ships = all_data.get('data') or []

    while True:
        user_input = input("\n> ").strip().split()
        if not user_input:
            continue

        command = user_input[0].lower()
        args = user_input[1:]

        if command == "exit":
            break

        if command == "help":
            print("help - Liste der Befehle")
            print("show_countries - Alle Länder sortiert")
            print("top_countries <num> - Top Länder nach Schiffsanzahl")
            continue

        if command == "show_countries":
            countries = sorted(list(set(
                ship["COUNTRY"] for ship in ships if "COUNTRY" in ship
            )))
            for country in countries:
                print(country)
            continue

        if command == "top_countries":
            if args:
                try:
                    anzahl = int(args[0])
                    # Zeilenumbruch für Pylint Konformität
                    counts = Counter(
                        ship["COUNTRY"] for ship in ships if "COUNTRY" in ship
                    ).most_common(anzahl)
                    for country, count in counts:
                        print(f"{country}: {count}")
                except ValueError:
                    print("Fehler: Bitte gib eine gültige Zahl an.")
            else:
                print("Bitte gib eine Zahl an.")
            continue

        print(f"Unbekannter Befehl: {command}")


if __name__ == "__main__":
    main()
    