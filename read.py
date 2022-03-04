# from PyPDF2 import PdfFileWriter, PDFFileReader

# temp = open('teste_pdf.pdf', 'rb')
# PDF_read = PDFFileReader(temp)
# first_page = PDF_read.getPage(0)
# print(first_page.extractText())



import pdfplumber
with pdfplumber.open("teste_pdf.pdf") as temp:
  first_page = temp.pages[0]
  print(first_page.extract_text())