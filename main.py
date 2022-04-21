from tkinter import *
import sqlite3


window=Tk()
window.geometry("1000x900")
def user_win():
    user = Tk()
    user.geometry("300x300")
    
def admin_win():
    admin = Tk()
    admin.geometry("300x300")

l1=Label(window,text="BOOKSTORE MANAGEMENT",font="times 20")
l1.grid(row=1,column=2,columnspan=2)

bt_admin=Button(window,text="ADMIN",width=20,command=admin_win)
bt_admin.grid(row=3,column=2)

bt_user=Button(window,text="USER",width=20,command=user_win)
bt_user.grid(row=3,column=3)


window.mainloop()