# Code that uses an API to find the current price of bitcoin

import requests  # Use to call APIs
import sys  # Use to find arguments

# Convert argument to a float, or else quit with error message
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")

try:
    response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin?apiKey=9cf6f025d2d07b02df3b4e8bfc7ba423a96fed9735c32e1a2e76b95c3ceafd3a"
    )  # Call API
    price = float(
        response.json()["data"]["priceUsd"]
    )  # Get current price of one bitcoin
    cost = n * price
    print(f"${cost:,.4f}")
except requests.RequestException:  # If API call fails, say that
    print("Request failed")
