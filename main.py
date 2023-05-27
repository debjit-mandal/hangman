import random

# List of words for the game

words = ['apple', 'banana', 'orange', 'mango', 'strawberry', 'grape', 'watermelon']

def hangman():

    # Select a random word from the list

    word = random.choice(words)

    guessed_letters = []

    attempts = 6

    

    print("Welcome to Hangman!")

    

    while True:

        # Display the current status of the word

        display_word(word, guessed_letters)

        

        # Get a letter from the player

        letter = input("Guess a letter: ").lower()

        

        # Check if the letter has already been guessed

        if letter in guessed_letters:

            print("You have already guessed that letter.")

            continue

        

        # Add the letter to the guessed letters list

        guessed_letters.append(letter)

        

        # Check if the letter is in the word

        if letter in word:

            print("Correct guess!")

        else:

            print("Wrong guess!")

            attempts -= 1

        

        # Check if the player has won or lost

        if all(letter in guessed_letters for letter in word):

            print("Congratulations! You won!")

            break

        elif attempts == 0:

            print("Game over. You lost!")

            print("The word was:", word)

            break

        

        print("Attempts remaining:", attempts)

        print()

    

def display_word(word, guessed_letters):

    # Display the word with underscores for unguessed letters

    displayed_word = ''

    for letter in word:

        if letter in guessed_letters:

            displayed_word += letter

        else:

            displayed_word += '_'

    print(displayed_word)

# Start the game

hangman()

