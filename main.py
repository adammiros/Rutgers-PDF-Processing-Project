import os
import subprocess
import time

global pdfFileName

# Created by Adam Miros
pageCount = 1

firstName = input("What is the persons first name?")
lastName = input("What is the persons last name?")

fileNames = os.listdir(os.getcwd())
for file in fileNames:
    if file.endswith(".pdf"):
            pdfFileName = file
            

cwd = os.getcwd()
fullFileName = os.path.join(cwd, pdfFileName)
print(pdfFileName)

pdftoppmFile = os.path.join(cwd, "PDFTOPPM", "pdftoppm.exe")


subprocess.Popen('"%s" -png "%s" out' % (pdftoppmFile, pdfFileName))

time.sleep(2)


os.rename(os.path.join(cwd ,"out-1.png"), lastName + ", " + firstName + "_Page_1.jpg")
os.rename(os.path.join(cwd ,"out-2.png"), lastName + ", " + firstName + "_Page_2.jpg")

print("All done!")
input("Press Enter to continue...")
