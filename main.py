from logging import disable
import os
from tkinter import *
from array import *
from tkinter.font import BOLD
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import filedialog

#Functionlity-----------
#openpdf-----
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter import simpledialog
from view_pdf import ShowPdf
#endopenpdf------
from decrypt_functionality import decryption
from encrypt_functionality import encryption
from rotate_functionality import rotate_pdf
from extract_image_functionality import extract_image
from split_pdf_functionality import split_pdf
from text_to_audio_functionality import text_to_audio
from play_audio_sound import *
from marge_pdf_functionality import marge_pdf
from watermark_functionality import add_watermark
import PyPDF2
# Import the gTTS module for text  
# to speech conversion 
from gtts import gTTS   
# This module is imported so that we can  
# play the converted audio  
from playsound import playsound
# for extracting text
import io
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage  
from typing import Text
from PyPDF2.pdf import PdfFileReader



#other files


# color = {"color": "#6C63FF", "orange": "#6C63FF", "darkorange": "#6C63FF"}

#Window
W=tk.Tk()
W.configure(bg="#c1c1c1")
#W.state('zoomed')

W.attributes('-fullscreen', True)
#W.geometry("%dx%d" % (W.winfo_screenwidth(), W.winfo_screenheight()-40))
#no title bar
#W.overrideredirect(True)
# setting the minimum size of the root window
#W.minsize(800, 600)
W.title("PDF Expert")
W.iconbitmap('icon.ico')


#Defining fuctionality--------------------------------------------------------------

#Open pdf file----------------------
temp=0 
filename=""
v1 = ShowPdf()

def show(filename):
    for widget in frame.winfo_children():
       widget.destroy()
       disable()
       Current_file.config(state=DISABLED)
    frame.pack()

    if(v1.pdf_is_encrypted(filename)):
        
        password =simpledialog.askstring("Password", "Enter password:", show='*')
        try:
            v2 = v1.pdf_view(frame,pdf_location =filename,password=password)
            v2.pack()
        except:
            messagebox.showerror('PDF Expert', 'Incorrect password')
            return ''
    else:
        v2 = v1.pdf_view(frame,pdf_location =filename)
        normalize()
        Current_file.config(state=NORMAL)
        v2.pack()
        
    
def Open_pdf():
    global filename
    cwd = os.getcwd()
    filename = fd.askopenfilename()
    global temp
    temp=0 
    show(filename)

def zoom():
    v1.zoom()
    show(filename)
def zoom_In():
    v1.zoom_in()
    show(filename)
    
def zoom_Out():
    if(v1.zoom_out()):
        messagebox.showerror('Pdf Expert', 'Not allow zoom')
    else:
        show(filename)

def clear_pdf():
    frame.pack_forget()

frame = tk.Frame(W)
frame.place()   



#text to audio functionlity-----------------------------

#play audio functionlity-----------------------------
def playaudio(save_path,save_name):
    # Play the exam.mp3 file  
    playsound(save_name+".mp3") 

#pdf to text functionlity-----------------------------
extracted_text=0
def pdf_to_text(file_path):
    
    global extracted_text
    def convert_pdf_to_txt(path):
        '''Convert pdf content from a file path to text

        :path the file path
        '''
        rsrcmgr = PDFResourceManager()
        codec = 'utf-8'
        laparams = LAParams()

        with io.StringIO() as retstr:
            with TextConverter(rsrcmgr, retstr, codec=codec,
                            laparams=laparams) as device:
                with open(path, 'rb') as fp:
                    interpreter = PDFPageInterpreter(rsrcmgr, device)
                    password = ""
                    maxpages = 0
                    caching = True
                    pagenos = set()

                    for page in PDFPage.get_pages(fp,
                                                pagenos,
                                                maxpages=maxpages,
                                                password=password,
                                                caching=caching,
                                                check_extractable=True):
                        interpreter.process_page(page)

                    return retstr.getvalue()


    
    
    extracted_text=convert_pdf_to_txt(file_path)
    #print(extracted_text) 

#text to text file-------------------------------------------
def text_to_text_file(save_path,save_name,extracted_text):
    with open(save_path+"/"+save_name+".txt", 'w') as f:
        f.write(extracted_text)
    
#bar functionality---------------------

