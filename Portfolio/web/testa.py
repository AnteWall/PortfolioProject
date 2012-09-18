# -*- coding: utf-8 -*-
from flask import Flask,render_template
from jinja2 import Template

app = Flask(__name__)

@app.route("/web/style/<filename>")
def css(filename):
    with app.open_resource("web/style/" +filename) as f:
        return f.read()
@app.route("/web/images/<filename>")
def images(filename):
    with app.open_resource("web/images/" + filename) as f:
        return f.read()

@app.route("/")
def home_page():
    return render_template("home.html")
if __name__ == "__main__":
    app.debug = True
    app.run()

