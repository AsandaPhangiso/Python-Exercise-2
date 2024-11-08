# # Question 1: Using a for loop with a list

# # TODO: Create a list of fruits
# fruit= ["apple" ,"orange " , "grape"]
# for fruit in fruit:
# # TODO: Use a for loop to print each fruit in the list
#     print(fruit)
# #-------------------------------------------------------------------------
# # Question 2: Using a while loop for countdown

# # TODO: Use a while loop to create a countdown from 5 to 1
# count=5
# while count>0:
#     print(count)
#     count-=1

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# # TODO: Use a for loop to print the first 10 square numbers
# number=0
# for number in range(1,11):
#     print(number **2)
    
#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random
# TODO: Create a list of colors
colors_list="pink" , "blue" , "yellow" , "green"
# TODO: Use a for loop to select and print 3 random colors from the list
for colors_list in colors_list:
   colors_list="pink" , "blue" , "yellow" , "green"
   random_colors= random.sample(colors_list,3)
   print(random_colors)
#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions
import math_operations

print(math_operations.add(2,3))
print(math_operations.subtract(2,3))
print(math_operations.divide(2,3))
print(math_operations.multiply(2,3))

# TODO: Use a while loop to create a simple calculator
def get_choice():
   print("")