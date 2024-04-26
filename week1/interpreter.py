express = input("Expression: ")

x, y, z = express.split(" ")

x = int(x)
z = int(z)

if y == "+":
    ans = x + z
elif y == "-":
    ans = x - z
elif y == "*":
    ans = x * z
elif y == "/":
    ans = x / z

print(float(round(ans, 1)))


