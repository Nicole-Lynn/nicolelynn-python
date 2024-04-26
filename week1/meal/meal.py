def main():
    # Prompt for time and output whether it is breakfast time, lunch time, or dinner time
    # If it’s not time for a meal, don’t output anything at all
    # Assume that the user’s input will be in 24-hour format
    time = input("What time is it? ")

    #call convert
    time1 = convert(time)

    if time1 >= 7 and time1 <= 8:
        print("breakfast time")
    elif time1 >= 12 and time1 <= 13:
        print("lunch time")
    elif time1 >= 18 and time1 <= 19:
        print("dinner time")

# Converts time, a str in 24-hour format, to the corresponding number of hours as a float
def convert(time):
    hours, minutes = time.split(":")
    mins = float(minutes) / 60
    result = float(hours) + mins
    return result


if __name__ == "__main__":
    main()
