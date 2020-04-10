#Method to create TXT file


def generateTXTFile(firstName, lastName, netID, department):
    #Check to make sure folder is cleared out
    try:
        with open((firstName + "_" + lastName + ".txt"), "w+") as f:
            f.write("First Name: " + firstName + "\n")
            f.write("Last Name: " + lastName + "\n")
            f.write("NetID: " + netID + "\n")
            f.write("Department: " + department + "\n")

            f.close()
    except:
        print("File most likly exists.... Skipping")