"""Module for ship data analysis using a dispatcher pattern."""
from collections import Counter
from load_data import load_data


def cmd_help(_ships, _args):
    """Print help message."""
    print("help - Liste der Befehle")
    print("show_countries - Alle Länder sortiert")
    print("top_countries <num> - Top Länder nach Schiffsanzahl")
    print("exit - Programm beenden")
    return True


def cmd_show_countries(ships, _args):
    """Show all unique countries."""
    countries = sorted(list(set(
        ship["COUNTRY"] for ship in ships if "COUNTRY" in ship
    )))
    for country in countries:
        print(country)
    return True


def cmd_top_countries(ships, args):
    """Show top countries by ship count."""
    if not args:
        print("Bitte gib eine Zahl an.")
        return True
    try:
        num = int(args[0])
        counts = Counter(
            ship["COUNTRY"] for ship in ships if "COUNTRY" in ship
        ).most_common(num)
        for country, count in counts:
            print(f"{country}: {count}")
    except ValueError:
        print("Fehler: Bitte gib eine gültige Zahl an.")
    return True


def cmd_exit(_ships, _args):
    """Exit the program."""
    return False


def cmd_unknown(_ships, _args):
    """Handle unknown commands."""
    print("Unbekannter Befehl. Tippe 'help' für eine Liste.")
    return True


def main():
    """Main CLI function with dispatcher pattern."""
    all_data = load_data()
    ships = all_data.get('data') or []

    dispatch = {
        "help": cmd_help,
        "show_countries": cmd_show_countries,
        "top_countries": cmd_top_countries,
        "exit": cmd_exit
    }

    while True:
        user_input = input("\n> ").strip().split()
        if not user_input:
            continue

        command = user_input[0].lower()
        args = user_input[1:]

        # Der Dispatcher ersetzt alle if-Abfragen zur Befehlssteuerung
        handler = dispatch.get(command, cmd_unknown)
        
        # Führt die Funktion aus. Wenn sie False zurückgibt, bricht die Schleife
        if not handler(ships, args):
            break


if __name__ == "__main__":
    main()
    