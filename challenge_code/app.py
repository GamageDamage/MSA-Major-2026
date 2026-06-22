import flask
from flask import request, jsonify
#import student_genorator as sg

app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route('/', methods = ['GET'])
def index():
    return "<h1>Student Data API</h1>"

app.run(debug=True)