def bar_rotate():
    global temp
    try:
        if temp==0:
            rotate_pdf(filename,"cache","temp",90)
            temp=temp+1
        else:
            rotate_pdf("cache/temp.pdf","cache","temp",90)
            
        show("cache/temp.pdf")
    except PyPDF2.utils.PdfReadError:
        
        messagebox.showerror('PDF Expert', "Getting truble to rotate, You can try PDF tools in side menu for rotation.(error: PdfReadError)")
state="play"

def bar_play_audio():
    pdf_to_text(filename)
    # print("extracted text:"+str(extracted_text))
    # print("filename:"+str(filename))
    global state
    if state=="play":
        i="pause.png"
        img = Image.open("img/"+i)
        resized_image= img.resize((35,35), Image.ANTIALIAS)
        icon[i]= ImageTk.PhotoImage(resized_image)
        state="pause"
        button_dict["stop.png"].config(state=NORMAL) 
        button_dict["play.png"].config(text=" "+i[-0:-4].capitalize()+" ",image=icon[i]) 
        read(extracted_text)
        
    elif state=="pause":
        i="play.png"
        img = Image.open("img/"+i)
        resized_image= img.resize((35,35), Image.ANTIALIAS)
        icon[i]= ImageTk.PhotoImage(resized_image)
        state="unpause"
        button_dict["play.png"].config(text=" "+i[-0:-4].capitalize()+" ",image=icon[i])
        button_dict["stop.png"].config(state=NORMAL)  
        pause()
    elif state=="unpause":
        i="pause.png"
        img = Image.open("img/"+i)
        resized_image= img.resize((35,35), Image.ANTIALIAS)
        icon[i]= ImageTk.PhotoImage(resized_image)
        state="pause"
        button_dict["play.png"].config(text=" "+i[-0:-4].capitalize()+" ",image=icon[i])
        button_dict["stop.png"].config(state=NORMAL) 
        unpause()
def bar_stopit():
    i="play.png"
    img = Image.open("img/"+i)
    resized_image= img.resize((35,35), Image.ANTIALIAS)
    icon[i]= ImageTk.PhotoImage(resized_image)
    
    button_dict["play.png"].config(text=" "+i[-0:-4].capitalize()+" ",image=icon[i])
    global state
    state="play"
    button_dict["stop.png"].config(state=DISABLED) 
    stop()   


#-----------------exception functionality---------------------------

#export to audio-----------
def export_to_audio(file_path,save_path,save_name):
    msg_sep.config(text="Wait pdf processing for text...",bg="#1c1c1c")
    pdf_to_text(file_path)

    msg_sep.config(text="Wait audio processing...",bg="#1c1c1c")
    #print("Extracted text:-",extracted_text)
    text_to_audio(extracted_text,save_path,save_name)

    #msg_sep.config(text="Wait playing audio...",bg="#1c1c1c")
    #play_audio(save_path+"/"+save_name+".mp3")
    msg_sep.config(text="Done.",bg="#14c917")
#extract text-------------
def extract_to_text(file_path,save_path,save_name):
    msg_sep.config(text="Wait pdf processing for text...",bg="#1c1c1c")
    pdf_to_text(file_path)

    msg_sep.config(text="Wait txt file processing...",bg="#1c1c1c")
    #print("Extracted text:-",extracted_text)
    text_to_text_file(save_path,save_name,extracted_text)

    msg_sep.config(text="Done.",bg="#14c917")
    os.system(save_path+"/"+save_name+".txt")



#End Defining functionality---------------------------------------------------------



btnState = False
#loading Navbar icon image:
navIcon = PhotoImage(file="menu.png")
# setting switch function:
def switch():
    global btnState
    if btnState is True:
        
        navbarBtn["state"] = "disabled"
        # create animated Navbar closing:
        for x in range(301):
            navRoot.place(x=-x, y=0)
            topFrame.update()
            

        # resetting widget colors:
      
        topFrame.config(bg="#FFF")
        W.config(bg="#c1c1c1")

        # turning button OFF:
        btnState = False
        navbarBtn["state"] = "normal"
    elif btnState is False:
        # make W dim:
     
        topFrame.config(bg="#FFF")
        W.config(bg="#c1c1c1")

        
        navbarBtn["state"] = "disabled"
        # created animated Navbar opening:
        for x in range(-300, 0, 5):
            navRoot.place(x=x, y=0)
            topFrame.update()

        # turing button ON:
        btnState = True
        navbarBtn["state"] = "normal"

# setting Navbar frame:
navRoot = tk.Frame(W, bg="#FFF", height=1000, width=300)
navRoot.place(x=-300, y=0)


