import PyPDF2
pdfFile = open('test.pdf', 'rb')

# Create reader and writer object
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()

# Add all pages to writer (accepted answer results into blank pages)
for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

# Encrypt with your password
pdfWriter.encrypt('password')

# Write it to an output file. (you can delete unencrypted version now)
resultPdf = open('encrypted_output.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()
