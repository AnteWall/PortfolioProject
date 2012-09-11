# -*- coding: utf-8 -*-
from flask import Flask
from jinja2 import Template
template = Template('Hello {{ name }}!')

app = Flask(__name__)
@app.route("/")
def hello():
    return template.render(name='John Doe')
if __name__ == "__main__":
    app.run()
