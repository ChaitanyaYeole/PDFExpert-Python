#Import the required Libraries
from decimal import Rounded
from tkinter import *
from tkinter import font
from tkinter.font import BOLD
from PIL import Image,ImageTk
import time

#Create an instance of tkinter frame
win = Tk()

def main():

    #progress bar
    
    open_file["state"] = "disabled"
    #Progress line
    progress_line= Label(win,width="145",bg="#6C63FF", relief="flat")
    #progress_line.place(x=-1020,y=560)

    #import time
    for x in range(-1020,0,1):
            progress_line.place(x=x, y=560)
            progress_line.update()
            #time.sleep(0.01)

    win.destroy()
    import main

#Set the geometry of tkinter frame
#win.geometry("1000x600")

#center the window
window_height = 570
window_width = 1000
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

#no title bar
win.overrideredirect(True)



#Create a canvas
canvas= Canvas(win, width= 1000, height= 570, bg="white")
canvas.pack()

#custome close button
close_btn = Button(win, text="  x  ",relief="flat",  command= win.destroy, bg="white",fg="#6C63FF" ,font =
               ('calibri', 25, BOLD),borderwidth=0, activebackground="#fff", activeforeground="#6C63FF")
close_btn.place(x=935, y=0)

#Open file button


btn_round = PhotoImage(file='openfilebtn.png')

img_label = Label(image=btn_round)


open_file = Button(win, image=btn_round,relief="flat",text="Open PDF Expert",font=('calibri 32 bold'),  command= main,borderwidth=0,bg="#FFF",fg="#fff",activebackground="#fff")
open_file.place(x=500, y=290)
#x=651, y=410


#Load an image in the script
img= (Image.open("welcome2.png"))


#Resize the Image using resize method
resized_image= img.resize((900,500), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(50,50, anchor=NW, image=new_image)

#bottom line
bottom_line= Label(win,width="145",bg="#c1c1c1", relief="flat")
bottom_line.place(x=0,y=560)

for x in reversed(range(500,550)):
            
            if x>540:
                time.sleep(0)
                open_file["state"] = "disabled"
            elif x>520:
                time.sleep(0)
                open_file["state"] = "normal"
            else:
                time.sleep(0.01)
                open_file["state"] = "normal"
            
            open_file.place(x=x, y=290)
            open_file.update()
            

win.mainloop()