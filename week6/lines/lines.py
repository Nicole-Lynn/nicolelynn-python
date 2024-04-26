import sys

try:
    file_name = sys.argv[1]
    with open(file_name) as file:
        lines = file.readlines()

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) == 2:
        if file_name.endswith(".py"):
            length = 0
            for line in lines:
                if line.strip() and not line.strip().startswith("#"):
                    length += 1
            print(length)

        elif not file_name.endswith(".py"):
             sys.exit("Not a Python file")

except IndexError:
     sys.exit("Too few command-line arguments")

except FileNotFoundError:
     sys.exit("File does not exist")

