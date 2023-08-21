import random
import art
from words import words_list

print(art.hangman)


chosen_word = random.choice(words_list).lower()
word_length = len(chosen_word)
lives = 6

display = []
for _ in range(word_length):
    display.append("_")
print(f"{' '.join(display).upper()}")

while "_" in display and lives > 0:
    guess = input("Guess A letter: ").lower()

    for n in range(word_length):
        if chosen_word[n] == guess:
            display[n] = guess

    if guess not in chosen_word:
        lives -= 1

    print(f"{' '.join(display).upper()}")
    print(art.stages[lives])

    if "_" not in display:
        print("GAME WON!")
    if lives == 0:
        print("GAME LOST!")
