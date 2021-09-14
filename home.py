from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
import asserts.images_ref
import gc

def cruella():
    root.destroy()
    import cruella
    cruella.root.mainloop()
    del cruella

def shershaah():
    root.destroy()
    import shershaah
    shershaah.root.mainloop()
    del shershaah

def boomika():
    root.destroy()
    import boomika
    boomika.root.mainloop()
    del boomika

def mimi():
    root.destroy()
    import mimi
    mimi.root.mainloop()
    del mimi

def mask():
    root.destroy()
    import mask
    mask.root.mainloop()
    del mask
def register():
    root.destroy()
    import register
    register.root.mainloop()
    del register
def admin():
    root.destroy()
    import admin_login
    admin_login.root.mainloop()
    del admin_login
def login():
    root.destroy()
    import login
    login.root.mainloop()
    del login
def logout():
    root.destroy()
    import login
    login.root.mainloop()
    del login

root = Tk()
root.title("CineBook")
root.iconbitmap("asserts\icons\clapperboard.ico")
root.geometry("1000x1000")
root.resizable(0,0)
root.wm_maxsize(1000, 1000)
root.configure(bg="#261C2C")

v = Scrollbar(root, orient='vertical').pack()


#list = Listbox(width=15, height=15, wrap=None, yscrollcommand=v).pack(side=TOP,fill=X)

films_list = Frame(root).place(x=0, y=0)

head = Label(root, text="Welcome to CineBook, ")

mov1x = ImageTk.PhotoImage(asserts.images_ref.mov1)
mov1 = Button(films_list, image=mov1x, command=cruella).place(x=0, y=0)

mov2x = ImageTk.PhotoImage(asserts.images_ref.mov2)
mov2 = Button(films_list, image=mov2x, command=shershaah).place(x=300, y=0)

mov3x = ImageTk.PhotoImage(asserts.images_ref.mov3)
mov3 = Button(films_list, image=mov3x, command=boomika).place(x=0, y=420)

mov4x = ImageTk.PhotoImage(asserts.images_ref.mov4)
mov4 = Button(films_list, image=mov4x, command=mimi).place(x=300, y=420)

mov5x = ImageTk.PhotoImage(asserts.images_ref.mov5)
mov5 = Button(films_list, image=mov5x, command=mask).place(x=600, y=0)

latest = Label(films_list, text="All latest movies in one Place...", font=('Lucida Handwriting', 24), bg='#261C2C', fg='#fff').place(x=200, y=400)

button_list = Frame(root).place()
btn1 = Button(button_list, text="admin", command=admin).place(x=100, y=900)
btn2 = Button(button_list, text="register", command=register).place(x=150, y=900)
btn3 = Label(button_list, text="logged in", fg='#fff', bg="#261C2C").place(x=210, y=900)

root.mainloop()