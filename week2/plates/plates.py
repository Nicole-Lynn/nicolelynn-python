# Checking if a plate given by the user is valid based on some requirements

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # All vanity plates must start with at least two letters.
    if s[0:2].isalpha() == False:
        return False

    # Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if not 2 <= len(s) <= 6:
        return False

    # Numbers cannot be used in the middle of a plate; they must come at the end.
    # For example, AAA222 would be an acceptable vanity plate; AAA22A would not be acceptable.
    # The first number used cannot be a ‘0’.
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            elif s[i:].isdigit() == False:
                return False
            else:
                return True
        i += 1

    # No periods, spaces, or punctuation marks are allowed. 
    for p in s:
        if p in [".", " ", "?", "!"]:
            return False

    return True



main()

