import os
import sqlite3
from sqlite3 import IntegrityError


base_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
con = sqlite3.connect(os.path.join(base_dir, 'db3.sqlite3'))


class Currencies():
    """
    A class that holds the Country, Currency, ISO_4217_Code
    """
    available_currencies = []

    def __init__(self):
        self.country = ""
        self.currency = ""
        self.code = ""
        self.con = con

        # Create a table to hold currency data if the table doesn't exist
        with self.con:
            sql = """
                CREATE TABLE IF NOT EXISTS Currencies (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                Country VARCHAR(100) UNIQUE,
                Currency VARCHAR(100),
                ISO_4217_Code VARCHAR(3)
                );
            """
            self.con.execute(sql)

    def __str__(self):
        return self.code

    def __repr__(self):
        return self.country + " " +self.currency+" "+ self.code

    # Add a single currency to the database
    def add_currency(self,currency):
        with self.con:
            sql = "INSERT INTO Currencies (Country,Currency,ISO_4217_Code) VALUES (?,?,?)"
            try:
                self.con.execute(sql,currency)
            except IntegrityError as ie:
                print(f"{currency[0]} already exists in the database with it's corresponding currency")
            except Exception as e:
                print(e)

    # Add a list of currencies to the database
    def add_currencies(self,currencies):
            with self.con:
                sql = "INSERT INTO Currencies (Country,Currency,ISO_4217_Code) VALUES (?,?,?)"
                try:
                    self.con.executemany(sql,currencies)
                except IntegrityError as ie:
                    print(f"Country already exists in the database with it's corresponding currency")
                except Exception as e:
                    print(e)

    # Retrieve specified currency information
    def get_currency(self, code):
        with self.con:
            query = f"SELECT * FROM Currencies WHERE ISO_4217_Code='{code}'"
            data = self.con.execute(query)
            self.code = data.fetchone()
            return self.code

    # Retrieve all available currencies' information
    def get_currencies(self):
            with self.con:
                query = "SELECT * FROM Currencies"
                data = self.con.execute(query)
                for currency in data:
                    self.available_currencies.append(currency)
                return self.available_currencies

    # Update the currencies' information
    def update_currency(self,data):
        with self.con:
            for i in data:
                sql = f"UPDATE Currencies SET Currency='{i[1]}', ISO_4217_Code='{i[2]}' where Country='{i[0]}'"
                try:
                    self.con.execute(sql)
                except Exception as e:
                    print(e)


class Languages():
    """docstring for Languages
        \nLanguages class holds the Language,ISO 639-1 code details
    """
    def __init__(self):
        self.con = con
        self.code = ''
        self.available_languages = []

        with self.con:
            sql = """
                CREATE TABLE IF NOT EXISTS Languages (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                Language VARCHAR(250) UNIQUE,
                ISO_639_1_Code VARCHAR(2)
                );
            """
            self.con.execute(sql)

    def __str__(self):
        return self.code

    def add_language(self,language):
        with self.con:
            sql = "INSERT INTO Languages (Language, ISO_639_1_Code) VALUES (?,?)"
            try:
                self.con.execute(sql,language)
            except IntegrityError as ie:
                print(f"Language {language} already exists in the database")
            except Exception as e:
                print(e)

    # Add a list of languages to the database
    def add_languages(self,languages):
        with self.con:
            sql = "INSERT INTO Languages (Language, ISO_639_1_Code) VALUES (?,?)"
            try:
                self.con.executemany(sql,languages)
            except IntegrityError as ie:
                print(f"Language already exists in the database")
            except Exception as e:
                print(e)

 # Retrieve specified language information
    def get_language(self, code):
        with self.con:
            query = f"SELECT * FROM Languages WHERE ISO_639_1_Code='{code}'"
            data = self.con.execute(query)
            self.code = data.fetchone()
            return self.code

    # Retrieve all available currencies' information
    def get_languages(self):
        with self.con:
            query = "SELECT * FROM Languages"
            data = self.con.execute(query)
            for language in data:
                self.available_languages.append(language)
            return self.available_languages