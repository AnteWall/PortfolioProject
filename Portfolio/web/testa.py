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
    return render_template("home.html", dataB = db)

@app.route("/list", methods=['GET', 'POST'])
def list_page():
    db = data.init()
    techniques = data.get_techniques(db)
    fields = data.get_fields(db)
    tech_list = []
    if request.method == 'POST':
        for i in data.get_techniques(db):
            try:
                if i == request.form["tech_"+i]:
                    tech_list.append(i)
            except:
                pass
            
        sort_order = request.form["sort_order"]
        db = data.search(db, search=request.form["search"],sort_order=sort_order,techniques=tech_list)
    return render_template("list.html",dataB = db, _fields = fields)

@app.route("/techniques")
def list_tech():
    db = data.init()
    techs = data.get_techniques(db)
    print("#####################3"+str(techs))
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

