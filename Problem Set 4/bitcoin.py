import sys
import requests
import json

if not 2 <= len(sys.argv) < 3:
    sys.exit("Missing command-line argument")

try:
    quantity = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("i dunno")

o = response.json()
price = o.get("bpi").get("USD").get("rate_float")
bitcoin = price*quantity
print(f"${bitcoin:,}")
