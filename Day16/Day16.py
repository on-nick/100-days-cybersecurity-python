import PyPDF2
import os

merger = PyPDF2.PdfMerger()

for filename in os.listdir(os.getcwd()):
  if filename.endswith('.pdf'):
    merger.append(filename)
merger.write("merged.pdf")
merger.close()
print("PDF successfully merged!") 
