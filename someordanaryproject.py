import pytesseract
import os
import os.path
from pytesseract import image_to_string
from PIL import Image

#locate tesseract on computer
pytesseract.pytesseract.tesseract_cmd = 'C:/Users/Windoof/AppData/Local/Tesseract-OCR/tesseract.exe'

#variables
img = "text_bild2.PNG"
testtxt = "testfile1.txt"

#convert image to string
#x = image_to_string(Image.open(img))

#functions
def readfile():
    file = open(testtxt,"r") 
    print(file.read())
    file.close()
def writefile():
    file = open(testtxt,"w") 
    file.write(""+image_to_string(Image.open(img)))
    file.close() 
def deletetxtfile():
    os.remove(testtxt)
def answerwantdelete():
    varanswerwantdelete = input("\n moechtest du die Textdatei loeschen? y/n: ")
    if varanswerwantdelete == "y":
        print("Textdatei wurde gelöscht!")
        deletetxtfile()
        pass
    elif varanswerwantdelete == "n":
        print("lasse Textdatei erstellt...")
        pass
    else:
        print("verstehe deine Antwort nicht, bitte schreibe y oder n")
        pass

#write text from the image into document or just read it
if not os.path.isfile(testtxt):
    print("Textdatei wird erstellt und ausgegeben\n")
    writefile()
    readfile()
else:
    print("Textdatei wurde nicht erstellt weil sie existiert und wird nun ausgelesen\n")
    readfile()
pass
answerwantdelete() 