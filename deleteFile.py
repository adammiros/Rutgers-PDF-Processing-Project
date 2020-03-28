import  os

def deleteFile(filename: str, filetype: str):
    temporaryDirectory = temporaryDirectory = os.path.join(os.getcwd(), "temporary")

    print("Removing: " + os.path.join(temporaryDirectory, (filename + filetype)) + "..... \n")
    os.remove(os.path.join(temporaryDirectory, (filename + filetype)))

    print("File deleted...")