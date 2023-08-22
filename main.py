import random
from art import hangman, stages
from words import words_list

# Display Game name
print(hangman)

# Game Constants
chosen_word = random.choice(words_list).lower()
word_length = len(chosen_word)
lives = 6

# Shows the Number of letters Present in the chosen word
display = []
wrong_letters_guessed = []
for _ in range(word_length):
    display.append("_")
print(f"{' '.join(display).upper()}")

# Game Logic
while "_" in display and lives > 0:
    guess = input("Guess A letter: ").lower()
    # If guess is wrong
    if guess not in chosen_word and guess not in wrong_letters_guessed:
        lives -= 1
        print(
            f"You guessed the letter {guess.upper()},  that's not in the word. You lose a life"
        )
        wrong_letters_guessed.append(guess)
    # Check if the letter has been guessed
    elif guess in display or guess in wrong_letters_guessed:
        print(f"You have already guessed {guess.upper()}")
    # If guess is in word and hasnt been guessed
    else:
        for n in range(word_length):
            if chosen_word[n] == guess:
                display[n] = guess
    # Show current letters guessed and hangman
    print(f"{' '.join(display).upper()}")
    print(stages[lives])
    # End game on game win
    if "_" not in display:
        print("GAME WON!")
    # End game on game loss
    if lives == 0:
        print("GAME LOST!")
        print(f"The Word was {chosen_word.upper()}")
