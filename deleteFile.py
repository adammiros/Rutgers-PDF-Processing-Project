import  os

#Removes specified file from root
def deleteFile(filename: str, filetype: str):

    print("Removing: " + (filename + filetype) + "..... \n")
    os.remove(filename + filetype)

    print("File deleted...")
