from tkinter import *

ws = Tk()
ws.geometry('400x300')
ws.title('PythonGuides')
ws['bg']='#5d8a82'

f = ("Times bold", 14)

def nextPage():
    ws.destroy()
    import abc1

def prevPage():
    ws.destroy()
    import search
    
Label(
    ws,
    text="This is First page",
    padx=20,
    pady=20,
    bg='#5d8a82',
    font=f
).pack(expand=True, fill=BOTH)

Button(
    ws, 
    text="Previous Page", 
    font=f,
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws, 
    text="Next Page", 
    font=f,
    command=prevPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()