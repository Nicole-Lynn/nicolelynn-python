def main():
    msg = input("Input: ")
    print(shorten(msg))


def shorten(word):
    short_word = ""
    for letter in word:
        if letter.lower() in ["a", "e", "i", "o", "u"]:
            short_word = short_word + ""
        else:
            short_word = short_word + letter
            
    return short_word


if __name__ == "__main__":
    main()
