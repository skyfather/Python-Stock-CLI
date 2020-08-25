import requests
import csv
from db_module.db import Currencies


currency = Currencies()
url = "https://focusmobile-interview-materials.s3.eu-west-3.amazonaws.com/Cheap.Stocks.Internationalization.Currencies.csv"


def insert_records():
    try:
        response = requests.get(url)
    except Exception as e:
        # print(e)
        print("Network error: Could not fetch records from the internet")
    else:
        if response.status_code != 200:
            print('Failed to get data: HttpError', response.status_code)
        else:
            wrapper = csv.reader(response.text.split('\n')[1:])
            print("Adding currencies to the database")
            currency.add_currencies(wrapper)


def update_records():
    try:
        response = requests.get(url)
    except Exception as e:
        # print(e)
        print("Network error: Could not fetch updates from the internet")
    else:
        if response.status_code != 200:
            print('Failed to update data: HttpError ', response.status_code)
        else:
            wrapper = csv.reader(response.text.split('\n')[1:])
            print("Updating currencies in the database")
            currency.update_currency(wrapper)
