from tkinter import *
import sqlite3


window=Tk()
window.geometry("400x300")


l1=Label(window,text="BOOKSTORE MANAGEMENT",font="times 20")
l1.grid(row=1,column=2,columnspan=2)

b1=Button(window,text="ADMIN",width=20)
b1.grid(row=3,column=2)

b2=Button(window,text="USER",width=20)
b2.grid(row=3,column=3)


window.mainloop()