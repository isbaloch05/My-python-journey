from pypdf import PdfWriter

merge = PdfWriter()

pdf_paths = [
    "C:/Users/Acer/Desktop/daily practice/x.pdf",
    "C:/Users/Acer/Desktop/daily practice/x.pdf",
    "C:/Users/Acer/Desktop/daily practice/x.pdf",
    "C:/Users/Acer/Desktop/daily practice/x.pdf",
]

for pdfs in pdf_paths:
    merge.append(pdfs)

merge.write("C:/Users/Acer/Desktop/daily practice/merged pdfs.pdf")