import requests
import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('CURRENCY_CONVERTER')

# Function to convert currencies
def convert_currency(from_currency, to_currency, amount, api_key):
    url = f"https://free.currconv.com/api/v7/convert?q={from_currency}_{to_currency}&compact=ultra&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    rate = data[f"{from_currency}_{to_currency}"]
    return rate * amount

# Convert 100 USD to EUR
amount_usd_to_eur = convert_currency('USD', 'EUR', 100, api_key)
print(f"100 USD is {amount_usd_to_eur} EUR")

# Convert 1000 JPY to GBP
amount_jpy_to_gbp = convert_currency('JPY', 'GBP', 1000, api_key)
print(f"1000 JPY is {amount_jpy_to_gbp} GBP")
