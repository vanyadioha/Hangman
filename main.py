import random

print(
    """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ 
"""
)

stages = [
    """
 _______
 |/    |
 |     O
 |    /|\\
 |    / \\
 |
 |___

""",
    """
 _______
 |/    |
 |     O
 |    /|\\
 |    / 
 |
 |___

""",
    """
 _______
 |/    |
 |     O
 |    /|\\
 |    
 |
 |___

""",
    """
 _______
 |/    |
 |     O
 |    /|
 |    
 |
 |___

""",
    """
 _______
 |/    |
 |     O
 |     |
 |    
 |
 |___

""",
    """
 _______
 |/    |
 |     O
 |    
 |    
 |
 |___

""",
    """
 _______
 |/    |
 |     
 |    
 |    
 |
 |___

""",
]

word_list = ["Drunk", "In", "Love"]
chosen_word = random.choice(word_list).lower()
word_length = len(chosen_word)
lives = 6

display = []
for _ in range(word_length):
    display.append("_")
print(display)

while "_" in display and lives > 0:
    guess = input("Guess A letter: ").lower()

    for n in range(word_length):
        if chosen_word[n] == guess:
            display[n] = guess

    if guess not in chosen_word:
        lives -= 1

    print(f"{' '.join(display).upper()}")
    print(stages[lives])

    if "_" not in display:
        print("Game Won!")
    if lives == 0:
        print("Game Lost")
