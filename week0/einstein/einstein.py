# To calculate the physics formula E=mc^2 by prompting a user for a mass value

mass = int(input("m(kg): "))

c = 300000000

E = mass * (c ** 2)
print(E)
