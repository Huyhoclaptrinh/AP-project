import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import numpy as np 
import matplotlib.pyplot as plt 
import sqlite3
import os
from tkinter import *


window = Tk()
window.geometry("1000x800")

                                      # ADMIN WINDOW
def admin_win():
    admin = Tk()
    admin.title("Admin")
    def admin_login():
        admin_username= entry1.get()
        admin_password= entry2.get()
        if (admin_username=="" and admin_password==''):
            messagebox.showinfo("","Blank Not Allowed")
        elif (admin_username=="Admin123" and admin_password=="admin2002"):
            messagebox.showinfo("","Login success",command=admin_menu_win())
        else:
            messagebox.showinfo("","incorrect username and password")
    Label(admin,text="Username").place(x=20,y=20)
    Label(admin,text="Password").place(x=20,y=60)
    entry1=Entry(admin,bd=5)
    entry1.place(x=140,y=20)
    
    entry2=Entry(admin,bd=5,show='*')
    entry2.place(x=140,y=60)
    admin.geometry("300x300")
    bt_admin_signin = Button(admin,text="Sign in",width=20,command=admin_login).place(x=100,y=120)

                                     # ADMIN MENU WINDOW
# # Phan cua Nam:
def admin_menu_win():
    admin_menu = Tk()
    admin_menu.title("Menu")
    admin_menu.geometry("300x300")
    
    bt_books_list = Button(admin_menu,text="Books list",width=10, height=3,command=books_list_win).place(x=20,y=0)
    bt_turnover = Button(admin_menu,text="Turnover",width=10, height=3,command=plot_turnover).place(x=20,y=50)
                                    # BOOKS LIST WINDOW