# top Navigation bar:
topFrame = tk.Frame(W, bg="#FFF")
topFrame.pack(side="top", fill=tk.X)

# Header label text:
#homeLabel = tk.Label(topFrame,bg="#FFF", fg="gray1", height=3, padx=20)
#homeLabel.pack(side="right")


# Menu
tk.Label(navRoot,text="Menu", font="Calibri 20 bold", bg="#6C63FF", fg="#FFF", height=1, width=17, padx=19).place(x=10, y=51)

# set y-coordinate of Navbar widgets:
y = 95
# option in the navbar:
menubtn_dict={}
options = ['Open File', 'Print', 'Close', 'Exit']


#massage box
msgframe = tk.Frame(W, bg="#1c1c1c", height=500, width=500)
#custome close button on frame
close_btn = Button(msgframe, text="  x  ",relief="flat",  command= msgframe.place_forget, bg="#1c1c1c",fg="#6C63FF" ,font =
               ('calibri', 25, BOLD),borderwidth=0, activebackground="#1c1c1c", activeforeground="#6C63FF")
close_btn.place(rely=0.0, relx=1.0, x=0, y=0, anchor="ne")
topic = tk.Label(msgframe,relief="flat", bg="#1c1c1c",fg="#6C63FF" ,font =('calibri', 25, BOLD),borderwidth=0, activebackground="#1c1c1c", activeforeground="#6C63FF")
sep= tk.Label(msgframe,relief="flat", bg="#6C63FF",fg="#1c1c1c",width=500 )   
sep.place(x=0,y=60)
msg_sep=tk.Label(msgframe,text="msg (msg_sep)",relief="flat",font =('calibri', 10, BOLD), bg="#6C63FF",fg="#FFF",width=71)
msg_sep.place(x = 0,y =479)

#open_file

first_file=""
def open_file():
    global first_file
    first_file= filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files","*.pdf"),("All Files","*.*")))
    if first_file=="":
        test = type(first_file)
        #print(test)
        #print(first_file)
        file_path.configure(state='normal')
        file_path.delete(0.0,END)
        file_path.insert(0.0,first_file)
        file_path.configure(state='disabled')
    else:
        test = type(first_file)
        #print(test)
        #print(first_file)
        file_name= r"'"+first_file+"'"
        file_path.configure(state='normal')
        file_path.delete(0.0,END)
        file_path.insert(0.0,first_file)
        file_path.configure(state='disabled')

#secondary open_file-------
second_file=""
def open_secondry_file():
    global second_file
    second_file= filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files","*.pdf"),("All Files","*.*")))
    if second_file=="":
        test = type(second_file)
        #print(test)
        #print(second_file)
        secondry4.configure(state='normal')
        secondry4.delete(0.0,END)
        secondry4.insert(0.0,second_file)
        secondry4.configure(state='disabled')
    else:
        test = type(second_file)
        #print(test)
        #print(second_file)
        file_name= r"'"+second_file+"'"
        secondry4.configure(state='normal')
        secondry4.delete(0.0,END)
        secondry4.insert(0.0,second_file)
        secondry4.configure(state='disabled')


#open_folder
folder=""
def open_folder():
    global folder
    folder= filedialog.askdirectory(title="Select a Folder")
    if folder=="":
        folder_path.configure(state='normal')
        folder_path.delete(0.0,END)
        folder_path.insert(0.0,folder)
        folder_path.configure(state='disabled')
        #print(folder)
    else:
        #print(folder)
        folder_path.configure(state='normal')
        folder_path.delete(0.0,END)
        folder_path.insert(0.0,folder)
        folder_path.configure(state='disabled')

#SelectFile---------------
# Add a Label widget
Label(msgframe, text="Select PDF Files:", relief="flat", bg="#1c1c1c",fg="#6C63FF" ,font =('calibri', 15, BOLD)).place(x=20,y=100)

def insert_filepath():
    file_path.configure(state='normal')
    file_path.delete(0.0,END)
    file_path.insert(0.0,filename)
    file_path.configure(state='disabled')
