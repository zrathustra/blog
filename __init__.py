from flask import Flask, render_template, send_file, request, abort, jsonify
import datetime
import random
import json
import uuid

import src

app = Flask(__name__)

app.config['HOME'] = "/var/www/ahrussell/ahrussell/"

from views.projects import projects
app.register_blueprint(projects)
from views.blog import blog
app.register_blueprint(blog)

@app.route('/')
def index():

    index = render_template("index.html", page_name="home")
    return index
    
@app.route('/about')
def about():
    return render_template("about.html", page_name="about")

@app.route('/resume')
def resume():
    return send_file("downloads/resume.pdf")
    
@app.route('/downloads/<path:filepath>')
def downloads(filepath):
    return send_file("downloads/"+filepath, as_attachment=True)

@app.errorhandler(404)
@app.errorhandler(403)
@app.errorhandler(410)
@app.errorhandler(500)
def error_page(e):
    error = str(e)[:3]

    return render_template("error/"+str(error)+".html", page_name="error", error_message=str(e), error=error), int(error)

if __name__ == '__main__':
    app.debug = True
    app.run(port=3333)