def books_list_win():
    books_list = Tk()
    books_list.title("Books list")
    books_list.geometry("300x300")
    
    def GetValue(event):
       id_entry.delete(0, END)
       book_name_entry.delete(0, END)
       author_name_entry.delete(0, END)
       genre_entry.delete(0, END)
       price_entry.delete(0, END)
       
       row_id = listBox.selection()[0]
       select = listBox.set(row_id)
       
       id_entry.insert(0,select['id'])
       book_name_entry.insert(0,select['book_name'])
       author_name_entry.insert(0,select['author_name'])
       genre_entry.insert(0,select['genre'])
       price_entry.insert(0,select['price'])
    
    def Add():
       add=Tk() 
       add.title("Turnover")
       add.geometry("300x300")
       id_get = id_entry.get()
       book_name_get = book_name_entry.get()
       author_name_get = author_name_entry.get()
       genre_get = genre_entry.get()
       price_get = price_entry.get()
       
       mysqldb=mysql.connector.connect(host="Localhost",user="root",password="dangtqwerty[25]@",database="bookstore")
       mycursor=mysqldb.cursor()
       try:
          sql = "INSERT INTO  books (id,book_name,author_name,genre,price) VALUES (%s, %s, %s, %s,%s,%s)"
          val = (id_get,book_name_get,author_name_get,genre_get,price_get)
          mycursor.execute(sql, val)
          mysqldb.commit()
          lastid = mycursor.lastrowid
          messagebox.showinfo("information", "Book inserted successfully")
          id_entry.delete(0, END)
          book_name_entry.delete(0, END)
          author_name_entry.delete(0, END)
          genre_entry.delete(0, END)
          price_entry.delete(0, END)
          id_entry.focus_set()
       except Exception as e:
          print(e)
          mysqldb.rollback()
          mysqldb.close()
    
    def update():
       id_get = id_entry.get()
       book_name_get = book_name_entry.get()
       author_name_get = author_name_entry.get()
       genre_get = genre_entry.get()
       price_get = price_entry.get()
       
       mysqldb=mysql.connector.connect(host="Localhost",user="root",password="dangtqwerty[25]@",database="bookstore")
       mycursor=mysqldb.cursor()
       try:
          sql = "Update  books set book_name= %s,author_name= %s,genre = %s, price= %s where id= %s"
          val = (book_name_get,author_name_get,genre_get,price_get,id_get)
          mycursor.execute(sql, val)
          mysqldb.commit()
          lastid = mycursor.lastrowid
          messagebox.showinfo("information", "Updated successfully")
          id_entry.delete(0, END)
          book_name_entry.delete(0, END)
          author_name_entry.delete(0, END)
          genre_entry.delete(0, END)
          price_entry.delete(0, END)
          id_entry.focus_set()
       except Exception as e:
    
          print(e)
          mysqldb.rollback()
          mysqldb.close()
    
    def delete():
       id_get = id_entry.get()
       mysqldb=mysql.connector.connect(host="Localhost",user="root",password="dangtqwerty[25]@",database="bookstore")
       mycursor=mysqldb.cursor()
       try:
          sql = "delete from books where id = %s"
          val = (id_get,)
          mycursor.execute(sql, val)
          mysqldb.commit()
          lastid = mycursor.lastrowid
          messagebox.showinfo("information", "Delete successfully...")
          id_entry.delete(0, END)
          book_name_entry.delete(0, END)
          author_name_entry.delete(0, END)
          genre_entry.delete(0, END)
          price_entry.delete(0, END)
          id_entry.focus_set()
       except Exception as e:
          print(e)
          mysqldb.rollback()
          mysqldb.close()
    def show():
          mysqldb = mysql.connector.connect(host="Localhost", user="root", password="dangtqwerty[25]@", database="bookstore")
          mycursor = mysqldb.cursor()
          mycursor.execute("SELECT id,book_name,author_name,genre,price FROM books")
          records = mycursor.fetchall()
          print(records)
          for i, (id1,book_name1,author_name1, genre1,price1) in enumerate(records,start=1):
             listBox.insert("", "end", values=(id1,book_name1,author_name1, genre1,price1))
             mysqldb.close()
    
    global id_entry
    global book_name_entry
    global author_name_entry
    global genre_entry
    global price_entry
    
    
    tk.Label(books_list, text="Book List", fg="black", font=(None, 30)).place(x=300, y=5)
    
    tk.Label(books_list, text="ID").place(x=10, y=10)
    Label(books_list, text="Book Name").place(x=10, y=40)
    Label(books_list, text="Author Name").place(x=10, y=70)
    Label(books_list, text="Genre").place(x=10, y=100)
    Label(books_list, text="Price").place(x=10, y=130)
    
    id_entry = Entry(books_list)
    id_entry.place(x=140, y=10)
    
    book_name_entry = Entry(books_list)
    book_name_entry.place(x=140, y=40)
    
    author_name_entry = Entry(books_list)
    author_name_entry.place(x=140, y=70)
    
    genre_entry = Entry(books_list)
    genre_entry.place(x=140, y=100)
    
    price_entry = Entry(books_list)
    price_entry.place(x=140, y=130)
    
    Button(books_list, text="Add",command = Add,height=3, width= 13).place(x=300, y=130)
    Button(books_list, text="Update",command = update,height=3, width= 13).place(x=400, y=130)
    Button(books_list, text="Delete",command = delete,height=3, width= 13).place(x=500, y=130)
    
    cols = ('id', 'book_name', 'author_name','genre','price')
    listBox = ttk.Treeview(books_list, columns=cols, show='headings' )
    
    for col in cols:
       listBox.heading(col, text=col)
       listBox.grid(row=1, column=0, columnspan=2)
       listBox.place(x=10, y=200)
    
    show()
    listBox.bind('<Double-Button-1>',GetValue)
                
                                         # TURNOVER PLOT WINDOW
def plot_turnover():
    labels = ["First quarter", "Second quarter", "Third quarter", "Fourth quarter"]
    values = [50, 70, 90, 10]
    plt.title("Turnover of Books store")
    plt.pie(values, labels = labels)
    plt.show()

                                             # USER WINDOW
def user_win():
    user = Tk()
    user.geometry("300x300")
    user.title("User")
    bt_user_signin = Button(user, text="Sign in", width=20, command=user_login_win).pack(side=LEFT)
    bt_user_signup = Button(user, text="Sign up", width=20, command=user_register_win).pack(side=RIGHT)


def login_sucess():
    global screen3
    screen3 = Toplevel(window)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text="Login Sucess").pack()
    Button(screen3, text="OK", command=user_menu_win).pack()


def password_not_recognised():
    global screen4
    screen4 = Toplevel(window)
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text="Password Error").pack()
    Button(screen4, text="OK").pack()


def user_not_found():
    global screen5
    screen5 = Toplevel(window)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text="User Not Found").pack()
    Button(screen5, text="OK").pack()


def user_register():
    print("working")

    
    username_info = username.get()
    password_info = password.get()
    email_info = mail.get()
    address_info = address.get()
    
    
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info + "\n")
    file.write(email_info +"\n")
    file.write(address_info + "\n")
    file.close()

    Label(screen1, text="Registration Sucess", fg="green", font=("calibri", 11)).pack()


