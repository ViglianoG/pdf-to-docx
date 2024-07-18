from pdf2docx import Converter

pdf_file = "./Storage/PDF_to_DOCX_EXAMPLE.pdf"

docx_file = "./Storage/PDF_to_DOCX_EXAMPLE.docx"

cv = Converter(pdf_file)

cv.convert(docx_file, start=0, end=None)

cv.close