from ascii_art import STAGES
import random

# secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the snowman and the current state of the word."""
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: " + display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    # Start der Spielschleife
    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()
        valid_characters = "abcdefghijklmnopqrstuvwxyz"

        # Prüfung: Ist die Länge ungleich 1 ODER ist das Zeichen NICHT in der Liste?
        if len(guess) != 1 or guess not in valid_characters:
            print("Invalid input! Please enter a single letter from a-z.")
            continue

        # 1. Prüfen ob schon geraten
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue

        # zur Liste hinzufügen
        guessed_letters.append(guess)

        # 2. Prüfen ob Richtig oder Falsch
        if guess in secret_word:
            print(f"Correct! {guess} is in the word.")

            # Gewinn-Prüfung
            found_all = True
            for letter in secret_word:
                if letter not in guessed_letters:
                    found_all = False

            if found_all:
                print(f"You won! The word was {secret_word}!")
                print("The snowman is saved! ⛄")
                return  # Beendet die Funktion sofort (Spiel vorbei)

        else:
            # Das else muss GENAU unter dem if stehen!
            print(f"Sorry, {guess} is not in the word.")
            mistakes += 1

    # Wenn die while-Schleife vorbei ist (mistakes erreicht), dann Game Over
    if mistakes >= max_mistakes:
        print(STAGES[mistakes])
        print(f"Game Over! The word was {secret_word}!")


if __name__ == "__main__":
    while True:
        play_game()

        again = input("Willst du nochmal spielen? (j/n): ").lower()
        if again != "j":
            print("Danke fürs spielen! Tschüss.")
            break