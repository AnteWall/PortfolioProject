# -*- coding: utf-8 -*-
from flask import Flask,render_template,request
from jinja2 import Template
import data, unicodedata

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
    sorted_list = data.search(db, sort_by="end_date")
    x = 0
    udb = []
    for proj in sorted_list:
        udb.append(proj)
        x += 1
        if x == 3:
            break
    return render_template("home.html", dataB = db, updatedPro = udb)

@app.route("/list", methods=['GET', 'POST'])
def list_page():
    db = data.init()
    fields = data.get_fields(db)
    if request.method == 'POST':
        search_list = []
        for x in data.get_fields(db):
            try:
                search_list.append(request.form[x])
            except:
                pass
        if search_list == []:
            search_list = None
        sort_order = request.form["sort_order"]
        db = data.search(db, search=request.form["search"],sort_order=sort_order, search_fields=search_list)
    return render_template("list.html",dataB = db, _fields = fields)

@app.route("/techniques")
def list_tech():
    db = data.init()
    techs = data.get_techniques(db)
    return render_template("list_techniques.html", techniques = techs,dataB = db  )


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
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run()

