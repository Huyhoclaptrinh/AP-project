from tkinter import *
root=Tk()
root.geometry("400x300")

def getvals():
    print("Accept")

Label(root,text="Register Form",font="ar 17 bold").place(x=4,y=1) 

name = Label(root, text ="Username")
email = Label(root, text ="Email")
phone = Label(root, text ="Phone")
add = Label(root, text ="Address")

name.place(x=1, y=60)
email.place(x=2, y=90)
phone.place(x=3, y=120)
add.place(x=4, y=150)

namevalue=StringVar
emailvalue=StringVar
phonevalue=StringVar
addvalue=StringVar
checkvalue=IntVar

nameentry = Entry(root, textvariable=namevalue )
emailentry = Entry(root, textvariable=emailvalue )
phoneentry = Entry(root, textvariable=phonevalue )
addentry = Entry(root, textvariable=addvalue )

nameentry.place(x=70, y=60)
emailentry.place(x=70, y=90)
phoneentry.place(x=70, y=120)
addentry.place(x=70, y=150)

checkbtn = Checkbutton(text="remember me?", variable= checkvalue)
checkbtn.place(x=70,y=180)

Button(text="Submit information", command=getvals).place(x=70,y=220)
 
root.mainloop()