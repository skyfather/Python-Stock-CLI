import argparse
import sys
from db_module.db import Currencies
from utils import insert_records, update_records


company_name = "Cheap Stocks, Inc CLI"
# create the parser
my_parser = argparse.ArgumentParser(prog=f"{company_name}",
                                    # usage=f"{company_name} [options] currency",
                                    description="Stocks CLI for African trade",
                                    epilog="Stay tuned for future updates.")
# Add the arguments
# Currency argument
my_parser.add_argument("Currency",
                       metavar="currency",
                       type=str,
                       nargs="+",
                       help="the ISO-4172 currency code i.e USD"
                       )

# Update option to fetch the latest information from the internet
my_parser.add_argument("-u",
                       "--update",
                       action='store_true',
                       help="obtain the latest currencies information")

# Execute the parse_args() method
args = my_parser.parse_args()

currency = args.Currency
update = args.update

print("-----------------------------------------")
print(f"\t{company_name}")
print("-----------------------------------------")
if update:
    print("***Fetching the latest currency information***")
    # Insert new records into the database and update the existing records
    insert_records()
    update_records()

currency_object = Currencies()

for cur in currency:
    cur = cur.upper()
    # Check if the input is three characters long
    if not len(cur) == 3:
        print(f"\n{cur} is not a valid ISO-4217 code")
    else:
        # Retrieve the specific currency from the database
        supported_currency = currency_object.get_currency(cur)
        # Check for the existence of currency in the database
        if not supported_currency:
            print(f"\n{cur} is not supported in the application as of now")
        else:
            print(f"\n{cur} Currency is supported")
print("-----------------------------------------")
# Retrieve all the currencies from the database
all_currencies = currency_object.get_currencies()
print(len(all_currencies), "Currencies supported by the application")
print("-----------------------------------------")
sys.exit()
