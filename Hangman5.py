# Step 5

import random
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
# TODO - 1 : - Update the word list to use the 'word_list'from hangman_word.py
# Delete this line:word_list = ["ardvark","baboon","camel"]
chosen_word =random.choice(word_list)
word_length =len(chosen_word)

Game_Over = True
lives = 6

# TODO - 3 : - import the logo from hangmana- ar.py and print it at the start of the game.

# Testing code
print(f"Psst,the solution is {chosen_word}") 

# Create blanks
display =[]
for _ in range(word_length):
    display += "_"

    
word_list = ["abandoned",
            "aberdeen",
             "abilities",
             "ability",
             "able",
             "aboriginal",
             "abortion",
             "about",
             "above",
             "abraham",
             "abroad",
             "absence",
             "absent",
             "absolute",
             "absolutely",
             "absorption",
             "abstract",
             "abstracts",
             "abuse",
             "academic",
             "academics",
             "academy",
             "accent",
             "accept",
             "acceptable",
             "acceptance",
             "accepted",
             "accepting",
             "accepts",
             "access",
             "accessed",
             "accessibility",
             "accessible",
             "accessing",
             "accessories",
             "accessory",
             "accident",
             "accidents",
             "believes",
             "belize",
             "belkin",
             "bell",
             "belle",
             "belly",
             "belong",
             "belongs",
             "below",
             "belt",
             "belts",
             "ben",
             "bench",
             "benchmark",
             "bend",
             "beneath",
             "beneficial",
             "benefit",
             "benefits",
             "benjamin",
             "bennett",
             "benz",
             "berkeley",
             "berlin",
             "bermuda",
             "bernard",
             "berry",
             "beside",
             "besides",
             "best",
             "bestiality",
             "bestsellers",
             "corrected",
             "correction",
             "corrections",
             "correctly",
             "correlation",
             "correspondence",
             "corresponding",
             "corruption",
             "cos",
             "cosmetic",
             "cosmetics",
             "cost",
             "costa",
             "costs",
             "costume",
             "costumes",
             "cottage",
             "cottages",
             "cotton",
             "could",
             "council",
             "councils",
             "counsel"
             "hearings",
             "heart",
             "hearts",
             "heat",
             "heated",
             "heater",
             "heath",
             "heather",
             "heating",
             "heaven",
             "heavily",
             "heavy",
             "hebrew",
             "heel",
             "height",
             "heights",
             "held",
             "helen",
             "helena",
             "helicopter",
             "modify",
             "mods",
             "modular",
             "module",
             "modules",
             "moisture",
             "mold",
             "moldova",
             "molecular",
             "molecules",
             "mom",
             "moment",
             "moments",
             "momentum",
             "moms",
             "mon",
             "monaco"
             ]
