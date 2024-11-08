# #------------------------------------------------------------------------------------
# #Task 1: Function with Loop and Conditional Logic

# # Define a function called 'check_attendance' that takes a list of names (students) and a list of absentees.
# # It should return a list of names of students who are absent.
def check_attendance(students, absentees):
    for student in students:
        if student in absentees:
            print(f"{student} is absent.")
        else:
            print(f"{student} is present.")

# # Call 'check_attendance' with a list of ["Alice", "Bob", "Charlie", "David"] 
# #       and a list of absentees ["Bob", "David"], and print the result.
students_list = ["Alice", "Bob", "Charlie", "David"]
absentees_list = ["Bob", "David"]

check_attendance(students_list, absentees_list)

# #------------------------------------------------------------------------------------
# # Task 2: Function for Real-Life Data Processing

# # TODO: Define a function called 'calculate_average_grade' that takes a dictionary where the keys are student names 
# #       and the values are their grades, and returns the average grade of the class.

def calculate_average_grade(grades):
    if not grades:
        return 0  # Return 0 if the dictionary is empty

    total = sum(grades.values())  # Sum of all grades
    count = len(grades)  # Number of students
    average = total / count  # Calculate average
    return average


# # TODO: Call the 'calculate_average_grade' function with the following dictionary:
# #       {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}, and print the result.
student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90
}

average_grade = calculate_average_grade(student_grades)
print(f"The average grade of the class is: {average_grade:.2f}")


# #------------------------------------------------------------------------------------
# # Task 3: Function Returning a Function (Higher-Order Function)

# # TODO: Define a function called 'operation_selector' that takes a string "add" or "multiply" as a parameter,
# #       and returns a function that either adds or multiplies two numbers.
def operation_selector(operation):
    if operation == "add":
        def add(x, y):
            return x + y
        return add
    elif operation == "multiply":
        def multiply(x, y):
            return x * y
        return multiply
    else:
        return None  # Return None if the operation is not recognized


# # TODO: Use 'operation_selector' to get the "add" function, and then call it to add 4 and 6.
add_function = operation_selector("add")

if add_function:
    print("Addition:", add_function(4, 6))


# # TODO: Use 'operation_selector' to get the "multiply" function, and then call it to multiply 3 and 7.
multiply_function = operation_selector("multiply")
if multiply_function:
    print("Multiplication:", multiply_function(3, 7))


# #------------------------------------------------------------------------------------
# # Task 4: Function for a Practical Scenario

# # TODO: Define a function called 'calculate_trip_cost' that takes three parameters:
# # • distance (in km), fuel_efficiency (km per liter), fuel_price (price per liter),
# # • and returns the total cost of fuel for the trip.
# # Task : Using a for loop with a dictionary (Real-life Scenario: Grocery Shopping List)
def calculate_trip_cost(distance, fuel_efficiency, fuel_price):
    # Calculate the total liters of fuel needed
    total_fuel_needed = distance / fuel_efficiency
    
    # Calculate the total cost of the fuel
    total_cost = total_fuel_needed * fuel_price
    
    return total_cost

trip_distance = 300  # in km
fuel_efficiency = 15  # km per liter
fuel_price = 20  # price per liter

trip_cost = calculate_trip_cost(trip_distance, fuel_efficiency, fuel_price)
print(f"The total cost of fuel for the trip is: {trip_cost:.2f}")


# # TODO: Create a dictionary with grocery items as keys and their quantities in stock as values.
# grocery_inventory = {
#     "Apples": 50,
#     "Bananas": 30,
#     "Tomatoes": 25,
#     "Bread": 15,
#     "Milk": 10
# }

grocery_inventory = {
    "Apples": 50,
    "Bananas": 30,
    "Tomatoes": 25,
    "Bread": 15,
    "Milk": 10
}


# # TODO: Use a for loop to print each item and its quantity in stock.
for item, quantity in grocery_inventory.items():
    print(f"{item}: {quantity} in stock")

# # TODO: Calculate and print the total number of items in stock (sum of all values in the dictionary).
total_items = sum(grocery_inventory.values())
print(f"Total number of items in stock: {total_items}")

# #------------------------------------------------------------------------------------
# # Task 5: Using a while loop for banking (Real-life Scenario: ATM Pin Retry System)

# # TODO: Ask the user to input their PIN.
# # TODO: If the PIN is incorrect, ask the user to try again, but only allow 3 attempts.
# # TODO: After 3 incorrect attempts, print "Account Locked". If the PIN is correct, print "Access Granted".

# correct_pin = "1234"
# attempts = 0

# # TODO: Use a while loop to implement the retry system.

# Define the correct PIN
correct_pin = "1234"
attempts = 0
max_attempts = 3

# Use a while loop to allow the user to enter their PIN
while attempts < max_attempts:
    user_input = input("Please enter your PIN: ")
    
    if user_input == correct_pin:
        print("Access Granted")
        break  # Exit the loop if the PIN is correct
    else:
        attempts += 1  # Increment the attempt counter
        print(f"Incorrect PIN. You have {max_attempts - attempts} attempts left.")

