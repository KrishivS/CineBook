from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox


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

def go_back():
    root.destroy()
    import home
    root.mainloop()
    del home


def check_data():
    username = usr.get()
    password = psw.get()
   
    if username == "admin":
        if password == "admin123":
            root.destroy()
            import admin
            root.mainloop()
            del admin
        else:
            messagebox.showerror("hi "+usr.get(), 'failed to login')
    else:
        messagebox.showinfo("hi "+usr.get(),"failed to login")

submit = ttk.Button(root, text="Submit", command=check_data).grid(padx=10, pady=10)
go_back = ttk.Button(root, text="Go Back", command=go_back).grid(padx=10, pady=10)
root.mainloop()