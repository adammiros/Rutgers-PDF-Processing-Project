from flask import Flask, request, redirect, url_for, render_template, flash

import os

#Importing Method to generate TXT file
from generateTXTFile import generateTXTFile

#Importing module to move files such as TXT file and pdf to temporary folder
from movetoTemporaryFolder import movetoTemporaryFolder


from convertToPDF import convertPDFToJpeg

#This is needed for flask framework to start
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), "temporary")


ALLOWED_EXTENSIONS = "pdf"


#Main view presented to user which will be used to collect information
@app.route("/", methods=["GET", "POST"])
def home():

    #Requesting the page
    if request.method == "GET":
        return render_template("home.html")

    #Getting the data from the page
    elif request.method == "POST":
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


        convertPDFToJpeg(firstName, lastName)

        return redirect(request.url)


        #Returning to homepage to submit another request
        return render_template("home.html")


@app.route("/sucess")
def sucessPage():
    return "<h1>Sucess!</h1>"



if __name__ == "__main__":
    app.secret_key = 'Test'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug=True)