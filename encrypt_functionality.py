# import PdfFileWriter and PdfFileReader
# class from PyPDF2 library
from PyPDF2 import PdfFileWriter, PdfFileReader

def encryption(file_path,save_path,save_name,save_pass,check):

    # create a PdfFileWriter object
    out = PdfFileWriter()

    # Open our PDF file with the PdfFileReader
    file = PdfFileReader(file_path)

    # Get number of pages in original file
    num = file.numPages

    # Iterate through every page of the original
    # file and add it to our new file.
    for idx in range(num):
        
        # Get the page at index idx
        page = file.getPage(idx)
        
        # Add it to the output file
        out.addPage(page)


    # Create a variable password and store
    # our password in it.
    password = save_pass

    # Encrypt the new file with the entered password
    out.encrypt(password)

    # Open a new file "myfile_encrypted.pdf"
    if check==1:
        with open(save_path+"/"+save_name+".pdf", "wb") as f:
            
            # Write our encrypted PDF to this file
            out.write(f)
        
    else:
        with open(file_path, "wb") as f:
        
            # Write our encrypted PDF to this file
            out.write(f)

        

    return save_pass