# Create a Button
Current_file=tk.Button(msgframe, text="Current File", command=insert_filepath,width="10", bg="#6C63FF",fg="#1c1c1c" ,font =('calibri', 12,BOLD),state=DISABLED)
Current_file.place(x=290,y=95)
tk.Button(msgframe, text="Browse", command=open_file,width="10", bg="#6C63FF",fg="#1c1c1c" ,font =('calibri', 12, BOLD)).place(x=385,y=95)
file_path=tk.Text(msgframe,highlightthickness=2,highlightcolor= "#6C63FF", bg="#1c1c1c",fg="#fff",width=56,height=2,wrap=CHAR)
file_path.place(x=20,y=140)
file_path.configure(state='disabled')
#Selectfolder-------------
# Add a Label widget
select_folder_btn=Label(msgframe, text="Select Folder To Save:", relief="flat", bg="#1c1c1c",fg="#6C63FF" ,font =('calibri', 15, BOLD))
select_folder_btn.place(x=20,y=197)
# Create a Button

browse_btn=tk.Button(msgframe, text="Browse", command=open_folder,width="10", bg="#6C63FF",fg="#1c1c1c" ,font =('calibri', 12, BOLD))
browse_btn.place(x=385,y=192)
folder_path=tk.Text(msgframe,highlightthickness=2,highlightcolor= "#6C63FF", bg="#1c1c1c",fg="#FFF",width=56,height=2,wrap=CHAR)
folder_path.place(x=20,y=238)
folder_path.configure(state='disabled')
#Selectname-------------
# Add a Label widget
savename_label=Label(msgframe, text="Save As Name:", relief="flat", bg="#1c1c1c",fg="#6C63FF" ,font =('calibri', 15, BOLD))
savename_label.place(x=20,y=290)
save_as_name=StringVar()
savename_entry=tk.Entry(msgframe,textvariable=save_as_name,highlightthickness=2,highlightcolor= "#6C63FF", bg="#1c1c1c",fg="#FFF",width=20,font =('calibri', 15))
savename_entry.place(x=175,y=290)
extention=tk.Label(msgframe, text=".pdf", relief="flat", bg="#1c1c1c",fg="#6C63FF" ,font =('calibri', 15, BOLD))
extention.place(x=385,y=290)
#generate button------------
generatebtn=tk.Button(msgframe, text="Generate", command=None,width="10", bg="#6C63FF",fg="#1c1c1c" ,font =('calibri', 12, BOLD))
generatebtn.place(x=385,y=430)
#rotation------------------
rotation1=Label(msgframe, text="Degree of Rotation:", relief="flat", bg="#1c1c1c",fg="#6C63FF" ,font =('calibri', 15, BOLD))

img_msg = Image.open("img/rotatepage1.png")
resized_image_msg= img_msg.resize((25,25), Image.ANTIALIAS)
icon1= ImageTk.PhotoImage(resized_image_msg)

rotate_page=90
def addrotation():
    global rotate_page
    rotate_page= rotate_page + 90
    if rotate_page==450:
        rotate_page=90
    #print(rotate_page)
    rotation2.config(text=rotate_page)

rotation2=tk.Label(msgframe,text="90",anchor="e",width=3,relief="flat", bg="#1c1c1c",fg="#FFF" ,font =('calibri', 15))

rotation3=tk.Label(msgframe, text=chr(176), relief="flat", bg="#1c1c1c",fg="#6C63FF" ,font =('calibri', 15, BOLD))

rotation4=tk.Button(msgframe, image=icon1, command=addrotation,width="25", bg="#6C63FF",fg="#1c1c1c",state=NORMAL)
def onrotation():
    rotation1.place(x=20,y=335)
    rotation2.place(x=325,y=335)
    rotation3.place(x=360,y=335)
    rotation4.place(x=385,y=335)
def offrotation():
    rotation1.place_forget()
    rotation2.place_forget()
    rotation3.place_forget()
    rotation4.place_forget()
#secondry file--------------
# Add a Label widget
secondry1=Label(msgframe, text="Select PDF Another File:", relief="flat", bg="#1c1c1c",fg="#6C63FF" ,font =('calibri', 15, BOLD))

# Create a Button
secondry2=tk.Button(msgframe, text="Current File", command=None,width="10", bg="#6C63FF",fg="#1c1c1c" ,font =('calibri', 12,BOLD))
secondry3=tk.Button(msgframe, text="Browse", command=open_secondry_file,width="10", bg="#6C63FF",fg="#1c1c1c" ,font =('calibri', 12, BOLD))
secondry4=tk.Text(msgframe,highlightthickness=2,highlightcolor= "#6C63FF", bg="#1c1c1c",fg="#FFF",width=56,height=2,wrap=CHAR)
secondry4.configure(state='disabled')
def onsecondry_file():
    secondry1.place(x=20,y=335)
    secondry2.place(x=290,y=335)
    secondry3.place(x=385,y=335)
    secondry4.place(x=20,y=379)
