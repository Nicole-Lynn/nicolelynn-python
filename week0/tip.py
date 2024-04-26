# Calculating how much one wants to tip as a percentage of the amount the spent

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d1 = d.replace("$", "")
    return float(d1)
    
def percent_to_float(p):
    p1 = p.replace("%", "")
    p2 = float(p1) / 100
    return p2

main()
