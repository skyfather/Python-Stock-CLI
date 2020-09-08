import argparse
import sys
from db_module.db import Currencies, Languages
from googletrans import Translator
import stockquotes
from utils import insert_currency_records, insert_language_records, update_currency_records
from currency_module.currency_rates import CurrencyRates


company_name = "Cheap Stocks, Inc CLI"
# create the parser
my_parser = argparse.ArgumentParser(prog=f"{company_name}",
                                    # usage=f"{company_name} [options] currency",
                                    description="Stocks CLI for African trade",
                                    epilog="Stay tuned for future updates.")

# Stock argument
my_parser.add_argument("Stock",
                       metavar="stock",
                       type=str,
                       help="the company's stock symbol i.e AAPL"
                       )

# Update option to fetch the latest information from the internet
my_parser.add_argument("-u",
                       "--update",
                       action='store_true',
                       help="obtain the latest currencies and languages information")

# List option to display the supported currencies
my_parser.add_argument("-listc",
                       # "--currencies",
                       action='store_true',
                       help="the list of supported currencies in ISO-4172 code"
                       )

# List option to display the supported currencies
my_parser.add_argument("-listl",
                       # "--languages",
                       action='store_true',
                       help="the list of supported languages"
                       )

# An option for the user's preferred currency
my_parser.add_argument("-c",
                       "--currency",
                       action="store",
                       help="preferred currency in ISO-4172 code"
                       )

# An option for the user's preferred language
my_parser.add_argument("-l",
                       "--language",
                       action="store",
                       help="preferred language in ISO 639-1 code ---Powered by Google Translate API--"
                       )

# Execute the parse_args() method
args = my_parser.parse_args()

stock = args.Stock
update = args.update
currencies_list = args.listc
languages_list = args.listl
preferred_language = args.language
preferred_currency = args.currency

print("-----------------------------------------")
print(f"\t{company_name}")
print("-----------------------------------------")
if update:
    print("***Fetching the latest currencies and languages information***")
    # Insert new records into the database and update the existing records
    insert_currency_records()
    insert_language_records()
    update_currency_records()

# Retrieve all the currencies from the database
currency_object = Currencies()
all_currencies = currency_object.get_currencies()

# Retrieve all the languages from the database
language_object = Languages()
all_languages = language_object.get_languages()

# Displays the list af supported currencies from the database
if currencies_list:
    if len(all_currencies) == 0:
        print("Please provide the -u option to get the updates")
    else:
        print("***List of the supported currencies***")
        print("Country\t Currency\t Code")
        for currency in all_currencies:
            disp_info = f"{currency[0]}, {currency[1]}, {currency[2]}, {currency[3]}"
            print(disp_info)

# Displays the list af supported languages from the database
if languages_list:
    if len(all_languages) == 0:
        print("Please provide the -u option to get the updates")
    else:
        print("***List of the supported languages***")
        print("Language\t Code")
        for language in all_languages:
            disp_info = f"{language[0]}, {language[1]}, \t {language[2]}"
            print(disp_info)

if stock:
    print("-----------------------------------------")
    try:
        stock = str(stock)
        stock = stock.upper()
    except Exception as e:
        print(e)
    else:
        try:
            stock_price = stockquotes.Stock(stock).current_price
        except stockquotes.StockDoesNotExistError as sde:
            print(f"Stock {stock} does not exist.")
        except stockquotes.NetworkError as sn:
            print("Could not establish a network connection")
        except Exception as ex:
            print("Could not obtain the stock. Please check your internet connection")
        else:
            print("Stock price in USD", stock_price)
            default_text = f"The current price for {stock} is "  # {stock_price} USD"#247.74 USD"

            # A boolean flag for determining whether the user's preferred currency should be diplayed
            currency_flag = False
            if preferred_currency:
                preferred_currency = preferred_currency.upper()
                # Check if the input is three characters long
                if not len(preferred_currency) == 3:
                    print(f"\n{preferred_currency} is not a valid ISO-4217 code")
                else:
                    # Retrieve the specific currency from the database
                    supported_currency = currency_object.get_currency(preferred_currency)
                    # Check for the existence of currency in the database
                    if not supported_currency:
                        print(f"\n{preferred_currency} is not supported in the application as of now")
                    else:
                        currency_flag = True # The user's preferred currency is valid and supported in the application

                        cr = CurrencyRates()
                        quotes = cr.convert(preferred_currency)
                        # Fallback to Fixer API for currency conversion
                        if not quotes:
                            # Obtain the EURO TO USD exchange rate. Fixer API defaults by default uses EURO while our stock_price currency is in USD
                            euro_to_usd = cr.fixer_conversion("USD")
                            # Converts the stock_price from USD to EURO
                            stock_price_euro = stock_price*(1/euro_to_usd)
                            # Obtain the conversion rates from EURO to the user's preferred currency
                            quotes = cr.fixer_conversion(preferred_currency)
                            print(f"Preferred currency {preferred_currency}, ({supported_currency[2]}), Rate: {quotes}")
                            # Calculates the resulting stock price
                            stock_price = stock_price_euro*quotes
                        elif quotes:
                            print(f"Preferred currency {preferred_currency}, ({supported_currency[2]}), Rate: {quotes}")
                            stock_price = stock_price * quotes

            else:
                preferred_currency = "USD"
            if preferred_language:
                supported_language = language_object.get_language(preferred_language)
                if supported_language:
                    print(f"Preferred language {preferred_language}, ({supported_language[1]})")
                    translator = Translator()
                    try:
                        default_text = translator.translate(default_text, src='en', dest=preferred_language).text
                    except Exception as e:
                        print(
                            f"***Failed to translate to {preferred_language}. Check your internet connection and try again later***")
                else:
                    print(f"{preferred_language} is not supported in the application")

            # Assign USD currency if the user's preferred currency is invlid or unsupported in the application
            if not currency_flag:
                preferred_currency = "USD"
            print("-----------------------------------------")
            default_text = f"{default_text} {stock_price:.2f} {preferred_currency}"
            print(default_text)
            # print("---Powered by Google Translate--")


print("-----------------------------------------")
print(len(all_currencies), "Currencies supported by the application")
print("-----------------------------------------")
sys.exit()
