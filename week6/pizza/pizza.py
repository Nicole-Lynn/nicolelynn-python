import sys
import csv
from tabulate import tabulate

try:
    file_name = sys.argv[1]

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) == 2:
        if not file_name.endswith(".csv"):
            sys.exit("Not a CSV file")

        elif file_name.endswith(".csv"):
            with open(file_name) as file:
                reader = csv.reader(file)
                pizzas_table = []
                for row in reader:
                    pizzas_table.append(row)

        print(tabulate(pizzas_table, headers="firstrow", tablefmt="grid"))

except IndexError:
    sys.exit("Too few command-line arguments")

except FileNotFoundError:
    sys.exit("File does not exist")






