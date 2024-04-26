#Values are prices in USD
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


#Enables a user to place an order, prompting them for items, one per line, till user inputs control-d(ending input)
#User’s input case insensitively - lower(). Assume every item on the menu will be titlecased -title().
total = 0
while True:
    try:
        order = input("Item: ").title()

        #Display total cost of all items inputted thus far, prefixed with dollar sign($) and formatted to 2dp.
        if order in menu:
            total += menu[order]
            print(f"Total: ${total:.2f}")

    #Ignore any input that isn’t an item - KeyError
    except KeyError:
        pass
    
    #Catch when user inputs ctrl-d to end the input
    except EOFError:
        print()
        break





