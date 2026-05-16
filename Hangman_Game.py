import random

# ─────────────────────────────────────────────
#  Hangman Game — CodeAlpha Python Internship
#  Task 1
# ─────────────────────────────────────────────

WORDS = ["python", "rocket", "jungle", "castle", "wizard"]

HANGMAN_STAGES = [
    # 0 wrong guesses
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    # 1
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    # 2
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    # 3
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    # 4
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    # 5
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    # 6 — dead
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
]


def display_state(wrong_guesses: int, guessed_letters: set, word: str) -> None:
    """Print the gallows, current word progress, and guessed letters."""
    print(HANGMAN_STAGES[wrong_guesses])
    print()

    # Show word with blanks
    display_word = " ".join(
        letter if letter in guessed_letters else "_" for letter in word
    )
    print(f"  Word: {display_word}")
    print(f"  Wrong guesses left: {6 - wrong_guesses}")

    wrong_letters = sorted(guessed_letters - set(word))
    if wrong_letters:
        print(f"  Wrong letters: {', '.join(wrong_letters)}")
    print()


def get_guess(guessed_letters: set) -> str:
    """Prompt the player for a valid, not-yet-guessed letter."""
    while True:
        guess = input("  Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("  ⚠  Please enter a single letter.")
        elif guess in guessed_letters:
            print(f"  ⚠  You already guessed '{guess}'. Try another.")
        else:
            return guess


def play_game() -> None:
    """Run one full round of Hangman."""
    word = random.choice(WORDS)
    guessed_letters: set = set()
    wrong_guesses = 0
    max_wrong = 6

    print("\n" + "=" * 40)
    print("        W E L C O M E  T O  H A N G M A N")
    print("=" * 40)
    print(f"  The word has {len(word)} letters. Good luck!\n")

    while wrong_guesses < max_wrong:
        display_state(wrong_guesses, guessed_letters, word)

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print(f"  🎉 You won! The word was '{word.upper()}'.")
            return

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"  ✅ '{guess}' is in the word!\n")
        else:
            wrong_guesses += 1
            print(f"  ❌ '{guess}' is NOT in the word.\n")

    # Ran out of guesses
    print(HANGMAN_STAGES[max_wrong])
    print(f"\n  💀 Game over! The word was '{word.upper()}'.")


def main() -> None:
    while True:
        play_game()
        print()
        again = input("  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing! Goodbye. 👋\n")
            break


if __name__ == "__main__":
    main()