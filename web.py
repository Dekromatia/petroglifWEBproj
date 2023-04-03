#import os

#REST_URL = os.enversion.get("MONGO_HOST", "http://localhost/")

from flask import Flask, render_template
import requests
# import image_datasets


# specify version number
# import pkg_resources
# __version__ = pkg_resources.get_distribution('pixplot').version

app = Flask(__name__)

# @app.route('/')
# def index():
#     # Make a request to the other Docker container's web server
#     html_response = requests.get('pixplot:6000')

#     # Extract the HTML content from the response
#     html_content = html_response.text

#     # Return the HTML content as a response
#     return render_template('index.html', html_content=html_content)

# image_datasets.oslomini.download()
# pixplot --images "datasets/images/*.jpg"

@app.route("/")
def homepage():
    #result = requests.get(REST_URL).json()
    return render_template("homepage.html.j2") #добавить в скобки , result = result

@app.route("/aboutus")
def about_us():
    #result = requests.get(REST_URL).json()
    return render_template("page4_present.html.j2")

# @app.route("/pixplot --images "path/to/images/*.jpg"")
@app.route("/graph2")
def graph():
    #result = requests.get(REST_URL).json()
    return render_template("yel.html.j2")


@app.route("/resurch")
def resurch():
    #result = requests.get(REST_URL).json()
    return render_template("page5_research.html.j2")

@app.route("/ch")
def ch():
    #result = requests.get(REST_URL).json()
    return render_template("chykotka.html.j2")

@app.route("/base2")
def base():
    #result = requests.get(REST_URL).json()
    return render_template("base2.html.j2")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
