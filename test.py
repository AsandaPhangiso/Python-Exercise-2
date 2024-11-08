# # #corrections
# # #Question 1
# # name = input("what is your name ?")
# # age = input("How old are you? ")
# # print("Hi " + name +" who is " + age +"years old")
# # print(f"Hi {name} who is {age} years old")#other way of using it with the f strings method
# # #Question 2
# # length=int(input("Enter the length of a rectangle "))
# # width=int(input("Enter the width of a rectangle "))
# # area= length * width
# # print(f"The area of the rectangle is: {area}")
 
# #  #Question 3
# #  celcius=input("Enter temperature in celcius: ")
# # fahrenheit= (celcius* 9/5)+32
# # print(f"The fahrenheit is {round(fahrenheit, 2)}")

# def calculator():
#     while True:
#         print("Simple Calculator")
#         print("Select operation:")
#         print("1. Addition")
#         print("2. Subtraction")
#         print("3. Multiplication")
#         print("4. Division")
#         print("5. Exit")

#         choice = input("Enter choice (1/2/3/4/5): ")

#         if choice == '5':
#             print("Exiting the calculator.")
#             break

#         if choice in ('1', '2', '3', '4'):
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))

#             if choice == '1':
#                 result = num1 + num2
#                 print(f"{num1} + {num2} = {result}")
#             elif choice == '2':
#                 result = num1 - num2
#                 print(f"{num1} - {num2} = {result}")
#             elif choice == '3':
#                 result = num1 * num2
#                 print(f"{num1} * {num2} = {result}")
#             elif choice == '4':
#                 if num2 != 0:
#                     result = num1 / num2
#                     print(f"{num1} / {num2} = {result}")
#                 else:
#                     print("Error: Division by zero is not allowed.")
#         else:
#             print("Invalid input. Please select a valid operation.")

# calculator()
# operation=input("Insert operation:")
# num1=float(input("Enter number:"))
# num2=float(input("Enter number:"))
# result = 0
# if operation == "+":
#     result = num1 + num2
#     print(result)
# elif operation == "-":
#     result = num1 - num2 
#     print(result)
# elif operation == "*":
#     result = num1 * num2
#     print(result)
# elif operation == "/":
#     result = num1/num2
#     print(result

student= { 
            "name":"Asanda",
            "age":"23",
            "Fav_color":"pink"
 }
 print(student)