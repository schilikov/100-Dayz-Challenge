import random
from hangman_words import word_list
from hangman_art import logo, stages

# Printing the main logo of the game
print(logo)

# Choosing a random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Setting some booleans
end_of_game = False
lives = 6

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed
    if guess in display:
        print(f"You've already guessed {guess}")

    # Checking guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        # If the letter is not in the chosen_word
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        # If lives drop to zero, the game is over.
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Printing the list in a string form
    print(f"{' '.join(display)}")

    # Checking if the user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
