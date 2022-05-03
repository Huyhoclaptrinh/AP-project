from tkinter import *
import tkinter 
import package
from package import admin
from package import user
from PIL import ImageTk,Image
# This is main window for bookstore management
window = Tk()
window.title("Bookstore Management")
window.geometry("1000x800")

bg_image = tkinter.PhotoImage(file= "WinBG.png")
#create label
label = Label(window, image=bg_image)
label.place(x=0, y=0,relwidth=1,relheight=1)
#Creat canvas    
canvas = Canvas(window,width=500, height=500) 
canvas.pack(fill="both", expand=True)
#place image in canvas
canvas.create_image(0,0,image=bg_image,anchor="nw")
#add a label
canvas.create_text(400,250, text="BOOKSTORE MANAGEMENT", font=("Helvetica",20),fill="white")

def resizer(e):
	global bg1, resized_bg, new_bg
	# Open our image 
	bg1 = Image.open("WinBG.png")
	# Resize the image
	resized_bg = bg1.resize((e.width, e.height), Image.LANCZOS)
	# Define our image again
	new_bg = ImageTk.PhotoImage(resized_bg)
	# Add it back to the canvas
	canvas.create_image(0,0, image=new_bg, anchor="nw")
	# Readd the text
	canvas.create_text(500, 250, text="BOOKSTORE MANAGEMENT", font=("Times", 20), fill="black")
   

window.title("Group 16 project")
window.bind('<Configure>', resizer)
bt_admin=Button(window,text="ADMIN",width=20,command=admin.admin_win)
bt_admin.place(x = 200, y =500)
bt_user=Button(window,text="USER",width=20,command=user.user_win)
bt_user.place(x=610, y =500)
window.mainloop() 


window.mainloop() 