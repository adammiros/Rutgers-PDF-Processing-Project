import os
import subprocess
import time

global pdfFileName

# Created by Adam Miros
pageCount = 1

firstName = input("What is the persons first name? \n")
lastName = input("What is the persons last name? \n")

fileNames = os.listdir(os.getcwd())
for file in fileNames:
    if file.endswith(".pdf"):
            pdfFileName = file
            

cwd = os.getcwd()
fullFileName = os.path.join(cwd, pdfFileName)
print(pdfFileName)

pdftoppmFile = os.path.join(cwd, "PDFTOPPM", "pdftoppm.exe")


subprocess.Popen('"%s" -jpeg "%s" out' % (pdftoppmFile, pdfFileName))

time.sleep(2)


os.rename(os.path.join(cwd ,"out-1.jpg"), lastName + ", " + firstName + "_Page_1.jpeg")
os.rename(os.path.join(cwd ,"out-2.jpg"), lastName + ", " + firstName + "_Page_2.jpeg")

print("All done!")
input("Press Enter to continue...")
