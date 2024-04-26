# Prompt the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if:
    # the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No

ans = input("What's the Great Question of Life, the Universe and Everything? ").strip().lower()

match ans:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")



