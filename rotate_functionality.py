# importing the required modules
import PyPDF2
def rotate_pdf(file_path,save_path,save_name,rotation_deg):
    def PDFrotate(origFileName, newFileName, rotation):

        # creating a pdf File object of original pdf
        pdfFileObj = open(origFileName, 'rb')
        
        # creating a pdf Reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        # creating a pdf writer object for new pdf
        pdfWriter = PyPDF2.PdfFileWriter()
        
        # rotating each page
        for page in range(pdfReader.numPages):

            # creating rotated page object
            pageObj = pdfReader.getPage(page)
            pageObj.rotateClockwise(rotation)

            # adding rotated page object to pdf writer
            pdfWriter.addPage(pageObj)

        # new pdf file object
        newFile = open(newFileName, 'wb')
        
        # writing rotated pages to new file
        pdfWriter.write(newFile)

        # closing the original pdf file object
        pdfFileObj.close()
        
        # closing the new pdf file object
        newFile.close()
        #print("pdf rotated")

    


    # original pdf file name
    origFileName = file_path
    
    # new pdf file name
    newFileName = save_path+"/"+save_name+".pdf"
    
    # rotation angle
    rotation = rotation_deg
    #print(file_path,save_path,save_name,rotation_deg)
    # calling the PDFrotate function
    PDFrotate(origFileName, newFileName, rotation)
    
    
    
    