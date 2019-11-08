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
        print("lasse Textdatei erstellt und beende das script...")
        pass
    else:
        print("verstehe deine Antwort nicht, bitte schreibe y oder n")
        pass

def answertotakeownpic():
    varanswertotakeownpic = input("\n Beispieldatei benutzen? (text_bild2.PNG) y/n:")
    if varanswertotakeownpic == "y":
        writefile()
        pass
    elif varanswertotakeownpic == "n":
        ownpic = input("\n Bitte Bild im gleichen Ordner legen und den Namen hier eintragen (Beispiel: Bild1.png):")
        if not os.path.isfile(ownpic):
            print("Deine Datei existiert nicht, ich nehme das Beispielfoto!")
            writefile()
            pass
        elif os.path.isfile(ownpic):
            print("Deine Datei wird ausgewertet und in die Textdatei geschrieben.")
            img = ownpic
            #writefile() -> Does not functioning because variables can only get into defs not out of defs
            file = open(testtxt,"w") 
            file.write(""+image_to_string(Image.open(img)))
            file.close()   
        else:
            pass
    else:
        print("Ich verstehe deine Antwort nicht, ich nehme das Beispielfoto!")
        writefile()


#write text from the image into document or just read it
if not os.path.isfile(testtxt):
    answertotakeownpic()
    print("Textdatei wird erstellt und ausgegeben\n")
    readfile()
else:
    print("Textdatei existiert und wird nun ausgelesen, lösche sie um ggf. eine neue einzulesen\n")
    readfile()
pass
answerwantdelete() 