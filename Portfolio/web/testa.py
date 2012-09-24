# -*- coding: utf-8 -*-
from flask import Flask,render_template,request
from jinja2 import Template
import data

app = Flask(__name__)

@app.route("/web/style/<filename>")
def css(filename):
    with app.open_resource("web/style/" +filename) as f:
        return f.read()
"""@app.route("/web/images/<filename>")
def images(filename):
    with app.open_resource("web/images/" + filename) as f:
        return f.read()"""

@app.route("/")
def home_page():
    db = data.init()
    return render_template("home.html", dataB = db)

@app.route("/list", methods=['GET', 'POST'])
def list_page():
    db = data.init()
    techniques = data.get_techniques(db)
    fields = data.get_fields(db)
    if request.method == 'POST':
        
        db = data.search(db, search=request.form["search"])
        print("####################################"+str(db))
    return render_template("list.html",dataB = db,tech = techniques,_fields = fields)

@app.route("/portfolio/<id>")
def id_page(id):
    db = data.init()
    project = data.get_project(db,id)
    return render_template("portfolio.html",dataB = project)

@app.errorhandler(404)
def error_404(e):
    return render_template("404.html"),404

if __name__ == "__main__":
    app.debug = True
    app.run()

