from tkinter import *
import os

def deposit():
    t.destroy()
    os.system("python deposit.py")

def withdraw():
    t.destroy()
    os.system("python withdraw.py")

def ibanking():
    t.destroy()
    os.system("python ibanking.py")

def atm():
    t.destroy()
    os.system("python atm.py")

t = Tk()
t.title("Online Services")
t.geometry('800x700')
t.configure(bg="yellow")

OnlineS = Label(t, text="Online Services", font=("Arial", 30), bg="Turquoise", fg="brown")
OnlineS.place(relx=0.5, rely=0.3, anchor=CENTER)

deposit_button = Button(t, text="Deposit", command= deposit, font=("Arial", 20), bg="green", fg="white")
deposit_button.place(relx=0.3, rely=0.5, anchor=CENTER)

withdraw_button = Button(t, text="Withdraw", command= withdraw, font=("Arial", 20), bg="red", fg="white")
withdraw_button.place(relx=0.7, rely=0.5, anchor=CENTER)

ibanking = Button(t, text="Internet Banking", command= ibanking, font=("Arial", 20), bg="black", fg="orange")
ibanking.place(relx=0.3, rely=0.63, anchor=CENTER)

withdraw_button = Button(t, text="ATM", command= atm, font=("Arial", 20), bg="pink", fg="red")
withdraw_button.place(relx=0.7, rely=0.63, anchor=CENTER)

t.mainloop()
