from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import sqlite3

db_path = "./db.db"
db = sqlite3.connect(db_path)
cursor = db.cursor()


root = Tk()
root.geometry("500x700")
root.resizable(0, 0)
header = Label(root, text="Login")
header.grid(padx=225,pady=10)

usr1 = tk.StringVar()
psw1 = tk.StringVar()
usr = ttk.Entry(root, textvariable=usr1)
psw = ttk.Entry(root, textvariable=psw1, show='*')

usr.grid(padx=10,pady=10)
psw.grid(padx=10,pady=10)

x = usr.get()


def check_data():
    username = usr.get()
    password = psw.get()
    cursor.execute(f"select usrnm, psw from data where usrnm='{username}' and psw='{password}'")
    abc = cursor.fetchall()
    print(abc)
   
    if len(abc)==1:
       root.destroy()
       import home
       del home
       #home.a = f"currently logged in as {usr.get()}, logout"
    else:
        messagebox.showinfo("hi "+usr.get(),"failed to login")
    db.commit()
    db.close()

def register():
    root.destroy()
    import register
    root.mainloop()
    del register

submit = ttk.Button(root, text="Submit", command=check_data).grid(padx=10, pady=10)
go_to_register = ttk.Button(root, text="Go to register", command=register).grid(padx=10, pady=10)


root.mainloop()

