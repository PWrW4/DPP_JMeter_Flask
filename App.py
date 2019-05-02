from flask import Flask
from flask import jsonify
from flask import request
from flask import json
from flask import abort

app = Flask(__name__)

empDB = [

    {

        'id': '101',

        'name': 'Saravanan S',

        'title': 'Technical Leader'

    },

    {

        'id': '201',

        'name': 'Rajkumar P',

        'title': 'Sr Software Engineer'

    }

]


@app.route('/')
def index():
    return jsonify({'APP': "DPP-JMETER TEST API"})


@app.route('/save', methods=['POST'])
def saveDB():
    file = open("db.txt", "w")
    json.dump(empDB, file)
    file.close()
    return jsonify({'Result': "Saved"})


@app.route('/load', methods=['POST'])
def loadDB():
    file = open("db.txt", "r")
    empDB = json.load(file)
    print(empDB)
    file.close()
    return jsonify({'Result': "Loaded"})


@app.route('/empdb/employee', methods=['GET'])
def getAllEmp():
    return jsonify({'emps': empDB})


@app.route('/empdb/employee/<empId>', methods=['GET'])
def getEmp(empId):
    usr = [emp for emp in empDB if (emp['id'] == empId)]

    return jsonify({'emp': usr})


@app.route('/empdb/employee/<empId>', methods=['PUT'])
def updateEmp(empId):
    em = [emp for emp in empDB if (emp['id'] == empId)]

    if 'name' in request.json:
        em[0]['name'] = request.json['name']

    if 'title' in request.json:
        em[0]['title'] = request.json['title']

    return jsonify({'emp': em[0]})


@app.route('/empdb/employee', methods=['POST'])
def createEmp():
    dat = {

        'id': request.json['id'],

        'name': request.json['name'],

        'title': request.json['title']

    }

    empDB.append(dat)

    return jsonify(dat)


@app.route('/empdb/employee/<empId>', methods=['DELETE'])
def deleteEmp(empId):
    em = [emp for emp in empDB if (emp['id'] == empId)]

    if len(em) == 0:
        abort(404)

    empDB.remove(em[0])

    return jsonify({'response': 'Success'})
