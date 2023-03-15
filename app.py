from PyPDF2 import PdfWriter
import os

merger = PdfWriter()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)

merger.write("combined_file.pdf")
merger.close()