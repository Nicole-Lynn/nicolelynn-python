# Prompt the user for an input and call convert

def main():
    say = input("Say something, ")
    say1 = convert(say)
    print(say1)

# Convert accepts a str as input and returns the input with any :) converted to 🙂 and any :( converted to 🙁
def convert(say):
    say2 = say.replace(":)","🙂").replace(":(","🙁")
    return say2


main()


