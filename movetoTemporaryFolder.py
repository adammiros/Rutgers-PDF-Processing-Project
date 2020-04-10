import pathlib
import os
import shutil
import time

def movetoTemporaryFolder(fileName: str, extension: str):

    #Get current Directory of this file (I.E Root... I need it so I can use it in the move function
    currentWorkingDirectory = pathlib.Path(__file__).parent.absolute()

    #Create the path for the value that will be moved
    fileToMove = os.path.join(currentWorkingDirectory, (fileName + extension))

    #Create the path for the temporary folder
    newDirectory = os.path.join(currentWorkingDirectory, "temporary")


    #Moving the file
    shutil.move(fileToMove, newDirectory)
