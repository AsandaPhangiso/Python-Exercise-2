# Question 1: Variable Assignment and String Manipulation

# TODO: Ask the user for their name and store it in a variable
print("What is your name? ")
username=input("name: ")
# TODO: Ask the user for their age and store it in a variable
print("What is your age ? ")
age= input ("age:")
# TODO: print a greeting using the name and age variables
print("Hi " + username + " " + age )
#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# TODO: Ask the user for the length of a rectangle and store it as an integer
print("What is the length of a rectangle?")
length=int(input('length:'))
# TODO: Ask the user for the width of a rectangle and store it as an integer
print("What is the width of the rectangle?")
width = int(input("width:"))
# TODO: Calculate the area of the rectangle
area = width * length
# TODO: Print the result
print(area)
#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# TODO: Ask the user for a temperature in Celsius and store it as a float
print("Write temperature in Celcius: ")
Celcius = float(input("Celcius= "))
letter='F'

# TODO: Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
print("Write temperature in Fahrenheit:")
Fahrenheit =str(((Celcius * 9/5 ) + 32)) + letter
# TODO: Print the result rounded to two decimal places
print(Fahrenheit) 
