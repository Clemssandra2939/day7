#   Step 3


import random
word_list = ["ardvark","baboon","camel"]
chosen_word =random.choice(word_list)
word_length =(len(chosen_word))


# Testing code
print(f"Psst,the solution is {chosen_word}")


Create blanks
display =[]
word_length =(len(chosen_word))   #length of the word from 0 t0 6 if the chosen word is baboon
for _ in range(word_length):
    display += "_"