def main():
    fraction = input("Fraction: ")
    percent = convert(fraction)
    print(gauge(percent))


def convert(fraction):
    while True:
        try:
            X, Y = fraction.split("/")
            X = int(X)
            Y = int(Y)

            if (X/Y) <= 1:
                percentage = round((X/Y) * 100)
                return percentage
            else:
                fraction = input("Fraction: ")
                pass

        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"



if __name__ == "__main__":
    main()
