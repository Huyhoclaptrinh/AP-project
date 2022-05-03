from tkinter import ttk, messagebox
import mysql.connector
import tkinter as tk
from tkinter import *

                                      # ADMIN WINDOW
def admin_win():
   admin = Tk()
   admin.title("Admin")
   
   # This def helps for admin to login correctly
   def admin_login():
      admin_username= entry1.get()
      admin_password= entry2.get()
      if (admin_username=="" and admin_password==''):
          messagebox.showinfo("","Blank Not Allowed")
      elif (admin_username=="a" and admin_password=="1"):
          messagebox.showinfo("","Login success",command=admin_menu_win())
          admin.destroy()
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
def admin_menu_win():
    admin_menu = Tk()
    admin_menu.title("Menu")
    admin_menu.geometry("300x300")
    
    bt_books_list = Button(admin_menu,text="Books list",width=10, height=3,command=books_list_win).place(x=20,y=0)
    bt_revenue = Button(admin_menu,text="Revenue",width=10, height=3,command=revenue_win).place(x=20,y=50)
                                    # BOOKS LIST WINDOW
def books_list_win():
    books_list = Tk()
    books_list.title("Books list")
    books_list.state('zoomed')
    # This def is used to get the value of the table from the database
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
    # Def for adding the data to the table and also database in mysql
    def Add():
       
       id_get = id_entry.get()
       book_name_get = book_name_entry.get()
       author_name_get = author_name_entry.get()
       genre_get = genre_entry.get()
       price_get = price_entry.get()
       
       mysqldb=mysql.connector.connect(host="Localhost",user="root",password="12345678910",database="bookstore")
       mycursor=mysqldb.cursor()
       # Connecting mysql to this code and excute the variable and the command from mysql
       try:
          sql = "INSERT INTO  books (id,book_name,author_name,genre,price) VALUES (%s, %s, %s,%s,%s)"
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
    
    # Def for updating the data to the table and also database in mysql
    def update():
       id_get = id_entry.get()
       book_name_get = book_name_entry.get()
       author_name_get = author_name_entry.get()
       genre_get = genre_entry.get()
       price_get = price_entry.get()
       
       mysqldb=mysql.connector.connect(host="Localhost",user="root",password="12345678910",database="bookstore")
       mycursor=mysqldb.cursor()
       # Connecting mysql to this code and excute the variable and the command from mysql
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
    
    # Def for deleting the data to the table and also database in mysql
    def delete():
       id_get = id_entry.get()
       mysqldb=mysql.connector.connect(host="Localhost",user="root",password="12345678910",database="bookstore")
       mycursor=mysqldb.cursor()
       # Connecting mysql to this code and excute the variable and the command from mysql
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
          
    # Def for showing the data from the database in mysql to the table
    def show():
         # Connecting mysql to this code and excute the variable and the command from mysql
          mysqldb = mysql.connector.connect(host="Localhost", user="root", password="12345678910", database="bookstore")
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
    
    # Create labels
    tk.Label(books_list, text="Book List", fg="black", font=(None, 30)).place(x=300, y=5)
    
    tk.Label(books_list, text="ID").place(x=10, y=10)
    Label(books_list, text="Book Name").place(x=10, y=40)
    Label(books_list, text="Author Name").place(x=10, y=70)
    Label(books_list, text="Genre").place(x=10, y=100)
    Label(books_list, text="Price").place(x=10, y=130)
    
    # Create entries
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
    
    # Create a table
    cols = ('id', 'book_name', 'author_name','genre','price')
    listBox = ttk.Treeview(books_list, columns=cols, show='headings')
    
    for col in cols:
       listBox.heading(col, text=col)
       listBox.grid(row=1, column=0, columnspan=2)
       listBox.place(x=10, y=200)
    
    show()
    listBox.bind('<Double-Button-1>',GetValue)

                                     # REVENUE WINDOW(Display all the books which are sold out and the summary of prices)              
