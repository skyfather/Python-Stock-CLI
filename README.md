# Python Stock CLI
A simple CLI stock application developed in Python that takes in an input flag 
corresponding to the stock symbol and displays the current stock price in the currency 
and language of preference if specified by the user.

## Technologies
The application is developed in Python programming language and
requires the following dependencies to properly function:
- python 3.71
- requests==2.24.0
- urllib3==1.25.10
- environs==8.0.0
- beautifulsoup4==4.9.1
- lxml==4.5.2
- googletrans==3.0.0
- stockquotes==2.0.0

The project is dependent upon [currencylayer](https://currencylayer.com/) and [fixer](https://fixer.io/) APIS to convert currencies.
## Illustration
### How to build the application
Git clone the project. It's recommended that you create a virtual environment
for Python3 and install the requirements from the `requirements.txt` file via 
`pip install -r requirements.txt`.

Create a `.env` file in the base directory and add your Currencylayer Api key and Fixer API key to `API_KEY_1` and `API_KEY_2` respectively.

`.env` file
```
export API_KEY_1 = YOUR_CURRENCY_LAYER_API_KEY
export API_KEY_2 = YOUR_FIXER_API_KEY
```

### How to run the application
Open the terminal or command prompt and navigate to the directory of the project.
Type a command in the following format `python main.py [options] stock`.

Type `python` followed by the name of the file in this case `main.py` and then the 
stock symbol or ticker symbol.

**Note:** For the first time running the application, run the following command
`python main.py -u AAPL`.

You could replace the `AAPL` argument with any stock symbol for the company of your 
choice. The `-u` or `--update` option will fetch the data from the website, create
the database and populate the table(s).

#### Arguments accepted by the CLI
+ Options
    - `-h` or `--help`. Provides help on the available commands for the CLI.
    - `-u` or `--update`. Updates the database with the latest information from
    the website.
    - `-listc`. Displays a list of all supported currencies in ISO 4217 code.
    - `-listl`. Displays a list of all supported languages in ISO 639-1 code.
    - `-c` or `--currrency`. The ISO 4217 code for the user's preferred currency.
    If specified, the application converts the currency and displays in the desired
    currency.
    - `-l` or `--language`. The ISO 639-1 code for the user's preferred language.
    If specified, the application translates the the stock price message to 
    display in that specified language through the third-party library `googletrans`
+ Parameter
    - `stock`. The stock symbol or ticker symbol for the company which you wish to
    know it's stock price i.e `AAPL`.

##### Example output
`python main.py AAPL -c KES -l sw`

![Program screenshot](/images/stock_cli.png)

## Status
The application is still in the development phase.
