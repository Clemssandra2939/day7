#   Step 3


import random
word_list = ["ardvark","baboon","camel"]
chosen_word =random.choice(word_list)
word_length =(len(chosen_word))


# Testing code
print(f"Psst,the solution is {chosen_word}")


# Create blanks
display =[]
for _ in range(word_length):
    display += "_"

# TODO 1 - Use a while loop to let the user guess again,the loop should only
# stop once the user has guessed all the letters in the chosen_word and
#  'display' has no more blanks ("_").then yiu can tell the user they hv won


guess = input ("Guess a letter:").lower()

# Chek guessed letter
for position in range(word_length):
    letter = chosen_word [position]
    print(f"Current postion:{position}\n 
    Current letter :{letter}\n Guessed 
    letter: {guess}")
    if letter == guess: