#pip install validator-collection
from validator_collection import checkers


email_address = input("What's your email address? ")

email_check = checkers.is_email(email_address)
if email_check:
    print("Valid")
else:
    print("Invalid")


