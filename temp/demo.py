from tkinter import *
from array import *

from PIL import Image,ImageTk
import tkinter
top = tkinter.Tk()

# Code to add widgets will go here...
top.config(bg="gray")
def color(a):
    print(a)
x = 95
button_dict={}
icon={}
options = ['up.png', 'vline.png', 'print.png','menu.png','search.png']
# Navbar Option Buttons:

for i in options:
    icon[i] = PhotoImage(file=i)

    img_label = Label(image=icon[i])
    def func(x=i):
      return color(x)
    button_dict[i]=tkinter.Button(top,  image=icon[i],command=func, width=25,font="calibri 15 bold",anchor="w", bg="#FFF", fg="#6C63FF",bd=0,activebackground="#1c1c1c", activeforeground="#FFF")
    button_dict[i].place(x=x, y=10)
    x += 40
top.mainloop()