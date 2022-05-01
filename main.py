from tkinter import *
import package
from package import admin
from package import user
# This is main window for bookstore management
window = Tk()
window.title("Bookstore Management")
window.geometry("1000x800")


l1=Label(window,text="BOOKSTORE MANAGEMENT",font="times 20")
l1.place(x=300, y = 250)

bt_admin=Button(window,text="ADMIN",width=20,command=admin.admin_win)
bt_admin.place(x = 200, y =500)
bt_user=Button(window,text="USER",width=20,command=user.user_win)
bt_user.place(x=610, y =500)
window.mainloop() 


window.mainloop() 