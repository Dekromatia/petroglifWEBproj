#import os

#REST_URL = os.enversion.get("MONGO_HOST", "http://localhost/")

from flask import Flask, render_template
#import requests

app = Flask(__name__)

@app.route("/")
def homepage():
    #result = requests.get(REST_URL).json()
    return render_template("homepage.html.j2") #добавить в скобки , result = result

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
