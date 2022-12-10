import pyttsx3
import PyPDF2

speaker=pyttsx3.init()

book=open("C:/Users/viole/Downloads/Python for Programmers with Introductory AI Case Studies by Paul Deitel, Harvey Deitel (z-lib.org).pdf","rb")
pdfreader=PyPDF2.PdfFileReader(book)
pages=pdfreader.numPages
print(pages)

for num in range(25,pages):
    page=pdfreader.getPage(num)
    text=page.extract_text()
    speaker.say(text)
    speaker.runAndWait()
