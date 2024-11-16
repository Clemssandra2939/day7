# Step 5
# Try modules and how to do import
import random
print(hangman_art.logo)
# TODO - 1 : - Update the word list to use the 'word_list'from hangman_word.py

from hangman_words import word_list
chosen_word =random.choice(word_list)
word_length =len(chosen_word)



Game_Over = False
lives = 6

# TODO - 3 : - import the logo from hangman- art.py and print it at the start of the game.
from hngman_art import logo
print

# Testing code
print(f"Psst,the solution is {chosen_word}") 

# Create blanks
display =[]
for _ in range(word_length):
    display += "_"


while not Game_Over :
    guess = input ("Guess a letter:").lower()

    # TODO - 4 : - If the user has entered a letter they have already guessed,print the letter and let them know.
    print(f"You have already guessed{letter}")
 # Check guessed letter

    for position in range(word_length):
        letter = chosen_word [position]
        # print(f"Current postion:{position}\n Current letter :{letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
        
    # Check if user is wrong.
    if guess not in chosen_word:
        # TODO - 5 : - If the letter is not in the chosen_word,print out the letter and let them know it's not in the word
         print (f"You guessed {letter},that's not in the word.You lose a life")
         lives -= 1
         if lives == 0:
                Game_Over = True
                print("You lose!!")
     
    # Join all the element in the list and turn it into a String.
    print(f"{' '.join(display)}")


    # Check if user has got all letters.
    if "_"  not in display:
        Game_Over = True
        print("You Win!!")

    # TODO - 2 : - import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages[lives])
   


