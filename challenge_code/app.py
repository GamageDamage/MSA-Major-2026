import flask
from flask import request, jsonify
import student_genorator as sg

def search_dict_list(search_key, search_value):
    catagory = []
    student_dicts = sg.get_student_dicts()
    for line in student_dicts:
        if line[search_key] == search_value:
            catagory.append(line)
    return catagory


app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route('/', methods = ['GET'])
def index():
    return "<h1>Student Data API</h1>"

@app.route('/api/students/all',methods=['GET'])
def api_all():
    #get student dict
    student_dicts = sg.get_student_dicts()
    return jsonify(student_dicts)

#create a route that returns students in a specific major
#create a route that reurns students of a specific class(freshman sophomore etc)
#create a route that returns students based off of id
app.run(debug=True)
