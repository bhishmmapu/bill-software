import sqlite3

connection = sqlite3.connect('items.db')

cursor = connection.cursor()

# cursor.execute("CREATE TABLE items (name TEXT, price INTEGER)")

'''
cursor.execute("INSERT INTO items VALUES ('pen', 10)")
cursor.execute("INSERT INTO items VALUES ('pencil', 5)")
cursor.execute("INSERT INTO items VALUES ('eraser', 5)")
cursor.execute("INSERT INTO items VALUES ('scale', 15)")
connection.commit()
'''

rows = cursor.execute("SELECT price FROM items WHERE name='scale'").fetchall()
connection.close()

print((rows))

print(rows[0][0])