# After the loop, check if the user has exhausted their attempts
if attempts == max_attempts:
    print("Account Locked")



# #------------------------------------------------------------------------------------
# # Task 6: Using a for loop with range() for a School Grading System

# # TODO: Create a list with 10 random assignment scores (between 0 and 100).
# # TODO: Use a for loop to calculate the total score.
# # TODO: Calculate and print the average score for the class.
# # Bonus: Use conditional logic to print a congratulatory message if the average is above 75.

# import random

# # List of 10 student scores.
# scores = [random.randint(0, 100) for _ in range(10)]

# # TODO: Calculate total and average scores.

import random

# Create a list of 10 random assignment scores (between 0 and 100)
scores = [random.randint(0, 100) for _ in range(10)]

# Print the generated scores for reference
print("Assignment Scores:", scores)

# Calculate the total score
total_score = 0
for score in scores:
    total_score += score

# Calculate the average score
average_score = total_score / len(scores)

# Print the total and average scores
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score:.2f}")  # Format average to 2 decimal places

# Bonus: Print a congratulatory message if the average is above 75
if average_score > 75:
    print("Congratulations! The class average is above 75!")


# #------------------------------------------------------------------------------------
# # Task 7: Using the random module (Real-life Scenario: Random Team Selection)

# # TODO: Create a list with the names of 20 participants.
# # TODO: Use the random module to select 5 random participants.
# # TODO: Print the names of the selected team members.

# import random

# # List of participants.
# participants = ["Person1", "Person2", "Person3", ..., "Person20"]

# # TODO: Randomly select 5 people from the participants list.

import random

participants = [
    "Person1", "Person2", "Person3", "Person4", "Person5",
    "Person6", "Person7", "Person8", "Person9", "Person10",
    "Person11", "Person12", "Person13", "Person14", "Person15",
    "Person15", "Person17", "Person18", "Person19", "Person20"
]

# Randomly select 5 participants from the list
selected_participants = random.sample(participants, 5)

# Print the names of the selected team members
print("Selected Team Members:")
for participant in selected_participants:
    print(participant)


# #------------------------------------------------------------------------------------
# # Task 8: Custom module for a Fitness Tracker (Real-life Scenario: Tracking Calories Burned)

# # Step 1: Create a module named 'fitness_tracker.py' with the following functions:
# """
# def walk_calories(distance_km):
#     # Calories burned per km walking: 50
#     return distance_km * 50

# def run_calories(distance_km):
#     # Calories burned per km running: 100
#     return distance_km * 100

# def cycle_calories(distance_km):
#     # Calories burned per km cycling: 70
#     return distance_km * 70
# """
    

def walk_calories(distance_km):
    """
    Calculate calories burned while walking.
    
    Parameters:
    distance_km (float): The distance walked in kilometers.
    
    Returns:
    float: Calories burned during the walk.
    """
    # Calories burned per km walking: 50
    return distance_km * 50

def run_calories(distance_km):
    """
    Calculate calories burned while running.
    
    Parameters:
    distance_km (float): The distance run in kilometers.
    
    Returns:
    float: Calories burned during the run.
    """
    # Calories burned per km running: 100
    return distance_km * 100

def cycle_calories(distance_km):
    """
    Calculate calories burned while cycling.
    
    Parameters:
    distance_km (float): The distance cycled in kilometers.
    
    Returns:
    float: Calories burned during the cycling session.
    """
    # Calories burned per km cycling: 70
    return distance_km * 70


# # Step 9: Use the custom module in your main script:
# # TODO: Import the custom 'fitness_tracker' module.
# # TODO: Ask the user to input the distance they walked, ran, and cycled today.
# # TODO: Calculate and print the total calories burned for each activity.
# # TODO: Sum and print the total calories burned for the day.


# #------------------------------------------------------------------------------------
# # Task 10: Using a while loop to Simulate Loan Repayment (Real-life Scenario: Paying Off a Loan)

# # TODO: Ask the user to input the total loan amount.
# # TODO: Ask the user to input their monthly repayment amount.
# # TODO: Use a while loop to simulate monthly payments, reducing the loan each month.
# # TODO: Print the remaining loan amount after each payment.
# # TODO: When the loan is fully paid off, print a congratulatory message.

# # TODO: Use a while loop to simulate the repayment process.

# Ask the user to input the total loan amount.
loan_amount = float(input("Enter the total loan amount: "))

# Ask the user to input their monthly repayment amount.
monthly_payment = float(input("Enter your monthly repayment amount: "))

# Validate that the monthly payment is greater than 0
if monthly_payment <= 0:
    print("Monthly repayment amount must be greater than zero.")
else:
    # Use a while loop to simulate the repayment process.
    while loan_amount > 0:
        # Reduce the loan amount by the monthly payment
        loan_amount -= monthly_payment
        
        # Ensure the loan amount doesn't go negative
        if loan_amount < 0:
            loan_amount = 0
        
        # Print the remaining loan amount after each payment
        print(f"Remaining loan amount: ${loan_amount:.2f}")
    
    # When the loan is fully paid off, print a congratulatory message.
    print("Congratulations! Your loan has been fully paid off.")