def offsecondry_file():
    secondry1.place_forget()
    secondry2.place_forget()
    secondry3.place_forget()
    secondry4.place_forget()

#Encrypt/Decript--------------
password1=Label(msgframe, text="Password:", relief="flat", bg="#1c1c1c",fg="#6C63FF" ,font =('calibri', 15, BOLD))
password2=tk.Entry(msgframe,show="*",highlightthickness=2,highlightcolor= "#6C63FF", bg="#1c1c1c",fg="#fff",width=20,font =('calibri', 15))
def show_password():
    if password2.cget('show') == '':
        password2.config(show='*')
        password3.config(text='Show')
    else:
        password2.config(show='')
        password3.config(text='Hide')
password3=tk.Button(msgframe, text="Show", command=show_password,width="10", bg="#6C63FF",fg="#1c1c1c" ,font =('calibri', 12, BOLD))
password4=Label(msgframe, text="Confirm Pass:", relief="flat", bg="#1c1c1c",fg="#6C63FF" ,font =('calibri', 15, BOLD))
password5=tk.Entry(msgframe,show="*",highlightthickness=2,highlightcolor= "#6C63FF", bg="#1c1c1c",fg="#fff",width=20,font =('calibri', 15))
CheckVar1 = IntVar()
def disable_folder():
    select_folder_btn.config(state=DISABLED)
    browse_btn.config(state=DISABLED,bg="#c1c1c1")
    folder_path.configure(highlightcolor= "#c1c1c1")
    savename_label.config(state=DISABLED)
    savename_entry.config(state=DISABLED)
    savename_entry.configure(highlightcolor= "#c1c1c1")
    extention.config(state=DISABLED)
def enable_folder():
    select_folder_btn.config(state=NORMAL)
    browse_btn.config(state=NORMAL,bg="#6C63FF")
    folder_path.configure(highlightcolor= "#6C63FF")
    savename_label.config(state=NORMAL)
    savename_entry.config(state=NORMAL)
    savename_entry.configure(highlightcolor= "#6C63FF")
    extention.config(state=NORMAL)
    


def checked():
    if CheckVar1.get()==1:
        enable_folder()
    else:
        disable_folder()

password6=Checkbutton(msgframe, text = "Generate separate file",command=checked, variable = CheckVar1,onvalue = 1, offvalue = 0, activebackground="#1c1c1c",activeforeground="#6C63FF",font =('calibri', 15, BOLD),bg="#1c1c1c",fg="#6C63FF" )
def onpassword():
    password1.place(x=20,y=335)
    password2.place(x=175,y=335)
    password3.place(x=385,y=335)
    password6.place(x=20,y=430)
    password6.deselect()
    disable_folder()
def onconfirm_password():
    password4.place(x=20,y=382)
    password5.place(x=175,y=382)
def offpassword():
    password1.place_forget()
    password2.place_forget()
    password3.place_forget()
    password4.place_forget()
    password5.place_forget()
    password6.place_forget()
    enable_folder()
def offconfirm_password():
    password4.place_forget()
    password5.place_forget()

#check fields------------------------
def check_basic_field():
    if first_file=="" or folder=="" or save_as_name.get()=="":
        return 0
    else: 
        return 1

#buttons functionality---------------

#rotate btn----
def rotate_btn():
    check_basic = check_basic_field()
    if check_basic==1:
        msg_sep.config(text="Processing...",bg="#1c1c1c")
        rotate_pdf(first_file,folder,save_as_name.get(),rotate_page)
        msg_sep.config(text="Done",bg="#14c917")
    else:
        msg_sep.config(text="Fill all fields",bg="#D0342C")
#export_to_audio_btn----
def export_to_audio_btn():
    check_basic = check_basic_field()
    if check_basic==1:
        msg_sep.config(text="Processing...",bg="#1c1c1c")
        export_to_audio(first_file,folder,save_as_name.get())
        msg_sep.config(text="Done",bg="#14c917")
    else:
        msg_sep.config(text="Fill all fields",bg="#D0342C")
    
