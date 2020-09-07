import requests
from environs import Env, EnvValidationError
import json


env = Env()
env.read_env()

BASE_URL_1 = "http://api.currencylayer.com/"
BASE_URL_2 = "http://data.fixer.io/api/"

currencies_url = "https://focusmobile-interview-materials.s3.eu-west-3.amazonaws.com/Cheap.Stocks.Internationalization.Currencies.csv"
languages_url = "https://focusmobile-interview-materials.s3.eu-west-3.amazonaws.com/Cheap.Stocks.Internationalization.Languages.csv"


class CurrencyRates(object):
    """docstring for CurrencyRates
    The class enables conversion of the currencies by relying on Currencylayer and fixer api
    """

    def __init__(self, url_1=BASE_URL_1, url_2=BASE_URL_2):
        try:
            self.api_key_1 = env("API_KEY_1")
            self.api_key_2 = env("API_KEY_2")
        except EnvValidationError as e:
            print(e)
        else:
            self.BASE_URL_1 = url_1
            self.BASE_URL_2 = url_2
            self.url_1 = f"{self.BASE_URL_1}live?access_key={self.api_key_1}"
            self.url_2 = f"{self.BASE_URL_2}latest?access_key={self.api_key_2}"

    def set_base_url_1(self, url):
        self.BASE_URL_1 = url

    def set_base_url_2(self, url):
        self.BASE_URL_2 = url

    def get_api_key_1(self):
        return self.api_key_1

    def set_api_key_1(self, api):
        try:
            self.api_key_1 = env(api)
        except EnvValidationError as e:
            print(e)

    def set_api_key_2(self, api_key):
        try:
            self.api_key_2 = env(api_key)
        except EnvValidationError as e:
            print(e)

    def convert(self, currency):
        currency = currency.upper()
        try:
            response = requests.get(self.url_1)
        except requests.exceptions.ConnectionError as ce:
            print("Failed to establish a new connection: [Errno 11001] getaddrinfo failed")
        except Exception as e:
            print("*The API response Failed! ")
        else:
            if response.status_code != 200:
                print("*The API response Failed. status_code", response.status_code)
            else:
                dollar_to_currency = f"USD{currency}"
                json_response = json.loads(response.text)
                try:
                    return json_response['quotes'][dollar_to_currency]
                except KeyError as ke:
                    print(f"Success: {json_response['success']}, Error code: {json_response['error']['code']}")
                except Exception as e:
                    print(e)

    def fixer_conversion(self, currency):
        try:
            response = requests.get(self.url_2)
        except requests.exceptions.ConnectionError as ce:
            print("Failed to establish a new connection: [Errno 11001] getaddrinfo failed")
        except Exception as e:
            print("*The API response Failed! ")
        else:
            json_response = json.loads(response.text)
            try:
                return json_response['rates'][currency]
            except KeyError as ke:
                print(f"Success: {json_response['success']}, Error code: {json_response['error']['code']}")
            except Exception as e:
                print(e)


