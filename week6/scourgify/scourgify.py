import sys
import csv


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    names = []
    with open(sys.argv[1]) as file1:
        reader = csv.DictReader(file1)
        for row in reader:
            names.append({"name": row["name"], "house": row["house"]})

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")


with open(sys.argv[2], "w", newline="") as file2:
    writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
    writer.writeheader()

    for student in names:
        last, first = student["name"].split(", ")
        house = student["house"]
        writer.writerow({"first": first, "last": last, "house": house})
