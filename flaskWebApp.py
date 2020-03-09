from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def home():
    return render_template("home.html")






@app.route("/sucess")
def sucessPage():
    return "<h1>Sucess!</h1>"



if __name__ == "__main__":
    app.run(debug=True)