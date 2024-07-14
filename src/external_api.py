import requests
import os

from dotenv import load_dotenv


def get_sum_of_transaction(user_trans: dict) -> float:
    currency = user_trans["operationAmount"]["currency"]["code"]
    amount = user_trans["operationAmount"]["amount"]
    if currency in ["USD", "EUR"]:
        load_dotenv(".env")
        api_key_exchange_rates_data = os.getenv("API_KEY_EXCHANGE_RATES_DATA")
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from={currency}&amount={amount}"
        headers = {"apikey": api_key_exchange_rates_data}
        response = requests.get(url, headers=headers)
        result = response.json()["result"]
        return round(result, 2)
    else:
        return amount
