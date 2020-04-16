import os
import subprocess
import time

from movetoTemporaryFolder import movetoTemporaryFolder
from deleteFile import deleteFile

def convertPDFToJpeg(firstName, lastName):

    pdfFileName = ""

    #Creating a variable to store path to temporary folder
    temporaryDirectory = os.path.join(os.getcwd(), "temporary")

    #Creating variable to store path to PDFTOPPM Folder which houses EXE (What I use to convert)
    pdftoppmFileDirectory = os.path.join(os.getcwd(), "PDFTOPPM")

    #Grabbing PDF File
    fileNames = os.listdir(temporaryDirectory)
    for file in fileNames:
        if file.endswith(".pdf"):
            pdfFileName = file
            os.rename(os.path.join(temporaryDirectory, pdfFileName), (firstName + "_" + lastName + ".pdf"))

    #Creating the full path to PDFTOPPM.EXE
    pdftoppmFile = os.path.join(pdftoppmFileDirectory, "pdftoppm.exe")

    print("Generating Jpeg's..... \n")
    print('"%s" -jpeg "%s" out' % (pdftoppmFile, pdfFileName))

    #Calling a subprocess (i.e another thread) which does actual conversion
    subprocess.call('"%s" -jpeg "%s" out' % (pdftoppmFile, (firstName + "_" + lastName + ".pdf")))

    #Waiting 2 seconds just in case
    time.sleep(2)

    #Creating names which JPEGs will be renamed to
    nameOfFirstNewJpeg = firstName + "_" + lastName + "_Page_1"
    nameOfSecondNewJpeg = firstName + "_" + lastName + "_Page_2"


    print("Remaning Jpeg's accordingly \n")

    #Renaming JPEG's accordingly
    os.rename(os.path.join(os.getcwd() ,"out-1.jpg"), nameOfFirstNewJpeg + ".jpeg")
    os.rename(os.path.join(os.getcwd() ,"out-2.jpg"), nameOfSecondNewJpeg + ".jpeg")


    #Moving Jpeg's to temporary folder
    print("Moving Jpeg's to temporary folder... \n")
    movetoTemporaryFolder(nameOfFirstNewJpeg, ".jpeg")
    movetoTemporaryFolder(nameOfSecondNewJpeg , ".jpeg")

    #Deleting PDF from root directory. We don't need to move it since it will not be used. Better to just delete.
    print("Deleting original PDF..... \n")
    deleteFile((firstName + "_" + lastName), ".pdf")



