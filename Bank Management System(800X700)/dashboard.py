from tkinter import *
import os

def accbal():
    t.destroy()
    os.system("python accbal.py")

def oservices():
    t.destroy()
    os.system("python oservices.py")
  
def tpassword():
    t.destroy()
    os.system("python tpassword.py")

t = Tk()
t.title("User Dashboard")
t.geometry('800x700')
t.configure(bg="yellow")

dashboard_heading = Label(t, text="User Dashboard", font=("Arial", 30), bg="Turquoise", fg="brown")
dashboard_heading.place(relx=0.5, rely=0.1, anchor=CENTER)


balance_button = Button(t, text="Account Balance", font=("Arial", 20), bg="skyblue", fg="black", command=accbal)
balance_button.place(relx=0.5, rely=0.3, anchor=CENTER)


online_services = Button(t, text="Online Services", font=("Arial", 20), bg="lightgreen", fg="black", command= oservices)
online_services.place(relx=0.5, rely=0.5, anchor=CENTER)

Transaction_Password = Button(t, text="Generate Transaction Password", font=("Arial", 20), bg="red", fg="yellow", command= tpassword)
Transaction_Password.place(relx=0.5, rely=0.7, anchor=CENTER)

t.mainloop()
