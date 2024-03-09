from decimal import Decimal
from tkinter import *
from tkinter import messagebox
import mysql.connector

t = Tk()
t.title("Deposit")
t.geometry('800x700')
t.configure(bg="yellow")

def deposit():
    account_number = Account.get()
    amount_val = Amount.get()

    # Check if account number or amount is empty
    if not account_number or not amount_val:
        messagebox.showwarning("Warning", "Please fill in both Account Number and Amount fields.")
        return

    amount_val = Decimal(amount_val)  # Convert amount to Decimal

    # Connect to the MySQL database
    connection = mysql.connector.connect(host='localhost', user='root', password='6368752',
                                         port='3306', database='amanbms')
    cursor = connection.cursor()

    # Fetch current balance from the database
    cursor.execute("SELECT balance FROM accounts WHERE accno = %s", (account_number,))
    result = cursor.fetchone()

    if result:
        current_balance = Decimal(result[0])  # Convert balance to Decimal
        new_balance = current_balance + amount_val

        # Update balance in the database
        cursor.execute("UPDATE accounts SET balance = %s WHERE accno = %s", (new_balance, account_number))
        connection.commit()

        messagebox.showinfo("Success", f"Amount {amount_val} deposited successfully. New balance: {new_balance}")
    else:
        messagebox.showerror("Error", "Account not found.")

    # Close the cursor and connection
    cursor.close()
    connection.close()

Deposit = Label(t, text="Deposit", font=("Arial", 30), bg="Turquoise", fg="brown")
Deposit.place(relx=0.5, rely=0.2, anchor=CENTER)

AccountNumber = Label(t, text="Account Number", font=("Arial", 20), bg="Black", fg="yellow")
AccountNumber.place(relx=0.2, rely=0.35, anchor=CENTER)
Account = Entry(t, font=("Arial", 15), bg="white", fg="black")
Account.place(relx=0.7, rely=0.35, anchor=CENTER)

EmailId = Label(t, text="Email Id", font=("Arial", 20), bg="pink", fg="brown")
EmailId.place(relx=0.2, rely=0.43, anchor=CENTER)
Email = Entry(t, font=("Arial", 15), bg="white", fg="black")
Email.place(relx=0.7, rely=0.43, anchor=CENTER)

Mobileno = Label(t, text="Mobile", font=("Arial", 20), bg="Magenta", fg="white")
Mobileno.place(relx=0.2, rely=0.5, anchor=CENTER)
Mobile = Entry(t, font=("Arial", 15), bg="white", fg="black")
Mobile.place(relx=0.7, rely=0.5, anchor=CENTER)

Amountdeposit = Label(t, text="Amount", font=("Arial", 20), bg="red", fg="white")
Amountdeposit.place(relx=0.2, rely=0.57, anchor=CENTER)
Amount = Entry(t, font=("Arial", 15), bg="white", fg="black")
Amount.place(relx=0.7, rely=0.57, anchor=CENTER)

deposit_button = Button(t, text="Deposit", font=("Arial", 20), bg="green", fg="white", command=deposit)
deposit_button.place(relx=0.4, rely=0.7, anchor=CENTER)

t.mainloop()
