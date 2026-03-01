from game_logic import play_game

if __name__ == "__main__":
    while True:
        play_game()

        again = input("Willst du nochmal spielen? (j/n): ").lower()
        if again != "j":
            print("Danke fürs spielen! Tschüss.")
            break