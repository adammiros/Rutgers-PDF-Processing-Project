from flask import Flask, redirect, url_for, render_template, request


#Importing Method to generate TXT file
from generateTXTFile import generateTXTFile

#This is needed for flask framework to start
app = Flask(__name__)

#Main view presented to user which will be used to collect information
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")

    elif request.method == "POST":
        firstName = request.form["firstName"]
        lastName = request.form["lastName"]
        netID = request.form["NETID"]
        department = request.form["Department"]





        generateTXTFile(firstName, lastName, netID, department)
        return render_template("home.html")


@app.route("/sucess")
def sucessPage():
    return "<h1>Sucess!</h1>"



if __name__ == "__main__":
    app.run(debug=True)