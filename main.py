from tkinter import Tk, ttk, END
from tkinter import Label, Frame, Entry, Spinbox, Button
from retrievals import getOptions, getPrice

global bill_items
bill_items = list()

# Function for items dropdown menu

def show_price(event):
    global selection
    selection = desc_combobox.get()
    price = getPrice(selection)
    unit_price_label.config(text= 'Rs.' + str(price))

# Function to clear values in textboxes after adding

def clear_item():
    qty_spinbox.delete(0, END)
    qty_spinbox.insert(0, '1')
    desc_combobox.set('')
    unit_price_label.config(text='')

# Function for adding item to invoice

def add_item():
    qty = int(qty_spinbox.get())
    desc = selection
    price = getPrice(desc)
    line_total = qty * price
    
    invoice_item = [desc, qty, price, line_total]  
    tree.insert('', 0, values=invoice_item)

    temp = (desc, qty) # (desc, qty, )
    bill_items.append(temp)
    print(bill_items)
    
    clear_item()

# Function to get added items



# Main

window = Tk()
window.title('Invoicer v2.1')
frame = Frame(window)
frame.pack(padx=20, pady=10)

# Labels
first_name_label = Label(frame, text='First Name')
first_name_label.grid(row=0, column=0)
last_name_label = Label(frame, text='Last Name')
last_name_label.grid(row=0, column=1)

# Entry boxes

first_name_entry = Entry(frame)
last_name_entry = Entry(frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

# Phone label and entry box

phone_label = Label(frame, text='Phone')
phone_label.grid(row=0, column=2)
phone_entry = Entry(frame)
phone_entry.grid(row=1, column=2)

# Quantity label and entry box

qty_label = Label(frame, text='Quantity')
qty_label.grid(row=2, column=0)
qty_spinbox = Spinbox(frame, from_=1, to=100)
qty_spinbox.grid(row=3, column=0)

# Description label and entry box

desc_label = Label(frame, text='Description')
desc_label.grid(row=2, column=1)

desc_combobox = ttk.Combobox(frame, state='readonly')
desc_combobox.grid(row=3, column=1)

desc_combobox['values'] = getOptions()
desc_combobox.bind('<<ComboboxSelected>>', show_price)

# Unit Price label and display box

unit_label = Label(frame, text='Unit Price')
unit_label.grid(row=2, column=2)
unit_price_label = Label(frame)
unit_price_label.grid(row=3, column=2)

# Add item button

add_item_button = Button(frame, text='Add Item', command=add_item)
add_item_button.grid(row=4, column=2, pady=5)

# Items display column

columns = ('desc', 'qty', 'price', 'total')
tree = ttk.Treeview(frame, columns=columns, show='headings')

tree.grid(row=5, column=0, columnspan=3, padx=20, pady=10)

tree.heading('desc', text='Description')
tree.heading('qty', text='Quantity')
tree.heading('price', text='Unit Price')
tree.heading('total', text='Total')

# Save Invoice and Generate Invoice Buttons

save_invoice_button = Button(frame, text='Save Invoice')
save_invoice_button.grid(row=6, column=0, columnspan=3, padx=20, pady=5, sticky='news')
new_invoice_button = Button(frame, text='New Invoice')
new_invoice_button.grid(row=7, column=0, columnspan=3, padx=20, pady=5, sticky='news')

# Running the application

window.mainloop()





