import os
import subprocess
import time

from movetoTemporaryFolder import movetoTemporaryFolder
from deleteFile import deleteFile


def convertPDFToJpeg(firstName, lastName):
    temporaryDirectory = os.path.join(os.getcwd(), "temporary")
    pdftoppmFileDirectory = os.path.join(os.getcwd(), "PDFTOPPM")


    print("Grabbing PDF..... \n")
    pdfFileName = os.path.join(temporaryDirectory, (firstName + "_" + lastName + ".pdf"))
    pageCount = 1


    pdftoppmFile = os.path.join(pdftoppmFileDirectory, "pdftoppm.exe")

    print("Generating Jpeg's..... \n")
    subprocess.Popen('"%s" -jpeg "%s" out' % (pdftoppmFile, pdfFileName))

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
