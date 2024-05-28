from flask import Flask, request, jsonify

import db

from models.employee import Employee

app = Flask(__name__)


@app.route("/employees", methods=["GET"])
def get_employees():
    return jsonify(db.get("employees"))

@app.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    employee = db.get_by_id("employees", employee_id)
    if employee:
        return jsonify(employee)
    return '', 404

@app.route("/employees", methods=["POST"])
def add_employee():
    global nextEmployeeId

    employee = request.json
    if not Employee.is_valid(employee):
        return jsonify({ 'error': 'Invalid employee properties.' }), 400
    employee["id"] = db.get_next_id_for_key("employees")
    db.insert("employees", employee)

    return '', 201, { 'location': f'/employees/{employee["id"]}' }

@app.route("/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    employee = request.json
    if not Employee.is_valid(employee):
        return jsonify({ 'error': 'Invalid employee properties.' }), 400
    updated_employee = db.update("employees", employee_id, employee)
    if not updated_employee:
        return '', 404
    return '', 204