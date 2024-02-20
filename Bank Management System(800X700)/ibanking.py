from tkinter import *

t = Tk()
t.title("Internet Banking")
t.geometry('800x700')
t.configure(bg="yellow")

InternetBanking = Label(t, text="Internet Banking", font=("Arial", 30), bg="Turquoise", fg="brown")
InternetBanking.place(relx=0.5, rely=0.2, anchor=CENTER)

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

Address = Label(t, text="Address", font=("Arial", 20), bg="Maroon", fg="white")
Address.place(relx=0.2, rely=0.57, anchor=CENTER)
Add = Entry(t, font=("Arial", 15), bg="white", fg="black")
Add.place(relx=0.7, rely=0.57, anchor=CENTER)

PinCode = Label(t, text="Pin Code", font=("Arial", 20), bg="red", fg="white")
PinCode.place(relx=0.2, rely=0.64, anchor=CENTER)
Pin = Entry(t, font=("Arial", 15), bg="white", fg="black")
Pin.place(relx=0.7, rely=0.64, anchor=CENTER)

Activate_button = Button(t, text="Activate", font=("Arial", 20), bg="green", fg="white")
Activate_button.place(relx=0.2, rely=0.75, anchor=CENTER)

deactivate_button = Button(t, text="Deactivate", font=("Arial", 20), bg="green", fg="white")
deactivate_button.place(relx=0.7, rely=0.75, anchor=CENTER)

t.mainloop()
