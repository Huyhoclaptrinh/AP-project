from tkinter import *
from tkinter import messagebox

def Login():
      Username=entry1.get()
      Password=entry2.get()

      if (Username=="" and Password==''):
          messagebox.showinfo("","Blank Not Allowed")
      elif (Username=="KhoaDzvl" and Password=="admin"):
            messagebox.showinfo("","Login success")
      else:
          messagebox.showinfo("","incorrect username and password")

root=Tk()
root.title("Login")
root.geometry("400x300")
  
global entry1
global entry2

Label(root,text="Username").place(x=20,y=20)
Label(root,text="Password").place(x=20,y=60)

entry1=Entry(root,bd=5)
entry1.place(x=140,y=20)

entry2=Entry(root,bd=5)
entry2.place(x=140,y=60)

Button(root,text="Login",commmand=Login,height=3,width=13,bd=6).place(x=100,y=120)

root.mainloop()






