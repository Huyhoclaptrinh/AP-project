from tkinter import *
import user
import admin

window = Tk()
window.geometry("1000x800")


l1=Label(window,text="BOOKSTORE MANAGEMENT",font="times 20")
l1.grid(row=1,column=2,columnspan=2)

bt_admin=Button(window,text="ADMIN",width=20,command=admin.admin_win)
bt_admin.grid(row=3,column=2)

bt_user=Button(window,text="USER",width=20,command=user.user_win)
bt_user.grid(row=3,column=3)


window.mainloop() 