#extract_to_text_btn----
def extract_to_text_btn():
    check_basic = check_basic_field()
    if check_basic==1:
        msg_sep.config(text="Processing...",bg="#1c1c1c")
        extract_to_text(first_file,folder,save_as_name.get())
        msg_sep.config(text="Done",bg="#14c917")
    else:
        msg_sep.config(text="Fill all fields",bg="#D0342C")
#extract_image_btn----
def extract_image_btn():
    check_basic = check_basic_field()
    if check_basic==1:
        msg_sep.config(text="Processing...",bg="#1c1c1c")
        extract_image(first_file,folder,save_as_name.get())
        msg_sep.config(text="Done",bg="#14c917")
    else:
        msg_sep.config(text="Fill all fields",bg="#D0342C")
#marge_pdf_btn----
def marge_pdf_btn():
    check_basic = check_basic_field()
    if check_basic==1 and second_file!="":
        msg_sep.config(text="Processing...",bg="#1c1c1c")
        marge_pdf(first_file,folder,save_as_name.get(),second_file)
        msg_sep.config(text="Done",bg="#14c917")
    else:
        msg_sep.config(text="Fill all fields",bg="#D0342C")
#split_pdf_btn----
def split_pdf_btn():
    check_basic = check_basic_field()
    if check_basic==1:
        msg_sep.config(text="Processing...",bg="#1c1c1c")
        split_pdf(first_file,folder,save_as_name.get())
        msg_sep.config(text="Done",bg="#14c917")
    else:
        msg_sep.config(text="Fill all fields",bg="#D0342C")   
#add_watermark_btn----
def add_watermark_btn():
    check_basic = check_basic_field()
    if check_basic==1 and second_file!="":
        msg_sep.config(text="Processing...",bg="#1c1c1c")
        add_watermark(first_file,folder,save_as_name.get(),second_file)
        msg_sep.config(text="Done",bg="#14c917")
    else:
        msg_sep.config(text="Fill all fields",bg="#D0342C")

#encrypt btn----
def encrypt_btn():
    check_basic = check_basic_field()
    try:
        if CheckVar1.get()==1:
            if check_basic==1 and password2.get()!="" and password5.get()!="":
                if password2.get()==password5.get():
                        msg_sep.config(text="Processing...",bg="#1c1c1c")
                        encryption(first_file,folder,save_as_name.get(),password2.get(),CheckVar1.get())
                        msg_sep.config(text="Your encrypted file stored to you decleared path",bg="#14c917")    
                    
                else:
                    msg_sep.config(text="Recheck password you have entered",bg="#D0342C")
            else:
                msg_sep.config(text="Fill all fields",bg="#D0342C")
        else:
            if first_file!="" and password2.get()!="" and password5.get()!="":
                if password2.get()==password5.get():
                        msg_sep.config(text="Processing...",bg="#1c1c1c")
                        encryption(first_file,folder,save_as_name.get(),password2.get(),CheckVar1.get())
                        msg_sep.config(text="Your file is Encrypted",bg="#14c917")    
                    
                else:
                    msg_sep.config(text="Recheck password you have entered",bg="#D0342C")
            else:
                msg_sep.config(text="Fill all fields",bg="#D0342C")
    except PyPDF2.utils.PdfReadError:
        msg_sep.config(text="File is already Encrypted(*You need to decrypt it first*)",bg="#D0342C")

#decrypt btn----
def decrypt_btn():
    check_basic = check_basic_field()
    try:
        if CheckVar1.get()==1:
            if check_basic==1 and password2.get()!="":
                
                msg_sep.config(text="Processing...",bg="#1c1c1c")
                decryption(first_file,folder,save_as_name.get(),password2.get(),CheckVar1.get())
                msg_sep.config(text="Your decrypted file stored to you decleared path",bg="#14c917")    
            
                
            else:
                msg_sep.config(text="Fill all fields",bg="#D0342C")
        else:
            if first_file!="" and password2.get()!="":
        
                msg_sep.config(text="Processing...",bg="#1c1c1c")
                decryption(first_file,folder,save_as_name.get(),password2.get(),CheckVar1.get())
                msg_sep.config(text="Your file is decrypted",bg="#14c917")    
            
                
            else:
                msg_sep.config(text="Fill all fields",bg="#D0342C")
    except PyPDF2.utils.PdfReadError:
        msg_sep.config(text="You entered incorrect password",bg="#D0342C")

    except KeyError:
        msg_sep.config(text="File is not Encrypted(*You need to encrypt it first*)",bg="#D0342C")
        

                         

