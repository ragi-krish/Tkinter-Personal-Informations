import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import mysql.connector
from mysql.connector import Error

def open_calendar():
    def set_date():
        selected_date = cal.get_date()
        entry_box.delete(0, tk.END)
        entry_box.insert(0, selected_date)
        top.destroy()

    top = tk.Toplevel(root)
    cal = Calendar(top, selectmode='day')
    cal.pack(pady=20)
    ok_button = ttk.Button(top, text="OK", command=set_date)
    ok_button.pack()

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='mydb',
            user='root',
            password=''
        )
        return connection
    except Error as e:
        print(e)

def insert_date():
    selected_date = entry_box.get()
    connection = connect_to_db()
    if connection is not None:
        try:
            cursor = connection.cursor()
            insert_query = "INSERT INTO dates (date) VALUES (%s)"
            cursor.execute(insert_query, (selected_date,))
            connection.commit()
            print("Date inserted successfully")
        except Error as e:
            print(e)
        finally:
            cursor.close()
            connection.close()
    else:
        print("Error connecting to database")

root = tk.Tk()
root.title("Insert Date")

# Create Entry box
entry_box = tk.Entry(root, width=30)
entry_box.pack(pady=10)

# Create Calendar button
calendar_button = ttk.Button(root, text="Select Date", command=open_calendar)
calendar_button.pack(pady=10)

# Create Insert button
insert_button = ttk.Button(root, text="Insert Date", command=insert_date)
insert_button.pack(pady=10)

root.mainloop()
