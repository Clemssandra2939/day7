# Google for Education :Python
#  Use of List
#  colors = ['red', 'blue', 'green']
# # print(colors[0])    ## red
# # print(colors[2])    ## green
# # print(len(colors))  ## 3

# For and In statement loop
# squares = [1, 4, 9, 16]
# sum = 0
# for num in squares:
#     sum += num
# print(sum)  ## 30



# Range
   ## print the numbers from 0 through 99
# for i in range(100):
#     print(i) ###count from one to 100 in a single line

# While Loop
  ## Access every 3rd element in a list
# i = 0
# while i < len(a):
#     print(a[i])
#     i = i + 3


# List Methods
# Here are some other common list methods.

# list.append(elem) -- adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
# list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
# list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
# list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
# list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)
# list.sort() -- sorts the list in place (does not return it). (The sorted() function shown later is preferred.)
# list.reverse() -- reverses the list in place (does not return it)
# list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).
# Notice that these are *methods* on a list object, while len() is a function that takes the list (or string or whatever) as an argument


# list = ['larry', 'curly', 'moe']
# list.append('shemp')         ## append elem at end
# list.insert(0, 'xxx')        ## insert elem at index 0
# list.extend(['yyy', 'zzz'])  ## add list of elems at end

# print(list)  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
# print(list.index('curly'))    ## 2

# list.remove('curly')         ## search and remove that element
# list.pop(1)                  ## removes and returns 'larry'
# print(list)  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']





# ## ROck,Paper,Scissor
# import random
# Rock =''' 
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# Paper ='''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# Scissor = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# gaming_images =[Rock,Paper,Scissor]


# my_choice=int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors:\n"))

# print(gaming_images[my_choice])

# computer_choicee=random.randint(0,2)
# print("Computer`s choice is:")

# print(gaming_images[computer_choicee])


# if my_choice >= 3 or my_choice < 0:
#     print("You added an invalid number! Try again")
# elif my_choice == 0 and computer_choicee == 2:
#     print("You win!")
# elif computer_choicee == 0 and my_choice == 2:
#     print("You lose!")
# elif computer_choicee > my_choice:
#     print("You lose!")
# elif my_choice > computer_choicee:
#     print("You win!")
# elif my_choice == computer_choicee:
#     print("it is a draw!")



    # Who is paying coding char
import random
test_seed =int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names,separated by a comma:")
names = namesAsCSV.split(",")

# Get the total number of items in list
num_items= len(names)
# generate random number between 0 and the last number
random_names =random.randint(0,num_items - 1)
person_who_will_pay =names[random_names]

print(person_who_will_pay +"  is going to buy the meal today!")



# #        Hurdle 4 before the maze
# def turn_right():
#    turn_left()
#    turn_left()
#    turn_left()

# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
       
# while  not at_goal():
#     if wall_in_front(): 
#         jump()   
#     else:
#         move()


# maze char

#  def turn_right():
#    turn_left()
#    turn_left()
#    turn_left()

# while not at_goal():
#     if right_is_clear() :
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
        
# # Flowchart Progamming for the hangman progarm

# Start 

# Generate a random word eg if the word is Mouse

# Generate as many blanks as letters in word... That is -_ _ _ _ _ that is wat the user will see

# Ask the user to guess a letter
#     is  the guessed letter in the word

# If Yes ...Replace the blank with the letter
    
# if No... Lose a life

# ~~If Yes is the answer to the previous question
# Check if:
# All of the blanks filled and Have they run out of lives?
#  Then Game Over 

# if No then the loop will keep running till it crashes or Game Over 



# print("Welcome to Python Pizza Deliveries! ")
# size=input("what size pizza do you want? small,medium or large ")
# bill=0

# if size == "small":
#     bill=+15
#     print(f"pay ${bill}")

# elif size == "medium":
#     bill=+20
#     print(f"pay ${bill}")
# else:
#     bill=+25
#     print(f"pay ${bill}")
# 
# add_pepperoni=input("do u want pepperoni? Yes or No ")
# if add_pepperoni=="Yes":
#         if size =="small":
#             bill+=2
#         else:
#             bill+=3
            
# extra_cheese= input("do u want extra cheese? Yes or No ")
# if extra_cheese=="Yes":
#                 bill +=1
                
#                 print(f"Your final bill is ${bill}")
# 
# 
#  # Logical operator
# having diferent conditions in the same line 
# if condition1 &c condition2 & condition3:
#     do A
#     else:
#   do B

# And,or,not is really useful when it comes to logical operator
# "And"operator
# (A and B) means that both A and B for the entire line of code should be True
# if one of them is False,the overall thing will be False

# "Or"operator
# (A or B) means that if a A or B condition is True or if thet are both True
# when both condition is False then it is False

# "Not" operator
# it reverses a condition...so if a condition is True,then it becomes False
# if it`s` False,then it is True


#Roller coaster program
print("welcome to the rollercoaster!")
height=int(input("what is ur height in cm? "))
bill=0

if height >= 120:
    print("u can ride the rollercoaster!")

    age=int(input("what is ur age? "))
    if age < 12:
      bill=5
      print("child ticket is 5$")

    elif age <= 18:
     bill=7
     print("youth ticket is 7$")

    elif age >= 45 and age <= 55:
      bill=0
      print("Midlife crisis ticket is 0$")

    else:
     bill=12
     print("Adult ticket is 12$")

   
    want_photo=input("do u want a photo taken? Yes or No  ") 
    if want_photo=="Yes":
     bill += 3

    print(f"Your final bill is {bill}$")

else:   
    print("Sorry,u have to grow taller before u can ride.")



    # Adding even  number from 1 to 100 including 1 and 100

total_numbr = 0
for numbr in range (2, 101,2):
    total_numbr += numbr
print(total_numbr)


total_number = 0
for number in range (1,101):
    if number % 2==0:
        total_number += number
print(total_number)


# Average Height Exercise coding char
student_heights = input("input a list of student heights ").split(",")
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height=0
for height in student_heights:
    total_height += height
print(total_height)
# 156,178,165,171,187

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)

average = round(total_height/number_of_students)
print(average)



# def turn_right():
#    turn_left()
#    turn_left()
#    turn_left()

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# number_of_hurdles = 6
# while number_of_hurdles >0 :
#     jump()
#     number_of_hurdles -= 1
#     print(number_of_hurdles)

# How to use to while loops with conditions in the reebrog robot
# def turn_right():
#    turn_left()
#    turn_left()
#    turn_left()

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# while not at_goal():
#     jump()
   