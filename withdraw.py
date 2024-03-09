from tkinter import *
import mysql.connector
from tkinter import messagebox

t = Tk()
t.title("Withdraw")
t.geometry('800x700')
t.configure(bg="yellow")

connection = mysql.connector.connect(host='localhost', user='root', password='6368752',
                                     port='3306', database='amanbms')

c = connection.cursor()

def withdraw():
    account_number = Account.get()
    amount_val = Amount.get()

    # Check if account number or amount is empty
    if not account_number or not amount_val:
        messagebox.showwarning("Warning", "Please fill in both Account Number and Amount fields.")
        return

    amount_val = float(amount_val)  # Convert amount to float

    # Fetch current balance from the database
    c.execute("SELECT balance FROM accounts WHERE accno = %s", (account_number,))
    result = c.fetchone()

    if result:
        current_balance = float(result[0])
        new_balance = current_balance - amount_val
        
        if new_balance >= 0:  # Ensure balance doesn't go negative
            # Update balance in the database
            c.execute("UPDATE accounts SET balance = %s WHERE accno = %s", (new_balance, account_number))
            connection.commit()

            messagebox.showinfo("Success", f"Amount {amount_val} withdrawn successfully. New balance: {new_balance}")
        else:
            messagebox.showerror("Error", "Insufficient balance.")
    else:
        messagebox.showerror("Error", "Account not found.")

Withdraw = Label(t, text="Withdraw", font=("Arial", 30), bg="Turquoise", fg="brown")
Withdraw.place(relx=0.5, rely=0.2, anchor=CENTER)

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

AmountWithdraw = Label(t, text="Amount", font=("Arial", 20), bg="red", fg="white")
AmountWithdraw.place(relx=0.2, rely=0.57, anchor=CENTER)
Amount = Entry(t, font=("Arial", 15), bg="white", fg="black")
Amount.place(relx=0.7, rely=0.57, anchor=CENTER)

withdraw_button = Button(t, text="Withdraw", command=withdraw, font=("Arial", 20), bg="green", fg="white")
withdraw_button.place(relx=0.43, rely=0.7, anchor=CENTER)

t.mainloop()
