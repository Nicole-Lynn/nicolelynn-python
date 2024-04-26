import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Expects a str in 12-hour format and returns the corresponding str in 24-hour format
        #Formats expected are: 9:00 AM to 5:00 PM OR 9 AM to 5 PM
    if match := re.search(r"^([01]?[0-9]):?([0-9]{2})? {1}(AM|PM) {1}to {1}([01]?[0-9]):?([0-9]{2})? {1}(PM|AM)$", s):
        hour1, min1, am_pm1, hour2, min2, am_pm2 = match.groups()
        hour1 = int(hour1)
        min1 = int(min1 or "0")
        hour2 = int(hour2)
        min2 = int(min2 or "0")

        # Raise ValueError if either time is invalid
        if not ((hour1 <= 12 and min1 <= 59) and (hour2 <= 12 and min2 <= 59)):
            raise ValueError


        if am_pm1 == "AM" and hour1 == 12:
            hour1 = 0
        elif am_pm1 == "PM" and hour1 != 12:
            hour1 += 12

        if am_pm2 == "AM" and hour2 == 12:
            hour2 = 0
        elif am_pm2 == "PM" and hour2 != 12:
            hour2 += 12


    #Raise a ValueError instead if the input to convert is not in either of those formats
    else:
        raise ValueError

    return f"{hour1:02}:{min1:02} to {hour2:02}:{min2:02}"





if __name__ == "__main__":
    main()
