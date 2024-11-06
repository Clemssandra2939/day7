# Step 2


import random
word_list = ["ardvark","baboon","camel"]
chosen_word =random.choice(word_list)

# Testing code
print(f"Psst,the solution is {chosen_word}")

# TODO-1: - Create an empty list called display.
# For each letter in the chosen_word,add s "_" to 'display'.
# So if the chosen_word was "apple",display should be 
# ["_" "_" "_" "_" "_"] with 5 "_" representing each letter to guess

guess =input("Guess a letter:").lower()

# # TODO-2: - Loop through each postion in the chosen_word:
# if the letter at that postion matches 'guess' then reveal that letter 
# in the display at that position.
# e.g. if the user guessed "p" and the chosen_word was "apple",
# then display should be ["_","p","p", "_", "_"].

for letter in chosen_word:
    if letter == guess:
        print("Right,in the blank!!")
    else:
        print("Wrong,Not in the blank!!")

# TODO-3: -Print "display" and you should see the guessed letter in 
# the correct potion and every other letter replace with "_"
# Hint - Don't worry about getting the user to guess the next letter,
# We will tackle that in step 3.

display = []


