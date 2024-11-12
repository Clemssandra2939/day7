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
