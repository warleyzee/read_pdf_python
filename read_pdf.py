# from re import search
# import PyPDF2



# pdfFileObj = open('test.pdf', 'rb')

# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# pageObj = pdfReader.getPage(0)

# text=(pageObj.extractText())
# text=text.split(",")
# text

# search_keywords=['Cube Ref', 'Cliente Ref', 'Method note 1']

# for sentence in pdfFileObj:
#     lst = []
#     for word in search_keywords:
#         if word in pdfFileObj:
#             lst.append(word)
#     print('{0} key word(s) in sentence: {1}'.format(len(lst), ', '.join(lst)))
#     print(sentence, "\n")

# print(pdfReader.numPages)
# print(text)


import xlrd
book = xlrd.open_workbook("Cube.xlsx")
print ("Número de abas: ", book.nsheets)
print ("Nomes das Planilhas:", book.sheet_names())
sh = book.sheet_by_index(0)
print(sh.name, sh.nrows, sh.ncols)
print("Valor da célula D30 é ", sh.cell_value(rowx=29, colx=3))
for rx in range(sh.nrows):
    print(sh.row(rx))