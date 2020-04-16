from flask import Flask, request, redirect, url_for, render_template, flash, send_from_directory, send_file


#Importing Python Libraries
import os
import time
import shutil
import pathlib
#Importing Method to generate TXT file
from generateTXTFile import generateTXTFile

#Importing module to move files such as TXT file and pdf to temporary folder
from movetoTemporaryFolder import movetoTemporaryFolder

#The module that handles conversion
from convertToPDF import convertPDFToJpeg


#The module that generates final zip file
from zipFiles import createZip


#This is needed for flask framework to start
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), "temporary")


#Setting variable for temporary directory
temporaryDirectory = os.path.join(os.getcwd(), "temporary")

ALLOWED_EXTENSIONS = "pdf"




#Main view presented to user which will be used to collect information.
@app.route("/", methods=["GET", "POST"])
def home():
    #Requesting the page
    if request.method == "GET":
        return render_template("home.html")

    #When user hits submit it runs the code inside this else if
    elif request.method == "POST":

        #First thing done is delete temporary folder then recreate it (If you try to submit the same form more than once you would have gotten error that it exists. This is the fix for it)
        os.chdir(pathlib.Path(__file__).parent.absolute())
        shutil.rmtree("temporary")

        time.sleep(3)
        os.mkdir("temporary")

        #On Submission get data from form
        firstName = request.form["firstName"]
        lastName = request.form["lastName"]
        netID = request.form["NETID"]
        department = request.form["Department"]

        #Generating TXT Document
        generateTXTFile(firstName, lastName, netID, department)
        movetoTemporaryFolder((firstName + "_" + lastName), ".txt")

        #Getinng PDF into temporary folder
        file = request.files["pdf_file"]
        file_name = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

        #Convert PFF to multiple JPEG's
        convertPDFToJpeg(firstName, lastName)

        #Wait three seconds for conversion to occur
        time.sleep(3)

        #Create zip file which will be returned
        createZip(firstName, lastName)

        return send_file(os.path.join(temporaryDirectory, "Returned_Files.zip"), mimetype=None, as_attachment=True)
        return render_template("home.html")




#Needed to start entire web application
if __name__ == "__main__":
    app.secret_key = 'Test'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug=True)