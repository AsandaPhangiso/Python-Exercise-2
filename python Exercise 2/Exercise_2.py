# Question 1: Arithmetic and Assignment Operators
x=9
y=10
# TODO: Add 3 to x using the += operator
x +=3
# TODO: Multiply y by 2 using the *= operator
y*=2
# TODO: Divide x by y and store the result in a variable called 'result'
result= x/y
# TODO: Print the value of 'result'
print(result)
#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators

# TODO: Create a condition that checks if a is greater than b
a=10
b=5
print(a>b)
# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
modulus =b%2
print(modulus==0)
# TODO: Create a condition that checks if c is less than or equal to a
c=10
print(c<=a)
# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a
final_conditions= (a>b) or (modulus==0) and (c<=a)
# TODO: Print the value of 'final_condition'
print(final_conditions)
#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
score = int(input("Enter a test score between 0-100 :"))
# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
if score>=90 and score<=100:
    print("You got an A!")
elif score<=89 and score>=80:
    print("You got a B!")
elif score<=79 and score>=70:
    print("You got a C!")
elif score<=69 and score>=60:
        print("You got a D!")
else:
     print("You got F!")       

 
# TODO: Print the grade for the given score
print(score)
#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1= int(input("Put number 1: "))
num2= int(input("Put number 2: "))
# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation = input("Insert (+, -, *, /) operation ")
# TODO: Use conditional statements to perform the chosen operation on num1 and num2
result = 0
if operation == "+":
    result = num1 + num2
    print(result)
elif operation == "-":
    result = num1 - num2 
    print(result)
elif operation == "*":
    result = num1 * num2
    print(result)
elif operation == "/":
    result = num1/num2
    print(result)
    if num2==0:
     print("you can't divide by 0")

# TODO: Handle the case of division by zero
elif num2==0:
    result = num1/num2

# TODO: Print the result of the operation
print(f"error")