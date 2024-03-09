from tkinter import *
from tkinter import messagebox
import mysql.connector

def fetch_balance():
    
    account_number = account_entry.get()
    password = T_password_entry.get()

   
    connection = mysql.connector.connect(host='localhost', user='root', password='6368752',
                                         port='3306', database='amanbms')
    cursor = connection.cursor()

    
    cursor.execute("SELECT balance FROM accounts WHERE accno = %s AND transaction_password = %s", (account_number, password))
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Balance", f"Your account balance is: {result[0]}")
    else:
        messagebox.showerror("Error", "Account not found or invalid transaction password.")

    
    cursor.close()
    connection.close()

t = Tk()
t.title("Account Balance")
t.geometry('800x700')
t.configure(bg="yellow")

account_bal_heading = Label(t, text="Account Balance", font=("Arial", 30), bg="Turquoise", fg="brown")
account_bal_heading.place(relx=0.5, rely=0.2, anchor=CENTER)

account_number_label = Label(t, text="Account Number", font=("Arial", 20), bg="Black", fg="yellow")
account_number_label.place(relx=0.2, rely=0.35, anchor=CENTER)
account_entry = Entry(t, font=("Arial", 15), bg="white", fg="black")
account_entry.place(relx=0.7, rely=0.35, anchor=CENTER)

Transaction_password_label = Label(t, text="Transaction Password", font=("Arial", 20), bg="green", fg="white")
Transaction_password_label.place(relx=0.2, rely=0.43, anchor=CENTER)
T_password_entry = Entry(t, font=("Arial", 15), bg="white", fg="black", show="*")
T_password_entry.place(relx=0.7, rely=0.43, anchor=CENTER)

fetch_balance_button = Button(t, text="Fetch Balance", font=("Arial", 20), bg="red", fg="yellow", command=fetch_balance)
fetch_balance_button.place(relx=0.45, rely=0.55, anchor=CENTER)

t.mainloop()
