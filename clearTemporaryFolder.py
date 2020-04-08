import os
import glob


temporaryDirectory = os.path.join(os.getcwd(), "temporary")

#Search for all the files in the temporary directory and delete them!
def clearTemporaryCache():
    for r, d, f in os.walk(temporaryDirectory):
        for file in f:
            os.remove(os.path.join(temporaryDirectory, file))

    print("Cleared out the temporary folder!")
