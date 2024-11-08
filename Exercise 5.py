# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits= ["apples", "grapes","banana", "peaches"]
# TODO: Add a fruit to the end of the list
fruits.append("blueberry")
print(fruits)
# TODO: Insert a fruit at the beginning of the list
fruits.insert(0,"guava")
print(fruits)
# TODO: Remove a fruit from the list
fruits.remove("apples")
# TODO: Print the modified list
print(fruits)

#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
numbers=[1,2,3,4,5]
# TODO: Create a new list with each number squared
new=[1*1,2*2,3*3,4*4,5*5]
# TODO: Find the sum and average of the original numbers
sum=1+2+3+4+5
avarege=sum/5
# TODO: Print the results
print(avarege)

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
capitals_countries={
    "South_Africa":"Pretoria",
    "Nigeria":"Abuja",
    "Ghana":"Acrra",
    "Zambia":"Lusaka"
}
# TODO: Add a new country-capital pair
capitals_countries["Lesotho"]="Maseru"
print(capitals_countries["Lesotho"])
# TODO: Update the capital of an existing country
capitals_countries["Ghana"]="Abuja"
print(capitals_countries)
# TODO: Remove a country-capital pair
capitals_countries.pop("Ghana")
# TODO: Print the modified dictionary
print(capitals_countries)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruit_colors={
    "orange":"orange",
    "banana":"yellow",
     "grape":"green",
     "apple":"red"

}
# TODO: Print all the fruits (keys)
keys=fruit_colors.keys()
print(keys)
# TODO: Print all the colors (values)
print(fruit_colors.values())
# TODO: Print each fruit and its color
for fruits,colors in fruit_colors.items():
    
# TODO: Check if a fruit is in the dictionary and print its color
    print(fruits,colors)