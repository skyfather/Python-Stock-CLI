import os
import sqlite3
from sqlite3 import IntegrityError


base_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Currencies():
    """
    A class that holds the Country, Currency, ISO_4217_Code
    """
    con = sqlite3.connect(os.path.join(base_dir, 'db3.sqlite3'))
    available_currencies = []

    def __init__(self):
        self.country = ""
        self.currency = ""
        self.code = ""

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
                # country,currency,code = i.split(',')
                # sql = f"UPDATE Currencies SET Currency='{currency}', ISO_4217_Code='{code}' where Country='{country}'"
                sql = f"UPDATE Currencies SET Currency='{i[1]}', ISO_4217_Code='{i[2]}' where Country='{i[0]}'"
                self.con.execute(sql)
#

# cur = Currencies()
# # print(cur.get_currency('KS'))
# print(cur.get_currency('AOA'))
# print(cur.get_currency('DZD'))
# new_list = ['Angolasa,Angolan kwanza,AOA', 'Algeria,Algerian dinar,DZD']
# for d in new_list:
#     co,na,code = d.split(',')
#     print(co)
#     print(na)
#     print(code)
# cur.update_currency(new_list)
# print(cur.get_currency('DZD'))
# print(cur.get_currency('AOA'))
# print(cur.get_currencies())
# print(cur)
# print("sffd")
# cur.country = "SD"
# print(cur)
# # cur.add_currencies([('Kenyissa','KShil',"KS"),('Kenyiasd','KShil',"KS")])
# cur.add_currencies([['Ksdvssa','KShil',"KSV"]])
# d =cur.get_currencies()
# print("---------")
# print(d)
# for i in d:
#     print(i[2])
# cur2 = Currencies()
# cur2.add_currency(['uganda','UG','UGX'])
# cur2.get_currencies()