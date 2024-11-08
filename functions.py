withdrawn=int(input("how much would you like to withdraw ?")) #asking the user 
def withdraw(amount): #function
    balance=700 #assigning balance to amount avaailable
    current_amount= balance - amount #assigning current acount
    if balance<current_amount:
       print("insuffient funds")
    return=:
print(f"You have R{current_amount} left in your acount")# this is what it will print
