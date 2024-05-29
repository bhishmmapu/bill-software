import sqlite3
from contextlib import closing


def getOptions():
    with closing(sqlite3.connect('items.db')) as connection:
        with closing(connection.cursor()) as cursor:
            rows = cursor.execute("SELECT name, price FROM items").fetchall()

            optionList = list()
            for i in rows:
                optionList.append(i[0])
            return optionList


def getPrice(item_name):
    with closing(sqlite3.connect('items.db')) as connection:
        with closing(connection.cursor()) as cursor:
            rows = cursor.execute("SELECT price FROM items WHERE name='" + item_name + "'").fetchall()

            return rows[0][0]

# bill_items - [('pen', 5), ('pencil', 2), ('eraser', 1), ('scale', 1)]
def invoice_preprocess(bill_items):

    l = len(bill_items)
    invoice_items = []
    

    


     
    

invoice_preprocess('eraser')
