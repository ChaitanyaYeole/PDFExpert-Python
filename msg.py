try:
    from tkinter import*
    
except Exception as e:
    print(f"This error occured while importing neccesary modules or library {e}")

#Create an instance of tkinter window or frame
win= Tk()

#Setting the geometry of window
win.geometry("600x350")

class msgbox():
    def __init__(self, a=""):
    

        
        print(a)
        #Create a Label
        Label(win, text= "Hello World! ",font=('Helvetica bold', 15)).pack(pady=20)

        #Make the window jump above all
        win.attributes('-topmost',True)
#top("hello")
win.mainloop()