def revenue_win():
    revenue = Tk()
    revenue.title("Revenue")
    revenue.state('zoomed')
    # This def is used to get the value of the table from the database
    def GetValue1(event):
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
    # Def for adding the data to the table and also database in mysql
    def Add1():
       
       id_get = id_entry.get()
       book_name_get = book_name_entry.get()
       author_name_get = author_name_entry.get()
       genre_get = genre_entry.get()
       price_get = price_entry.get()
       
       mysqldb=mysql.connector.connect(host="Localhost",user="root",password="12345678910",database="bookstore")
       mycursor=mysqldb.cursor()
       # Connecting mysql to this code and excute the variable and the command from mysql
       try:
          sql = "INSERT INTO  sakila (id,book_name,author_name,genre,price) VALUES (%s, %s, %s,%s,%s)"
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
    # Def for updating the data to the table and also database in mysql
    def update1():
       id_get = id_entry.get()
       book_name_get = book_name_entry.get()
       author_name_get = author_name_entry.get()
       genre_get = genre_entry.get()
       price_get = price_entry.get()
       
       mysqldb=mysql.connector.connect(host="Localhost",user="root",password="12345678910",database="bookstore")
       mycursor=mysqldb.cursor()
       # Connecting mysql to this code and excute the variable and the command from mysql
       try:
          sql = "Update  sakila set book_name= %s,author_name= %s,genre = %s, price= %s where id= %s"
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
    # Def for deleting the data to the table and also database in mysql
    def delete1():
       id_get = id_entry.get()
       mysqldb=mysql.connector.connect(host="Localhost",user="root",password="12345678910",database="bookstore")
       mycursor=mysqldb.cursor()
       # Connecting mysql to this code and excute the variable and the command from mysql
       try:
          sql = "delete from sakila where id = %s"
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
          
    # Def for calculating the sum of the data to the table and also database in mysql
    def sum():
        db = mysql.connector.connect(host="Localhost",user="root",password="12345678910",database="bookstore")
          
        # Create cursor object
        cursor = db.cursor()
          
        # Get the sum of rows of a column
        cursor.execute("SELECT SUM(price) FROM sakila")
          
        # Fetch sum and display it
        global result
        result = cursor.fetchall()[0][0]
        messagebox.showinfo("Total", result)
        # Def for showing the data from the database in mysql to the table
    def show1():
         # Connecting mysql to this code and excute the variable and the command from mysql
          mysqldb = mysql.connector.connect(host="Localhost", user="root", password="12345678910", database="bookstore")
          mycursor = mysqldb.cursor()
          mycursor.execute("SELECT id,book_name,author_name,genre,price FROM sakila")
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
    
    # Create labels
    tk.Label(revenue, text="Revenue", fg="black", font=(None, 30)).place(x=300, y=5)
    
    tk.Label(revenue, text="ID").place(x=10, y=10)
    Label(revenue, text="Book Name").place(x=10, y=40)
    Label(revenue, text="Author Name").place(x=10, y=70)
    Label(revenue, text="Genre").place(x=10, y=100)
    Label(revenue, text="Price").place(x=10, y=130)
    
    # Create entries
    id_entry = Entry(revenue)
    id_entry.place(x=140, y=10)
    
    book_name_entry = Entry(revenue)
    book_name_entry.place(x=140, y=40)
    
    author_name_entry = Entry(revenue)
    author_name_entry.place(x=140, y=70)
    
    genre_entry = Entry(revenue)
    genre_entry.place(x=140, y=100)
    
    price_entry = Entry(revenue)
    price_entry.place(x=140, y=130)
    
    Button(revenue, text="Add",command = Add1,height=3, width= 13).place(x=300, y=130)
    Button(revenue, text="Update",command = update1,height=3, width= 13).place(x=410, y=130)
    Button(revenue, text="Delete",command = delete1,height=3, width= 13).place(x=520, y=130)
    Button(revenue, text="Sum",command = sum,height=3, width= 13).place(x=630, y=130)

    # Create a table
    cols = ('id', 'book_name', 'author_name','genre','price')
    listBox = ttk.Treeview(revenue, columns=cols, show='headings')
    
    for col in cols:
       listBox.heading(col, text=col)
       listBox.grid(row=1, column=0, columnspan=2)
       listBox.place(x=10, y=200)
    
    show1()
    listBox.bind('<Double-Button-1>',GetValue1)