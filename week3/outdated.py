months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


while True:
    # Prompt the user for a date. Format month-day-year; 9/8/1636 or September 8, 1636
    # If the user’s input is not a valid date in either format, prompt the user again

    date = input("Date: ").strip()

    try:
        if "/" in date:
            month, day, year = date.split("/")
            if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                break

        elif "," in date:
            month1, day1, year = date.split(" ")

            # Find the number of the month
            if month1 in months:
                month = months.index(month1) + 1

            # Remove comma from day variable
            day = day1.replace(",", "")

            if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                break

    except:
        pass

# Print result in YYYY-MM-DD format. If day/month is below 10, add a zero before using print(f"{n:02}"), where n is a digit
# print(f"{year}-{int(month):02}-{int(day):02}")
print(year + "-" + f"{int(month):02}" + "-" + f"{int(day):02}")