def msg(msg_title):
    if msg_title=="Open File" or msg_title=="Print" or msg_title=="Close" or msg_title=="Exit":
        if msg_title=="Open File":
            msgframe.place_forget()
            Open_pdf()
            #print("open File")
        elif msg_title=="Print":
            msgframe.place_forget()
            messagebox.showerror('PDF Expert', 'Printer not found.')
        elif msg_title=="Close":
            msgframe.place_forget()
            clear_pdf()
            disable()
            #print("close")
        elif msg_title=="Exit":
            msgframe.place_forget()
            W.destroy()
            #print("exit")



    else:
        msgframe.place_forget()
        topic.config(text=msg_title.title())
        topic.place(x=20,y=12)
        msgframe.place(anchor="c", relx=.5, rely=.5)
        
        if msg_title=="Rotate":
            msg_sep.config(text="",bg="#6C63FF")
            extention.config(text=".pdf")
            onrotation()
            offsecondry_file()
            offpassword()
            generatebtn.config(command=rotate_btn)
        elif msg_title=="Export as Audio":
            msg_sep.config(text="",bg="#6C63FF")    
            extention.config(text=".mp3")
            offrotation()
            offsecondry_file()
            offpassword()
            generatebtn.config(command=export_to_audio_btn)

        elif msg_title=="Extract only text":
            msg_sep.config(text="",bg="#6C63FF")    
            extention.config(text=".txt")
            offrotation()
            offsecondry_file()
            offpassword()
            generatebtn.config(command=extract_to_text_btn)
        elif msg_title=="Extract only images":
            msg_sep.config(text="",bg="#6C63FF")    
            extention.config(text="(pn-n).png")
            offrotation()
            offsecondry_file()
            offpassword()
            generatebtn.config(command=extract_image_btn)
        elif msg_title=="Marge":
            msg_sep.config(text="",bg="#6C63FF")    
            extention.config(text=".pdf")
            offrotation()
            onsecondry_file()
            offpassword()
            generatebtn.config(command=marge_pdf_btn)
        elif msg_title=="Split":
            msg_sep.config(text="",bg="#6C63FF")    
            extention.config(text="(n).pdf")
            offrotation()
            offsecondry_file()
            offpassword()
            generatebtn.config(command=split_pdf_btn)
        elif msg_title=="Add Watermark":
            msg_sep.config(text="",bg="#6C63FF")    
            extention.config(text=".pdf")
            offrotation()
            onsecondry_file()
            offpassword()
            generatebtn.config(command=add_watermark_btn)
        elif msg_title=="Encrypt":
            msg_sep.config(text="",bg="#6C63FF")    
            extention.config(text=".pdf")
            offrotation()
            offsecondry_file()
            onpassword()
            onconfirm_password()
            generatebtn.config(command=encrypt_btn)

        elif msg_title=="Decrypt":
            msg_sep.config(text="",bg="#6C63FF")    
            extention.config(text=".pdf")
            offrotation()
            offsecondry_file()
            onpassword()
            offconfirm_password()
            generatebtn.config(command=decrypt_btn)
    
    

#configuring nav options:

def functionality(msg_title):
    msg(msg_title)
    #print(msg_title+"nav")


# Navbar Option Buttons:
for i in options:
    def func(x=i):
      return functionality(x)
    menubtn_dict[i]=tk.Button(navRoot,  text=i,command=func, width=29,font="calibri 15 bold",anchor="w", bg="#FFF", fg="#6C63FF",bd=0,activebackground="#6C63FF", activeforeground="#FFF")
    menubtn_dict[i].place(x=10, y=y)
    y += 40

# Tools
tk.Label(navRoot,text="PDF Tools", font="Calibri 20 bold", bg="#6C63FF", fg="#FFF", height=1, width=17, padx=19).place(x=10, y=256)

y=300
toolbtn_dict={}
options = ["Rotate","Export as Audio", "Extract only text","Extract only images","Marge","Split","Add Watermark","Encrypt","Decrypt"]
for i in options:
    def func(x=i):
      return functionality(x)
    menubtn_dict[i]=tk.Button(navRoot,  text=i,command=func, width=29,font="calibri 15 bold",anchor="w", bg="#FFF", fg="#6C63FF",bd=0,activebackground="#6C63FF", activeforeground="#FFF")
    menubtn_dict[i].place(x=10, y=y)
    y += 40

