# Prompt the user for the name of a variable in camel case and outputs the corresponding name in snake case. 
    # Assume that the user’s input will indeed be in camel case, eg firstName to first_name

name = input("camelCase: ")

print("snake_case: ", end="")
for i in name:
    if i.isupper() == True:
        print(i.replace(i, "_" + i.lower()), end="")
    else:
        print(i, end="")

print()


