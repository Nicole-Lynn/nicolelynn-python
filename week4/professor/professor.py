import random


def main():
    n = get_level()

    # Randomly generate ten (10) math problems
    problems = 0
    score = 0
    while problems < 10:
        x, y = generate_integer(n)

        problem = (f"{x} + {y}")
        solved = x + y

        # If an answer is not correct (or not even a number), output EEE and re-prompt. Allow the user 3 tries in total.
        # If after three tries answer is still incorrect, output the correct answer.
        trials = 0
        while trials < 3:
            answer = int(input(f"{problem} = "))

            if answer != solved:
                print("EEE")
                trials += 1

                if trials == 3:
                    print(f"{problem} = {solved}")

            else:
                score += 1
                break

        problems += 1

    # Output the user’s score
    print(f"Score: {score}")


# get_level - Define and return level or raise a ValueError if level is not 1, 2, or 3
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                break
            elif level not in [1, 2, 3]:
                raise ValueError

        except ValueError:
            print(end="")
        except:
            pass

    return level


# generate_integer - Return a randomly generated non-negative integer with level digits
def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x, y


if __name__ == "__main__":
    main()
