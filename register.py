from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3
import os

if os.path.exists("db.db"):
    pass
else:
    db_path = "./db.db"
    db = sqlite3.connect(db_path)
    cursor = db.cursor()
    cursor.execute("""
        create table data(usr integer primarykey, usrnm varchar(100), psw varchar(100), phn varchar(20), email varchar(100))
    """)
    db.commit()
    db.close()
root = Tk()
root.geometry("500x700")
root.resizable(0, 0)
header = Label(root, text="Register")
header.grid(padx=225,pady=10)
usr1 = StringVar()
psw1 = tk.StringVar()
ph1 = tk.IntVar()
em1 = tk.StringVar()
usr = ttk.Entry(root, textvariable=usr1)
psw = ttk.Entry(root, textvariable=psw1, show='*')
ph = ttk.Entry(root, textvariable=ph1)
em = ttk.Entry(root, textvariable=em1)

usr.grid(padx=10,pady=10)
psw.grid(padx=10,pady=10)
ph.grid(padx=20,pady=20)
em.grid(padx=10,pady=10)



def check_data():
    global data
    data = {"username": usr1.get(), "password": psw1.get(), "phonenumber": ph1.get(), "email": em1.get()}
    if data["username"] != '':
        if data["password"] != '':
            if len(str(data["phonenumber"])) == 10:
                if data["email"].find("@") != -1:
                    messagebox.showinfo("success", f"Successfully logged in as {data['username']}")
                    # satisfy
                    db = sqlite3.connect("db.db")
                    cursor = db.cursor()
                    cursor.execute(f"""
                            insert into data(usr, usrnm, psw, phn, email)
                            values(null, '{data["username"]}', '{data["password"]}', '{data["phonenumber"]}', '{data["email"]}')
                            """)
                    db.commit()
                    db.close()
                    print("success")
                else:
                    messagebox.showinfo("failed", "login failed(1)")    
            else:
                messagebox.showinfo("failed", "login failed(2)")
        else:
            messagebox.showinfo("failed", "login failed(3)")
    else:
        messagebox.showinfo("failed", "login failed(4)")

def close():
    root.destroy()
    import login
    root.mainloop()
    del login


submit = ttk.Button(root, text="Submit", command=check_data).grid(padx=10, pady=10)
go_to_login = ttk.Button(root, text="Go to login", command=close).grid(padx=10, pady=10)
root.mainloop()
