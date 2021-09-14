from tkinter import *
import sqlite3
db = sqlite3.connect("db.db")
cursor = db.cursor()


cursor.execute("select usrnm from data")
ans = cursor.fetchall()

def go_back():
    r.destroy()
    import home
    home.root.mainloop()
    del home


r=Tk()
r.geometry("1000x500")
r.resizable(0,0)
scrollbar=Scrollbar(r)
scrollbar.pack(side=RIGHT,fill=Y)
listbox=Listbox(r,yscrollcommand=scrollbar.set)
for i in range(0, len(ans)):
    listbox.insert(END,ans[i])
go_back_btn = Button(r, text="Go Back", command=go_back, padx=10, pady=10).place(x=500, y=250)


listbox.pack()
r.mainloop()