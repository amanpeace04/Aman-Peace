from tkinter import *
import os

def deposit():
    t.destroy()
    os.system("python deposit.py")

def withdraw():
    t.destroy()
    os.system("python withdraw.py")

t = Tk()
t.title("Online Services")
t.geometry('800x700')
t.configure(bg="yellow")

Transactions = Label(t, text="Online Services", font=("Arial", 30), bg="Turquoise", fg="brown")
Transactions.place(relx=0.5, rely=0.3, anchor=CENTER)

deposit_button = Button(t, text="Deposit", command= deposit, font=("Arial", 20), bg="green", fg="white")
deposit_button.place(relx=0.3, rely=0.5, anchor=CENTER)

withdraw_button = Button(t, text="Withdraw", command= withdraw, font=("Arial", 20), bg="red", fg="white")
withdraw_button.place(relx=0.7, rely=0.5, anchor=CENTER)

t.mainloop()
