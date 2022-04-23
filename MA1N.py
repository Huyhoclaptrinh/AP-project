from tkinter import *
from tkinter import messagebox
import sqlite3


window=Tk()
window.title("Bookstore Management")
window.geometry("1000x900")
# Phan cua Khoa:
# Phan dang nhap

def user_win():
    user = Tk()
    user.geometry("300x300")
    user.title("User")
    
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
    user_menu.title("Menu")
    
    bt_user_detail = Button(user_menu,text="User",width = 10, height=3,command=user_detail_win).place(x=20,y=0)
    bt_display_book = Button(user_menu,text="Display book",width = 10, height=3,command=display_book_win).place(x=20,y=50)
    bt_search = Button(user_menu,text="Search",width = 10, height=3,command=search_win).place(x=20,y=100)
    bt_my_cart = Button(user_menu,text="My cart",width = 10, height=3,command=my_cart_win).place(x=20,y=150)
def user_detail_win():
    user_detail = Tk()
    user_detail.title("User Detail")
    user_detail.geometry("300x300")

def display_book_win():
    display_book = Tk()
    display_book.title("Display Book")
    display_book.geometry("300x300")

def search_win():
    search = Tk()
    search.title("Search")
    search.geometry("300x300")

def my_cart_win():
    my_cart = Tk()
    my_cart.title("My Cart")
    my_cart.geometry("300x300")
    
# Thiet ke giao dien cho phan dang ky
def user_signup_win():
    user_signup = Tk()
    user_signup.title("Sign up")
    user_signup.geometry("300x300")
    
    def getvals():
        messagebox.showinfo("","Accept")

    Label(user_signup,text="Register Form",font="ar 17 bold").place(x=4,y=1) 
    
    name = Label(user_signup, text ="Username")
    email = Label(user_signup, text ="Email")
    phone = Label(user_signup, text ="Phone")
    add = Label(user_signup, text ="Address")
    
    name.place(x=1, y=60)
    email.place(x=2, y=90)
    phone.place(x=3, y=120)
    add.place(x=4, y=150)
    
    namevalue=StringVar
    emailvalue=StringVar
    phonevalue=StringVar
    addvalue=StringVar
    checkvalue=IntVar
    
    nameentry = Entry(user_signup, textvariable=namevalue )
    emailentry = Entry(user_signup, textvariable=emailvalue )
    phoneentry = Entry(user_signup, textvariable=phonevalue )
    addentry = Entry(user_signup, textvariable=addvalue )
    
    nameentry.place(x=70, y=60)
    emailentry.place(x=70, y=90)
    phoneentry.place(x=70, y=120)
    addentry.place(x=70, y=150)
    
    checkbtn = Checkbutton(user_signup, text="remember me?", variable= checkvalue)
    checkbtn.place(x=70,y=180)
    
    Button(user_signup,text="Submit information", command=getvals).place(x=70,y=220)
    
def admin_win():
    admin = Tk()
    admin.title("Admin")
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
    admin_menu.title("Menu")
    admin_menu.geometry("300x300")
    
    bt_books_list = Button(admin_menu,text="Books list",width=10, height=3,command=books_list_win).place(x=20,y=0)
    bt_turnover = Button(admin_menu,text="Turnover",width=10, height=3,command=turnover_win).place(x=20,y=50)
    
def books_list_win():
    books_list = Tk()
    books_list.title("Books list")
    books_list.geometry("300x300")
    def addlist():
        listbox.insert(END, entry.get())
        entry.delete(0, END)

    def removelist():
        listbox.delete(listbox.curselection())
    # Day la phan giao dien de dien thong tin de them vao bang
    def add_win():
        add_win_menu = Tk()
        add_win_menu.title("Add Book")
        add_win_menu.geometry("300x300")
        # Nut submit de add thong tin vao table
        bt_submit_add = Button(add_win_menu,width = 20, command=addlist).pack()
    
    listbox = Listbox(books_list)
    listbox.pack()
    
    entry = Entry(books_list)
    entry.pack()
    
    bt_add = Button(books_list, text="Add book",command=add_win)
    bt_add.pack()
    
    bt_remove = Button(books_list, text="Remove book",command=removelist)
    bt_remove.pack()
        
        
def turnover_win():
    turnover = Tk()
    turnover.title("Turnover")
    turnover.geometry("300x300")    
        
l1=Label(window,text="BOOKSTORE MANAGEMENT",font="times 20")
l1.grid(row=1,column=2,columnspan=2)

bt_admin=Button(window,text="ADMIN",width=20,command=admin_win)
bt_admin.grid(row=3,column=2)

bt_user=Button(window,text="USER",width=20,command=user_win)
bt_user.grid(row=3,column=3)


window.mainloop()