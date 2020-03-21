#Method to create TXT file


def generateTXTFile(firstName, lastName, netID, department):
    f = open((firstName + "_" + lastName + ".txt"), "w+")
    f.write("First Name: " + firstName + "\n")
    f.write("Last Name: " + lastName + "\n")
    f.write("NetID: " + netID + "\n")
    f.write("Department: " + department + "\n")

    f.close()