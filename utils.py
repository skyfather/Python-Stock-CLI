import requests
import csv
from db_module.db import Currencies, Languages


currency = Currencies()
language = Languages()
currencies_url = "https://focusmobile-interview-materials.s3.eu-west-3.amazonaws.com/Cheap.Stocks.Internationalization.Currencies.csv"
languages_url = "https://focusmobile-interview-materials.s3.eu-west-3.amazonaws.com/Cheap.Stocks.Internationalization.Languages.csv"


def insert_currency_records():
    """
    Function to populate the database with currency records from the website
    :return:
    """
    try:
        curencies_response = requests.get(currencies_url)
    except Exception as e:
        print("Network error: Could not fetch records from the internet")
    else:
        if curencies_response.status_code != 200:
            print('Failed to get Currencies data: HttpError', curencies_response.status_code)
        # Inserts currency records to the database
        else:
            currencies_wrapper = csv.reader(curencies_response.text.split('\n')[1:])
            print("Adding currencies to the database")
            currency.add_currencies(currencies_wrapper)


def insert_language_records():
    """
    function to populate the database with language records from the website
    :return:
    """
    try:
        languages_response = requests.get(languages_url)
    except Exception as e:
        print("Network error: Could not fetch language records from the internet")
    else:
        if languages_response.status_code != 200:
            print('Failed to get Languages data: HttpError', languages_response.status_code)
        # Inserts language records to the database
        else:
            languages_wrapper = csv.reader(languages_response.text.split('\n')[1:])
            print("Adding Languages to the database")
            language.add_languages(languages_wrapper)


def update_currency_records():
    """
    Updates the database currency's records
    :return:
    """
    try:
        curencies_response = requests.get(currencies_url)
    except Exception as e:
        print("Network error: Could not fetch updates from the internet")
    else:
        if curencies_response.status_code != 200:
            print('Failed to update data: HttpError ', curencies_response.status_code)
        else:
            currencies_wrapper = csv.reader(curencies_response.text.split('\n')[1:])
            print("Updating currencies in the database")
            currency.update_currency(currencies_wrapper)

