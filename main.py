import tkinter as tk 
from tkinter import filedialog, Text 
import os

root = tk.Tk()

canvas = tk.Canvas(root,height=1000,width=1540,bg="#00FFFF")
canvas.pack()
# root.attributes('-fullscreen',True)
frame = tk.Frame(root,bg="white")
frame.place(relwidth=0.8,relheight=0.8, relx=0.1,rely=0.1)

openAdmin = tk.Button(root, text="Admin", padx = 10, pady = 5, fg="red", bg="#000000")
openAdmin.pack()
root.mainloop()