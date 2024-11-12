# Step 4

logo = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""

stages = ['''

 _______
 |/    |
 |     0
 |    <|>
 |     |
 |    / !
 |
_|___''', '''

 _______
 |/    |
 |     0
 |    <|>
 |     |
 |    / 
 |
_|___''', '''

 _______
 |/    |
 |     0
 |    <|>
 |     |
 |    
 |
_|___''', '''

 _______
 |/    | 
 |     0
 |    <|
 |     
 |    
 |
_|___''', '''

 _______
 |/    |
 |     0
 |    
 |     
 |    
 |
_|___''', '''

 _______
 |/    |
 |     
 |    
 |     
 |    
 |
_|___''']


import random
word_list = ["ardvark","baboon","camel"]
chosen_word =random.choice(word_list)
word_length =(len(chosen_word))

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6

# Testing code
print(f"Psst,the solution is {chosen_word}") 

# Create blanks
display =[]
for _ in range(word_length):
    display += "_"


Game_Over = False
while not Game_Over :
    guess = input ("Guess a letter:").lower()

    # Check guessed letter

    for position in range(word_length):
        letter = chosen_word [position]
        # print(f"Current postion:{position}\n Current letter :{letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

# TODO- 2: - If guess is not a letter in the chosen_word.then reduce "lives" by 1.
# if lives goes down to 0 then the gamw should stop and it should print "You lose"


# Join all the element in the list and turn it into a String.
print(f"{''.join(display)}")


# Check if user has got all letters.
if "_"  not in display:
        Game_Over = True
        print("You Win!!")

TODO -3- Print the ASCII art from 'stages'that corresponds to the current number of 'lives' the user has remaining