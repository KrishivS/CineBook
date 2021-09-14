import json
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
import asserts.images_ref
from tkinter import messagebox

def go_back():
    root.destroy()
    import home
    home.root.mainloop()
    del home

x = {
    "cinema_name": "{request}".format(request='None'),
	"book_status": True,
	}

def book(new_data=x, filename='data.json'):
    a = messagebox.askyesno("purchase", "Are you sure you want to book this show?")
    if a == True:
        if json.load(open(filename, 'r+'))["book_details"][3]['book_status'] == False:
            with open(filename, 'r+') as file:
                file_data = json.load(file)
                file_data["book_details"][3]['book_status'] = True
                file.seek(0)
                json.dump(file_data, file, indent=4)
                import mod_data
            messagebox.showinfo("show booked", "show booked")
        else:
            messagebox.showinfo("show booked", "show is aldready booked")
    else:
        messagebox.showinfo("cancelled", "show cancelled")

def cancell_show(new_data=x, filename='data.json'):
    a = messagebox.askyesno("cancell", "Are you sure you want to cancel your booking?")
    if a == True:   
        if json.load(open(filename, 'r+'))["book_details"][3]['book_status'] == True:
            with open(filename, 'r+') as file:
                file_data = json.load(file)
                file_data["book_details"][3]['book_status'] = False
                file.seek(0)
                json.dump(file_data, file, indent=4)
                import mod_data
            messagebox.showinfo("cancelled", "show cancelled")
        else:
            messagebox.showinfo("show not booked","the show can be cancelled only when booked")
    else:
        messagebox.showinfo("cancelled", "show cancelled")


root = Tk()
root.title("CineBook")
root.iconbitmap("asserts\icons\clapperboard.ico")
root.geometry("800x800")
root.wm_maxsize(1000, 1000)
root.wm_minsize(800, 800)
root.configure(bg="#261C2C")


#list = Listbox(width=15, height=15, wrap=None, yscrollcommand=v).pack(side=TOP,fill=X)

films_list = Frame(root).place(x=0, y=0)

head = Label(root, text="Welcome to CineBook, ")

mov4x = ImageTk.PhotoImage(asserts.images_ref.mov4)
mov4 = Label(films_list, image=mov4x).place(x=0, y=0)

content = Label(films_list, text="""
Nulla nec porta velit. Aenean eu nulla tempus, tincidunt \nlorem eu, mollis ligula. Aenean convallis nulla eget metus volutpat,\n at cursus nisi consequat. Fusce rutrum sollicitudin lacus, \na gravida nunc. Curabitur condimentum, metus et cursus porttitor,\n turpis ligula suscipit arcu, ac hendrerit mauris magna at orci. Duis aliquam consequat nisl,\n id luctus libero luctus sed. In hac habitasse \nplatea dictumst. Mauris viverra sem ante,\n quis volutpat massa interdum vel.
""", fg="#fff", bg="#261C2C", font=("Cascadia Codes", 16), justify='left').place(x=0, y=410)
book_show = Button(root, text="Book this Show", padx=10, pady=10, command=book).place(x=200, y=750)
cancell = Button(root, text="Cancell if aldready booked", padx=10, pady=10, command=cancell_show).place(x=325, y=750)
go_back = Button(root, text="Go back", padx=10, pady=10, command=go_back).place(x=100, y=750)

root.mainloop()