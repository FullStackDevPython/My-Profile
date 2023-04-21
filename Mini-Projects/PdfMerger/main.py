import PyPDF2
path="C:\\Users\\USER\\OneDrive\\Desktop\\uploads\\Mini-Projects\\PdfMerger\\"
#Does Not work in VS Code run directly from terminal for better results.
# pdfiles = [f"{path}1.pdf", f"{path}2.pdf", f"{path}sample.pdf"]
pdfiles = ["1.pdf","2.pdf","sample.pdf"]
merger=PyPDF2.PdfMerger()

for filename in pdfiles:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write('merged.pdf')    