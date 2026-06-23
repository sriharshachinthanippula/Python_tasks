import random

WORDS = ["python", "rocket", "jungle", "bridge", "planet"]

HANGMAN_STAGES = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""
]

def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("\n=============================")
    print("       HANGMAN GAME")
    print("=============================")
    print("Guess the word! You have 6 incorrect guesses.\n")

    while incorrect_guesses < max_incorrect:
        print(HANGMAN_STAGES[incorrect_guesses])
        display_word = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in word
        )
        print(f"\nWord: {display_word}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")

        if all(letter in guessed_letters for letter in word):
            print(f"\n🎉 You WIN! The word was: {word.upper()}")
            break

        guess = input("\nEnter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠ Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"⚠ You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"✅ '{guess}' is in the word!")
        else:
            incorrect_guesses += 1
            print(f"❌ '{guess}' is NOT in the word!")

    else:
        print(HANGMAN_STAGES[max_incorrect])
        print(f"\n💀 Game Over! The word was: {word.upper()}")

    play_again = input("\nPlay again? (yes/no): ").strip().lower()
    if play_again == "yes":
        play_hangman()
    else:
        print("Thanks for playing! Goodbye! 👋")

if __name__ == "__main__":
    play_hangman()
