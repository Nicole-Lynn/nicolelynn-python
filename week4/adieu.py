import inflect

p = inflect.engine()

name = []
while True:
    try:
        myname = input("Name: ")
        name.append(myname)

    except EOFError:
        print()
        names = p.join(name)
        print("Adieu, adieu, to " + names)
        break




