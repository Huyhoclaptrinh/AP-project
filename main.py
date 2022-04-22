from glob import glob
from tkinter import *
from tkinter import messagebox
import sqlite3


window=Tk()
window.geometry("1000x900")
# Phan cua Khoa:
# Phan dang nhap

def user_win():
    user = Tk()
    user.geometry("300x300")
    
    Label(user,text="Username").place(x=20,y=20)
    Label(user,text="Password").place(x=20,y=60)
    entry1=Entry(user,bd=5)
    entry1.place(x=140,y=20)
    
    entry2=Entry(user,bd=5)
    entry2.place(x=140,y=60)
    # Dang nhap xong, xac nhan va bam nut ben duoi de chuyen sang phan menu cua User
    bt_user_signin = Button(user,text="Sign in",width=20,command=user_menu_win).pack(side=LEFT)
    # Nut dang ky, bam vao thi se chuyen sang tab khac de dien thong tin dang ky
    # Khoa tim cach de luu thong tin dang ky va lien ket voi phan dang nhap de xac nhan tai khoan dang nhap
    bt_user_signup = Button(user,text="Sign up",width=20,command=user_signup_win).pack(side=RIGHT)

def user_menu_win():
    user_menu = Tk()
    user_menu.geometry("300x300")
# Thiet ke giao dien cho phan dang ky
def user_signup_win():
    user_signup = Tk()
    user_signup.geometry("300x300")
    
def admin_win():
    admin = Tk()
    def admin_login():
        admin_username= entry1.get()
        admin_password= entry2.get()
        if (admin_username=="" and admin_password==''):
            messagebox.showinfo("","Blank Not Allowed")
        elif (admin_username=="KhoaDzvl" and admin_password=="admin"):
            messagebox.showinfo("","Login success",command=admin_menu_win())
        else:
            messagebox.showinfo("","incorrect username and password")
    
    
    Label(admin,text="Username").place(x=20,y=20)
    Label(admin,text="Password").place(x=20,y=60)
    entry1=Entry(admin,bd=5)
    entry1.place(x=140,y=20)
    
    entry2=Entry(admin,bd=5)
    entry2.place(x=140,y=60)
    admin.geometry("300x300")
    bt_admin_signin = Button(admin,text="Sign in",width=20,command=admin_login).place(x=100,y=120)
# Phan cua Nam:
def admin_menu_win():
    admin_menu = Tk()
    admin_menu.geometry("300x300")
    # Thay list thanh table
    def addlist():
        listbox.insert(END, entry.get())
        entry.delete(0, END)

    def removelist():
        listbox.delete(listbox.curselection())
    # Day la phan giao dien de dien thong tin de them vao bang
    def add_win():
        add_win_menu = Tk()
        add_win_menu.geometry("300x300")
        # Nut submit de add thong tin vao table
        bt_submit_add = Button(add_win_menu,width = 20, command=addlist).pack()
    
    listbox = Listbox(admin_menu)
    listbox.pack()
    
    entry = Entry(admin_menu)
    entry.pack()
    
    bt_add = Button(admin_menu, text="Add book",command=add_win)
    bt_add.pack()
    
    bt_remove = Button(admin_menu, text="Remove book",command=removelist)
    bt_remove.pack()

l1=Label(window,text="BOOKSTORE MANAGEMENT",font="times 20")
l1.grid(row=1,column=2,columnspan=2)

bt_admin=Button(window,text="ADMIN",width=20,command=admin_win)
bt_admin.grid(row=3,column=2)

bt_user=Button(window,text="USER",width=20,command=user_win)
bt_user.grid(row=3,column=3)


window.mainloop()