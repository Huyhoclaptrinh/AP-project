from tkinter import *
root=Tk()
root.geometry("400x300")

def getvals():
    print("Accept")
#heading
Label(root,text="Register Form",font="ar 17 bold").place(x=4,y=1) 

#Field name
name = Label(root, text ="Username")
entry = Label(root,text ="Password")
email = Label(root, text ="Email")
phone = Label(root, text ="Phone")
add = Label(root, text ="Address")

#packing field
name.place(x=1, y=60)
entry.place(x=1, y=90)
email.place(x=1, y=120)
phone.place(x=1, y=150)
add.place(x=1, y=180)

#variable for storing data
namevalue=StringVar
entryvalue=StringVar
emailvalue=StringVar
phonevalue=StringVar
addvalue=StringVar
checkvalue=IntVar

#creating entry filed
nameentry = Entry(root, textvariable=namevalue )
entryentry = Entry(root, textvariable=entryvalue, show='*')
emailentry = Entry(root, textvariable=emailvalue )
phoneentry = Entry(root, textvariable=phonevalue )
addentry = Entry(root, textvariable=addvalue )

#packing entry fields
nameentry.place(x=70, y=60)
entryentry.place(x=70,y=90)
emailentry.place(x=70, y=120)
phoneentry.place(x=70, y=150)
addentry.place(x=70, y=180)

#checking
checkbtn = Checkbutton(text="remember me?", variable= checkvalue)
checkbtn.place(x=70,y=220)

Button(text="Submit information", command=getvals).place(x=70,y=250)
 
root.mainloop()