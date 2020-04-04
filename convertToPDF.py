import os
import subprocess
import time

from movetoTemporaryFolder import movetoTemporaryFolder
from deleteFile import deleteFile


def convertPDFToJpeg(firstName, lastName):

    pdfFileName = ""

    temporaryDirectory = os.path.join(os.getcwd(), "temporary")
    pdftoppmFileDirectory = os.path.join(os.getcwd(), "PDFTOPPM")


    fileNames = os.listdir(temporaryDirectory)
    for file in fileNames:
        if file.endswith(".pdf"):
            pdfFileName = file
            os.rename(os.path.join(temporaryDirectory, pdfFileName), (firstName + "_" + lastName + ".pdf"))






    pdftoppmFile = os.path.join(pdftoppmFileDirectory, "pdftoppm.exe")

    #print("Generating Jpeg's..... \n")
    print('"%s" -jpeg "%s" out' % (pdftoppmFile, pdfFileName))
    subprocess.call('"%s" -jpeg "%s" out' % (pdftoppmFile, (firstName + "_" + lastName + ".pdf")))

    time.sleep(2)

    nameOfFirstNewJpeg = firstName + "_" + lastName + "_Page_1"
    nameOfSecondNewJpeg = firstName + "_" + lastName + "_Page_2"




    print("Remaning Jpeg's accordingly \n")

    os.rename(os.path.join(os.getcwd() ,"out-1.jpg"), nameOfFirstNewJpeg + ".jpeg")
    os.rename(os.path.join(os.getcwd() ,"out-2.jpg"), nameOfSecondNewJpeg + ".jpeg")


    print("Moving Jpeg's to temporary folder... \n")
    movetoTemporaryFolder(nameOfFirstNewJpeg, ".jpeg")
    movetoTemporaryFolder(nameOfSecondNewJpeg , ".jpeg")


    print("Deleting original PDF..... \n")
    deleteFile((firstName + "_" + lastName), ".pdf")



