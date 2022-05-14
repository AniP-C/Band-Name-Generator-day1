import random
from Hangman_art_file import stages
from Hangman_words_list import word_list

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

print(f'the solution is {chosen_word}')

display = []

for letter in range (word_length):
    display += "_"

while not end_of_game :
    guess = input("Guess a letter: ").lower()

    for position in range (word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position]= letter
    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0 :
            end_of_game=True
            print("you lose")

    print(f"{' '.join(display)}")

    if "_"  not in display:
        end_of_game=True
        print("you win")
    
    print(stages[lives])
        