import fitz
def extract_image(file_path,save_path,save_name):
    doc = fitz.open(file_path)
    for i in range(len(doc)):
        for img in doc.getPageImageList(i):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
            if pix.n < 5:       # this is GRAY or RGB
                pix.writePNG(save_path+"/"+save_name+"(%s-%s).png" % (i, xref))
            else:               # CMYK: convert to RGB first
                pix1 = fitz.Pixmap(fitz.csRGB, pix)
                pix1.writePNG(save_path+"/"+save_name+"(%s-%s).png" % (i, xref))
                pix1 = None
            pix = None
    #print("image extracted.")     