# Python Stock CLI
A simple CLI stock application developed in Python that takes in an input flag 
corresponding to the input currency.
## Technologies
The application is developed in Python programming language and
requires the following dependencies to properly function:
- python 3.71
- requests==2.24.0
- urllib3==1.25.10
## Ilustration
### How to build the application
Git clone the project. It's recommended that you create a virtual environment
for Python3 and install the requirements from the `requirements.txt` file via 
`pip install -r requirements.txt`.
### How to run the application
Open the terminal or command prompt and navigate to the directory of the project.
Type a command in the following format `python main.py [options] currency`.

Type `python` followed by the name of the file in this case `main.py` and then the 
currency using ISO 4217 code.

**Note:** For the first time running the application, run the following command
`python main.py -u KES`.

You could replace the `KES` argument with any currency code of your 
choice. The `-u` or `--update` option will fetch the data from the website, create
the database and populate the table(s).

#### Arguments accepted by the CLI
+ Options
    - `-h` or `--help`. Provides help on the available commands for the CLI.
    - `-u` or `--update`. Updates the database with the latest information from
    the website.
+ Parameter
    - `currrency`. The ISO 4217 code for currency that the user inputs
    into the application. The application then displays whether or not the currency
    is supported. 

## Status
The application is still in the development phase.
