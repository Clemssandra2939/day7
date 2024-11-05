# Step 1

word_list = ["ardvark","baboon","camel"]

# TODO- 1 - Randomly choose a word_list
#  and assign it  to a variable  called chosen_word

import random
chosen_word =random.choice(word_list)

# TODO- 2 - Ask the user to gues a letter and assign their answer
#  to a variable called guess.Make guess lowercase
#  
guess =input("Guess a letter:").lower()

# TODO- 3 - Check if the letter the user guessed(guess)
# is one of the letters in the chosen_word
#   
for letter in chosen_word:
    if letter == guess:
        print("Right,in the blank!!")
    else:
        print("Wrong,Not in the blank!!")
# Generate a random word eg if the word is Mouse

# Generate as many blanks as letters in word... That is -_ _ _ _ _ that is wat the user will see

# Ask the user to guess a letter
#     is  the guessed letter in the word

# If Yes ...Replace the blank with the letter
    
# if No... Lose a life