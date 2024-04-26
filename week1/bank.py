salute = input("Greeting: ").strip().lower()

if salute.startswith("hello"):
    print("$0")
elif salute.startswith("h"):
    print("$20")
else:
    print("$100")

