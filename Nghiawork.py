import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
 
def Ok():
    global myresult
    studname = e1.get()
    coursename = e2.get()
    fee = e3.get()
 
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="12345678910",database="smschool")
    mycursor=mysqldb.cursor()
 
    try:
        mycursor.execute("SELECT * FROM record where id = '" + stname + "'")
        myresult = mycursor.fetchall()
 
        for x in myresult:
            print(x)
        e2.delete(0, END)
        e2.insert(END, x[2])
        e3.delete(0, END)
        e3.insert(END, x[3])
 
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()

def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)

    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['id'])
    e2.insert(0,select['stname'])
    e3.insert(0,select['fee'])

def show():
      mysqldb = mysql.connector.connect(host="Localhost", user="root", password="12345678910", database="smschool")
      mycursor = mysqldb.cursor()
      studname = e1.get()
      mycursor.execute("SELECT * FROM record where id = '" + studname + "'")
      records = mycursor.fetchall()
      print(records)
      for i, (id1, stname1, course1, fee1) in enumerate(records,start=1):
         listBox.insert("", "end", values=(id1, stname1, course1, fee1))
         mysqldb.close()
 
root = Tk()
root.title("Search Mysql")
root.geometry("300x200")

Label(root, text="Student ID").place(x=10, y=10)
Button(root, text="Search", command=show ,height = 1, width = 13).place(x=140, y=40)
#Label(root, text="Course").place(x=10, y=80)
#Label(root, text="Fee").place(x=10, y=120)

e1 = Entry(root)
e1.place(x=140, y=10)
 
#e2 = Entry(root)
#e2.place(x=140, y=80)
 
#e3 = Entry(root)
#e3.place(x=140, y=120)

cols = ('id', 'stname', 'course', 'fee')
listBox = ttk.Treeview(root, columns=cols, show='headings' )

for col in cols:
   listBox.heading(col, text=col)
   listBox.grid(row=1, column=0, columnspan=2)
   listBox.place(x=10, y=200)

#show()
#listBox.bind('<Double-Button-1>',GetValue)
root.mainloop()