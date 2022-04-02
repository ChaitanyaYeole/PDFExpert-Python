try:
    from tkinter import*
    import fitz
    from tkinter.ttk import Progressbar
    from threading import Thread
    import math
except Exception as e:
    print(f"This error occured while importing neccesary modules or library {e}")

class ShowPdf():
    img_object_li = []

    def __init__(self):
        self.zoom()
    def zoom(self):
        self.zoom_x = 1.5
        self.zoom_y = 1.5
        self.pdx=300
    def zoom_in(self):
        self.zoom_x=self.zoom_x+0.1
        self.zoom_y=self.zoom_y+0.1
        self.pdx=self.pdx-30
    def zoom_out(self):
        if self.zoom_x==1.3 or self.zoom_y==1.0:
            return True
        else:
            self.zoom_x=self.zoom_x-0.1
            self.zoom_y=self.zoom_y-0.1
            self.pdx=self.pdx+30
            return False
        
    def pdf_is_encrypted(self,pdf_location):
        pdf = fitz.Document(pdf_location)
        
        return pdf.isEncrypted
    def pdf_view(self,master,width=1200,height=600,bar=True,load="after", pdf_location="",password=None):
        
        self.pdf_location=pdf_location
        frame = Frame(master,width= width,height= height,bg="white")
        scroll_y = Scrollbar(frame,orient="vertical")
        scroll_x = Scrollbar(frame,orient="horizontal")

        scroll_x.pack(fill="x",side="bottom")
        scroll_y.pack(fill="y",side="right")

        self.text = Text(frame,yscrollcommand=scroll_y.set,xscrollcommand= scroll_x.set,padx=self.pdx,width= width,height= height)
      
        self.text.pack(side="left")

        scroll_x.config(command=self.text.xview)
        scroll_y.config(command=self.text.yview)


        def add_img():
            
            if password is not None:
                open_pdf = fitz.Document(pdf_location)
                open_pdf.authenticate(password)
            else:
                open_pdf = fitz.open(self.pdf_location)
            pdf_img=[]
            for page in open_pdf:
                mat = fitz.Matrix(self.zoom_x,self.zoom_y)
                pix = page.getPixmap(matrix=mat)
                pix1 = fitz.Pixmap(pix,0) if pix.alpha else pix
                
                img = pix1.getImageData("ppm")
                timg = PhotoImage(data = img)
                self.img_object_li.append(timg)
                pdf_img.append(timg)
            
            for i in pdf_img:
                self.text.image_create("1.6",image=i)
                self.text.insert(END,"\n\n")

        add_img()

        return frame
            
        