import pyttsx3
import PyPDF2

# Put the PDF you want to be converted to audiobook here
PDF = open('TheHobbit-converted.pdf', 'rb')
read_through_PDF = PyPDF2.PdfFileReader(PDF)

number_of_pages = read_through_PDF.numPages
print(number_of_pages)

reciter = pyttsx3.init()

# Choose which pages you wish to be read here:
# i.e in this case pages 15-end will be read
for i in range(18, number_of_pages):
    page = read_through_PDF.getPage(i)
    content = page.extractText()
    # get rid of double white spaces for clearer reciting
    text = ' '.join(content.split())
    print(text)
    reciter.say(text)
    reciter.runAndWait()


