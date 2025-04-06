from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Загрузка переменных окружения
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/todo_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Определение моделей
class TaskList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    tasks = db.relationship('Task', backref='task_list', cascade='all, delete-orphan', lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    list_id = db.Column(db.Integer, db.ForeignKey('task_list.id'), nullable=False)

# Создание таблиц
with app.app_context():
    db.create_all()

# CRUD для списков задач
@app.route('/lists', methods=['GET'])
def get_lists():
    lists = TaskList.query.all()
    return jsonify([{'id': lst.id, 'name': lst.name} for lst in lists])

@app.route('/lists', methods=['POST'])
def create_list():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': 'Missing name'}), 400
    new_list = TaskList(name=data['name'])
    db.session.add(new_list)
    db.session.commit()
    return jsonify({'id': new_list.id, 'name': new_list.name}), 201

@app.route('/lists/<int:list_id>', methods=['PUT'])
def update_list(list_id):
    data = request.get_json()
    task_list = TaskList.query.get_or_404(list_id)
    task_list.name = data.get('name', task_list.name)
    db.session.commit()
    return jsonify({'id': task_list.id, 'name': task_list.name})

@app.route('/lists/<int:list_id>', methods=['DELETE'])
def delete_list(list_id):
    task_list = TaskList.query.get_or_404(list_id)
    db.session.delete(task_list)
    db.session.commit()
    return '', 204

# CRUD для задач
@app.route('/tasks', methods=['GET'])
def get_tasks():
    list_id = request.args.get('list_id')
    query = Task.query
    if list_id:
        query = query.filter_by(list_id=list_id)
    tasks = query.all()
    return jsonify([{'id': task.id, 'title': task.title, 'completed': task.completed, 'list_id': task.list_id} for task in tasks])

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if 'title' not in data or 'list_id' not in data:
        return jsonify({'error': 'Missing title or list_id'}), 400
    new_task = Task(title=data['title'], list_id=data['list_id'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'id': new_task.id, 'title': new_task.title, 'completed': new_task.completed, 'list_id': new_task.list_id}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = Task.query.get_or_404(task_id)
    task.title = data.get('title', task.title)
    task.completed = data.get('completed', task.completed)
    db.session.commit()
    return jsonify({'id': task.id, 'title': task.title, 'completed': task.completed, 'list_id': task.list_id})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)