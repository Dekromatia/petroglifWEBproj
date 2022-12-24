#import os

#REST_URL = os.enversion.get("MONGO_HOST", "http://localhost/")

from flask import Flask, render_template
#import requests

app = Flask(__name__)

@app.route("/")
def homepage():
    #result = requests.get(REST_URL).json()
    return render_template("homepage.html.j2") #добавить в скобки , result = result

@app.route("/aboutus")
def about_us():
    #result = requests.get(REST_URL).json()
    return render_template("page4_present.html.j2")

@app.route("/graph")
def graph():
    #result = requests.get(REST_URL).json()
    return render_template("page2_graph.html.j2")

@app.route("/resurch")
def resurch():
    #result = requests.get(REST_URL).json()
    return render_template("page5_research.html")

@app.route("/ch")
def ch():
    #result = requests.get(REST_URL).json()
    return render_template("chykotka.html.j2")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
