import random

# List of words for the game
WORDS = ["apple", "banana", "orange", "strawberry", "grape", "pineapple", "watermelon"]

def choose_word(words):
    """
    Randomly choose a word from the list.
    """
    return random.choice(words)

def display_word(word, guessed_letters):
    """
    Display the word with guessed letters revealed and others hidden.
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def get_guess():
    """
    Get a letter guess from the player.
    """
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid input! Please enter a single letter.")

def play_game(word):
    """
    Main game loop.
    """
    print("Welcome to Guess the Word!")
    print("Try to guess the word within 6 attempts.")

    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts left:", attempts)
        
        guess = get_guess()

        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            print("Correct guess!")
            guessed_letters.append(guess)
            if set(guessed_letters) == set(word):
                print("Congratulations! You guessed the word:", word)
                break
        else:
            print("Incorrect guess!")
            attempts -= 1

    if attempts == 0:
        print("Sorry, you ran out of attempts. The word was:", word)

if __name__ == "__main__":
    word = choose_word(WORDS)
    play_game(word)