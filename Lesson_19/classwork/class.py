
from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__)


# route and endpoint = synonyms
# host + route
# http://127.0.0.1:5000 + / = http://127.0.0.1:5000/
@app.route('/', methods=['GET'])
def ping():
    return jsonify({
        "message": "Server is up and running!"
    }), HTTPStatus.OK


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    return jsonify({
        "id": user_id,
        "full_name": "Vasya Federov",
        "birth_date": "01.01.1999",
    }), HTTPStatus.OK


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    print(data)

    return jsonify({
        "message": "User created"
    }), HTTPStatus.CREATED


"""
GET - для получения информации
POST - для создания сущности
PUT - для полной перезаписи информации о сущности
PATCH - для частично изменения
DELETE - для удаления
"""

app.run(port=5000)
