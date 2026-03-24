from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage
todos = {}
next_id = 1


def success_response(data, message="Success", status_code=200):
    return jsonify({
        "status": "success",
        "message": message,
        "data": data
    }), status_code


def error_response(message, status_code):
    return jsonify({
        "status": "error",
        "message": message,
        "data": None
    }), status_code


# GET /todos - List all todos
@app.route("/todos", methods=["GET"])
def get_todos():
    return success_response(list(todos.values()))


# GET /todos/<id> - Get single todo
@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = todos.get(todo_id)
    if not todo:
        return error_response(f"Todo with id {todo_id} not found", 404)
    return success_response(todo)


# POST /todos - Create todo
@app.route("/todos", methods=["POST"])
def create_todo():
    global next_id
    body = request.get_json()
    if not body or not body.get("title"):
        return error_response("Field 'title' is required", 400)

    todo = {
        "id": next_id,
        "title": body["title"],
        "description": body.get("description", ""),
        "completed": False
    }
    todos[next_id] = todo
    next_id += 1
    return success_response(todo, "Todo created successfully", 201)


# PUT /todos/<id> - Update todo
@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    todo = todos.get(todo_id)
    if not todo:
        return error_response(f"Todo with id {todo_id} not found", 404)

    body = request.get_json()
    if not body:
        return error_response("Request body is required", 400)

    todo["title"] = body.get("title", todo["title"])
    todo["description"] = body.get("description", todo["description"])
    todo["completed"] = body.get("completed", todo["completed"])
    return success_response(todo, "Todo updated successfully")


# DELETE /todos/<id> - Delete todo
@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todo = todos.pop(todo_id, None)
    if not todo:
        return error_response(f"Todo with id {todo_id} not found", 404)
    return success_response(None, "Todo deleted successfully")


@app.route("/health", methods=["GET"])
def health():
    return success_response({"status": "healthy"}, "API is running")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
