# bill-software
This project is a simple billing software with an sqlite3 database.

# What each file does

## models.py

This file contains the database that I created for testing purpose. It has 2 field, name and price.

## retrievals.py

This file contains 2 functions:
1. getOptions() : Returns a list of items in the database
2. getPrice() : Return the price of an item

## main.py

This file has the main code. Check whatsapp for the working of the project. 

# How can you access the items added to the bill?

There is a dictionary declared in the globals scope called *bill_items*. It contains the item name as key, and the no of items as value.
Here is a sample output.

![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](https://i.ibb.co/cNz5cX2/CS-demo1.png)



# What is pending?

An invoice must be generated in the pdf format. Serial number, item name, unit price, qty, and total should be included in the tabular column.



