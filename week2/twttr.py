# Prompt the user for a str of text and then output the text but with all vowels (A, E, I, O, and U) omitted, 
    # whether inputted in uppercase or lowercase.

word = input("Input: ")

print("Output: ", end="")
for letter in word:
    if letter.lower() in ["a", "e", "i", "o", "u"]:
        print(letter.strip(letter), end="")
    else:
        print(letter, end="")

print()
