import re


def main():
    print(count(input("Text: ")))


def count(s):
    # Findall 'um' in the text input using findall function
    all_um = re.findall(r"\b(um)\b[\W\s,\.]*", s, re.IGNORECASE)

    # The only items generated in all_um will be the 'um's found in the text and therefore we begin counting and count all
        # in the set
    count_um = 0
    for _ in all_um:
        count_um += 1

    return count_um





if __name__ == "__main__":
    main()
