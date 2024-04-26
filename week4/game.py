import random

while True:
    try:
        n = int(input("Level: "))

        # Get a random number between 1 and n
        randomly = random.randint(1, n)

        while True:
            try:
                guess = int(input("Guess: "))

                if guess > 0:
                    if guess < randomly:
                        print("Too small!")

                    elif guess > randomly:
                        print("Too large!")

                    elif guess == randomly:
                        print("Just right!")
                        break

            except ValueError:
                print(end="")
        break

    except ValueError:
        print(end="")

    except:
        print()
        break
