from flask import Flask, request, jsonify
from rest import models

app = Flask(__name__)
students = models.read_csv("./db/students.csv")


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/login', methods=['POST'])
def login():
    json_data = request.json
    stu_id = None
    stu_password = None
    if isinstance(json_data, dict):
        stu_id = json_data.get("id")
        stu_password = json_data.get("password")

    for student in students:
        if student.id == stu_id and stu_password == student.password:
            response = jsonify(
                {
                    'message': 'success',
                    'result': {
                        "student": vars(student)
                    }
                })
            return response

    response = jsonify(
        {
            'message': 'failed',
        })
    return response


@app.route("/data")
def get_all():
    response = jsonify({'message': 'success', "result": [vars(s) for s in students]})
    return response


@app.route('/select', methods=['POST'])
def select():
    json_data = request.json
    if isinstance(json_data, dict):
        target = '-'.join(json_data.values())
    for student in students:
        to_str = student.to_str()
        if to_str == target:
            response = jsonify(
                {
                    'message': 'success',
                    'result': {
                        "dormitory": student.dormitory
                    }
                })
            return response

    response = jsonify(
        {
            'message': 'success'
        })
    return response


@app.route('/get/<id>', methods=['Get'])
def get(id):
    for student in students:
        to_str = student.id
        if to_str == id:
            response = jsonify(
                {
                    'message': 'success',
                    'result': {
                        "student": vars(student)
                    }
                })
            return response

    response = jsonify(
        {
            'message': 'failed'
        })
    return response


if __name__ == '__main__':
    app.run()
