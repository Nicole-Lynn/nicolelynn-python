grocery_list = {}

while True:
    try:
        #Treat user’s input case-insensitively
        item = input().lower()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1

    except EOFError:
        print()
        #Print user’s grocery list ;
        # all uppercase, sorted alphabetically , prefixing each line with the no. of times the user inputted that item
        for item in sorted(grocery_list.keys()):
            print(grocery_list[item], item.upper())
        break


