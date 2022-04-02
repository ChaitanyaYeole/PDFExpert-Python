# importing required modules
import PyPDF2

def marge_pdf(file_path,save_path,save_name,second_file_path):
    


    def PDFmerge(pdfs, output):
        # creating pdf file merger object
        pdfMerger = PyPDF2.PdfFileMerger()

        # appending pdfs one by one
        for pdf in pdfs:
            pdfMerger.append(pdf)

        # writing combined pdf to output pdf file
        with open(output, 'wb') as f:
            pdfMerger.write(f)
        #print("marged done.")

    # pdf files to merge
    pdfs = [file_path, second_file_path]

    # output pdf file name
    output = save_path+"/"+save_name+".pdf"

    # calling pdf merge function
    PDFmerge(pdfs=pdfs, output=output)
    
        


