from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
import re
import test

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("form.html")
#    return render_template("home.html")

@app.route('/qrconvert', methods=['GET', 'POST'])
def qrconvert():
    return render_template("qrconvert.html", shortcode = request.form['shortcode'])

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")