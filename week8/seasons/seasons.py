from datetime import date
import sys
import inflect


p = inflect.engine()

def main():
    try:
        birth = input("Date of Birth: ")
        year, month, day = get_year_month_day(birth)
    except ValueError:
        sys.exit("Invalid date")

    print(age_minutes(year, month, day))


# Get the year, month and date from the input date as integers
def get_year_month_day(dob):
    try:
        yy, mm, dd = dob.split("-")
    except ValueError:
        return "Invalid date"

    return int(yy), int(mm), int(dd)


def age_minutes(y, m, d):
    # Get age in days then convert to minutes
    try:
        bday = date(int(y), int(m), int(d))
    except ValueError:
        return "Invalid date"

    tday = date.today()
    age_in_days = (tday - bday).days
    age_in_minutes = age_in_days * 24 * 60
    minutes_in_words =  p.number_to_words(age_in_minutes, andword = "")
    return f"{minutes_in_words.capitalize()} minutes"




if __name__ == "__main__":
    main()









