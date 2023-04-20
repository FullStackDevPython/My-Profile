import PyPDF2
path="C:\\Users\\USER\\OneDrive\\Desktop\\uploads\\Mini-Projects\\PdfMerger\\"
pdfiles = [f"{path}1.pdf", f"{path}2.pdf", f"{path}sample.pdf"]
merger=PyPDF2.PdfMerger()

for filename in pdfiles:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write('merged.pdf')    