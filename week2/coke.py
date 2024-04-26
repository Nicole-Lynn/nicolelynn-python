# Coke is 50 cents, machine only accepts: 25 cents, 10 cents, and 5 cents. 
# Assume that the user will only input integers, ignore any integer that isn’t an accepted denomination.

amount = 50

while amount > 0:
    print("Amount Due:", amount)

    # Prompt the user to insert a coin, one at a time, each time informing the user of the amount due.
    insert = int(input("Insert Coin: "))
    if insert == 25 or insert == 10 or insert == 5:
        amount -= insert

# Once the user has inputted at least 50 cents, output how many cents in change the user is owed. 
change = abs(amount)
print("Change Owed:", change)




