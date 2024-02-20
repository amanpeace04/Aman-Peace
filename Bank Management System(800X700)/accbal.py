from tkinter import *

def fetch_balance():

    account_number = account_entry.get()
    password = T_password_entry.get()

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
