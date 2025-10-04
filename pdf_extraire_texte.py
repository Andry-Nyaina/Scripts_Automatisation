from PyPDF2 import PdfWriter, PdfReader


f = open("recap.pdf", "rb")
reader = PdfReader(f)

page0 = reader.pages[1]
texte = page0.extract_text()

f.close

print(texte)