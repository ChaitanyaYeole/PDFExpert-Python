# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open('example.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

num=pdfReader.numPages

for i in range(num):
    print("page",i+1)
    # creating a page object
    pageObj = pdfReader.getPage(i)

    # extracting text from page
    print(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()
