from flask import Flask, jsonify, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

tasks = []
task_id = 1

@app.route('/')
def healthcheck():
    return 'OK', 200

@app.route('/health')
def health():
    return jsonify(status='healthy'), 200

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id
    data = request.get_json()
    if 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    task = {
        'id': task_id,
        'title': data['title'],
        'description': data.get('description', ''),
        'done': False
    }
    task_id += 1
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks/<int:id>', methods=['PUT'])
def mark_done(id):
    for task in tasks:
        if task['id'] == id:
            task['done'] = True
            return jsonify(task)
    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    global tasks
    tasks = [task for task in tasks if task['id'] != id]
    return jsonify({'message': 'Task deleted'}), 200

@app.route('/error')
def trigger_error():
    1 / 0  # division by zero

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
