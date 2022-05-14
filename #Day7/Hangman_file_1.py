import imp


import random

word_list =["aardvark" , "baboon" , "camel"]
chosen_word =  random.choice(word_list)
print(chosen_word)


guess = input("Enter you guessed letter").lower()
print(guess)


for selected_letter in chosen_word:
    if selected_letter== guess:
        print("Right")
    else:
        print("Wrong")
    