def user_login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            password_not_recognised()

    else:
        user_not_found()

                                               # REGISTER WINDOW
def user_register_win():
    global screen1
    screen1 = Toplevel(window)
    screen1.title("Register")
    screen1.geometry("800x500")

    global username
    global password
    global mail
    global address
    global username_entry
    global password_entry
    global mail_entry
    global address_entry
    username = StringVar()
    password = StringVar()
    mail = StringVar()
    address = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()

    Label(screen1, text="Username * ").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()

    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password, show='*')
    password_entry.pack()

    Label(screen1, text="email").pack()
    mail_entry = Entry(screen1, textvariable=mail)
    mail_entry.pack()

    Label(screen1, text="address").pack()
    address_entry = Entry(screen1, textvariable=address)
    address_entry.pack()

    Button(screen1, text="Register", width=10, height=1, command=user_register).pack()

                                           # USER LOGIN WINDOW

def user_login_win():
    global screen2
    screen2 = Toplevel(window)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify, show='*')
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=user_login_verify).pack()

                                            # USER MENU WINDOW
def user_menu_win():
    user_menu = Tk()
    user_menu.geometry("300x300")
    user_menu.title("Menu")

    bt_user_detail = Button(user_menu, text="User", width=10, height=3, command=user_detail_win).place(x=20, y=0)
    bt_display_book = Button(user_menu, text="Display book", width=10, height=3, command=display_book_win).place(x=20,
                                                                                                                 y=50)
    bt_search = Button(user_menu, text="Search", width=10, height=3, command=search_win).place(x=20, y=100)
    bt_my_cart = Button(user_menu, text="My cart", width=10, height=3, command=my_cart_win).place(x=20, y=150)


                                               # USER DETAIL WINDOW

def user_detail_win():
    user_detail = Toplevel(window)
    user_detail.title("User Detail")
    user_detail.geometry("300x300")
    
    name_user = Label(user_detail, text="Name: ").pack()
    name_user_entry = Entry(user_detail, textvariable = username).pack()
    
    email_user = Label(user_detail, text="Email: ").pack()
    email_user_entry = Entry(user_detail, textvariable=mail).pack()
    
    address_user = Label(user_detail, text="Address: ").pack()
    address_user_entry = Entry(user_detail, textvariable = address).pack()

                                            # USER DISPLAY BOOK WINDOW

def display_book_win():
    display_book = Tk()
    display_book.title("Display Book")
    display_book.geometry("300x300")

    def show():
          mysqldb = mysql.connector.connect(host="Localhost", user="root", password="dangtqwerty[25]@", database="bookstore")
          mycursor = mysqldb.cursor()
          mycursor.execute("SELECT id,book_name,author_name,genre,price FROM books")
          records = mycursor.fetchall()
          print(records)
          for i, (id1,book_name1,author_name1, genre1,price1) in enumerate(records,start=1):
                listBox.insert("", "end", values=(id1,book_name1,author_name1, genre1,price1))
                mysqldb.close()

    cols = ('id', 'book_name', 'author_name','genre','price')
    listBox = ttk.Treeview(display_book, columns=cols, show='headings' )
    
    for col in cols:
       listBox.heading(col, text=col)
       listBox.grid(row=1, column=0, columnspan=2)
       listBox.place(x=10, y=200)
    
    show()                                         # SEARCH WINDOW

def search_win():
    search = Tk()
    search.title("Search")
    search.geometry("300x300")

                                                 # MY CART WINDOW

def my_cart_win():
    my_cart = Tk()
    my_cart.title("My Cart")
    my_cart.geometry("300x300")

l1=Label(window,text="BOOKSTORE MANAGEMENT",font="times 20")
l1.grid(row=1,column=2,columnspan=2)

bt_admin=Button(window,text="ADMIN",width=20,command=admin_win)
bt_admin.grid(row=3,column=2)

bt_user=Button(window,text="USER",width=20,command=user_win)
bt_user.grid(row=3,column=3)

l1=Label(window,text="BOOKSTORE MANAGEMENT",font="times 20")
l1.grid(row=1,column=2,columnspan=2)

bt_admin=Button(window,text="ADMIN",width=20,command=admin_win)
bt_admin.grid(row=3,column=2)

bt_user=Button(window,text="USER",width=20,command=user_win)
bt_user.grid(row=3,column=3)

window.mainloop() 