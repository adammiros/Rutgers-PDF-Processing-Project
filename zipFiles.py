from zipfile import ZipFile
import os
def createZip(firstName: str, lastName: str):
    temporaryDirectory = os.path.join(os.getcwd(), "temporary")


    os.chdir(temporaryDirectory)
    # Create a Zip File
    zipObj = ZipFile('Returned_Files.zip', 'w')

    # Add multiple files to the zip
    zipObj.write((firstName + "_" + lastName + "_" + "Page_1.jpeg"))
    zipObj.write(firstName + "_" + lastName + "_" + "Page_2.jpeg")
    zipObj.write(firstName + "_" + lastName + ".txt")

    # close the Zip File
    zipObj.close()
