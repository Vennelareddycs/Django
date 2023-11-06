stages = [
    '''
    +___+
    |   |
    0   |
   /|\  |
   / \  |
        |
===========
    ''', '''
    +___+
    |   |
    0   |
   /|\  |
   /    |
        |
==========
    ''','''
    +___+
    |   |
    0   |
   /|\  |
        |
        |
==========
    ''','''
    +___+
    |   |
    0   |
   /|   |
        |
        |
==========
    ''','''
    +___+
    |   |
    0   |
    |   |
        |
        |
==========
    ''','''
    +___+
    |   |
    0   |
        |
        |
        |
==========
    ''','''
    +___+
    |   |
        |
        |
        |
        |
==========
    '''
]

word_list= ["python", "camel","apple", "letter"]

import random
chosen_word = random.choice(word_list)

lives = 6
print(f'the solution is {chosen_word}.')

display = []
for letter in range(len(chosen_word)):
    display+= "_"
print(display)

end_of_game = False

while not end_of_game:
    guess =input("Guess a letter").lower()

    for position in range(len(chosen_word)):
        letter= chosen_word[position]
        if letter == guess:
            display[position]= letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(display)
    #print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")

    print(stages[lives])