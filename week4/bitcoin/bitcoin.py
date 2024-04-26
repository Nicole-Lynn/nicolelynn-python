import requests
import sys

try:
    n = float(sys.argv[1])


    coindesk_api = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    i = coindesk_api.json()

    #Current rate of bitcoin in USD
    USD_rate = i["bpi"]["USD"]["rate_float"]
    amount = float(USD_rate)

    #Outputs the current cost of n Bitcoins in USD to four decimal places, using, as a thousands separator.
    current_cost = (amount * n)
    print(f"${current_cost:,.4f}")


except ValueError:
    sys.exit("Command-line argument is not a number")

except requests.RequestException:
    print()

except IndexError:
    sys.exit("Missing command-line argument")