# Navbar button:
navbarBtn = tk.Button(W, image=navIcon, bg="#FFF",activebackground="#FFF", bd=0, padx=20,command=switch)
navbarBtn.place(x=10, y=13)
#img = Image.open('icon.png')
#Resize the Image using resize method
#resized_image= img.resize((45,45), Image.ANTIALIAS)
#new_image= ImageTk.PhotoImage(resized_image)
pdfExpert = tk.Label(W, 
                  text = "PDF EXPERT",bg="#fff",fg="#6C63FF",font="Nova 20 bold").place(x = 45,
                                           y = 8)

ESearch = Entry(W, width=13,font="Consolas 22",bg="#c1c1c1")
ESearch.place(x=240,y=6)
ESearch.config(state=DISABLED)

def normalize():
    ESearch.config(state=NORMAL)
    button_dict["search.png"].config(state=NORMAL)
    button_dict["zoomin.png"].config(state=NORMAL)
    button_dict["zoomout.png"].config(state=NORMAL)
    button_dict["fitScreen.png"].config(state=NORMAL)
    button_dict["rotate.png"].config(state=NORMAL)
    button_dict["play.png"].config(state=NORMAL)
    
def disable():
    ESearch.config(state=DISABLED)
    button_dict["search.png"].config(state=DISABLED)
    button_dict["zoomin.png"].config(state=DISABLED)
    button_dict["zoomout.png"].config(state=DISABLED)
    button_dict["fitScreen.png"].config(state=DISABLED)
    button_dict["rotate.png"].config(state=DISABLED)
    button_dict["play.png"].config(state=DISABLED)


def bar_functionality(a):
    msgframe.place_forget()

    if a=="search.png":
        print("searchclicked")
    elif a=="zoomin.png":
        zoom_In()
    elif a=="zoomout.png":
        zoom_Out()
    elif a=="fitScreen.png":
        zoom()
    elif a=="rotate.png":
        bar_rotate()
    elif a=="play.png":
        bar_play_audio()
    elif a=="stop.png":
        bar_stopit()

    #print(a+"icon")
x = 460
button_dict={}
icon={}
options = ['search.png', 'zoomin.png', 'zoomout.png','fitScreen.png','rotate.png','play.png','stop.png']
for i in options:
    img = Image.open("img/"+i)
    resized_image= img.resize((35,35), Image.ANTIALIAS)
    icon[i]= ImageTk.PhotoImage(resized_image)
    #img_label = Label(image=icon[i])
    def func(x=i):
      return bar_functionality(x)

    # if i=="zoomin.png":
    #     #side line
    #     side_line= Label(topFrame,text="|",font="arial 22",bg="#FFF",fg="#1c1c1c", relief="flat")
    #     side_line.place(x=x-0,y=0)
    #     #x +=22
    # elif i=="zoomout.png":
    #     x=x-0
    button_dict[i]=tk.Button(W,text=" "+i[-0:-4].capitalize()+" " ,width="130", image=icon[i],compound=LEFT,command=func ,font="calibri 15 bold", bg="#6C63FF", fg="#1c1c1c",bd=0,activebackground="#c1c1c1", activeforeground="#6C63FF")
    button_dict[i].place(x=x, y=5)
    button_dict[i].config(state=DISABLED)
    # if i=="zoomout.png":
    #     #side line
    #     #x +=22
    #     side_line= Label(topFrame,text="|",font="arial 22",bg="#FFF",fg="#1c1c1c", relief="flat")
    #     side_line.place(x=x+22,y=0)
    x += 138
button_dict["stop.png"].config(state=DISABLED) 
    


closeBtn = tk.Button(topFrame, text=" x ",relief="flat",  command= W.destroy, bg="#ff1919",fg="#1c1c1c" ,font =
               ('Consolas', 19, BOLD),borderwidth=0, activebackground="#ff1919", activeforeground="#FFF")
closeBtn.pack(side=RIGHT)
#checkBtn.place(x=W.winfo_screenwidth()-50,y=0)
minimizeBtn = tk.Button(topFrame, text=" - ",relief="flat",  command= W.iconify, bg="#FFF",fg="#1c1c1c" ,font =
               ('Consolas', 19, BOLD),borderwidth=0, activebackground="#fff", activeforeground="#1c1c1c")
minimizeBtn.pack(side=RIGHT)
#minimizeBtn.place(x=W.winfo_screenwidth()-100,y=0)

W.mainloop()


