from datetime import datetime, timezone

todos = {}
_next_id = 1


def get_all():
    return list(todos.values())


def get_by_id(todo_id):
    return todos.get(todo_id)


def create(title, description=""):
    global _next_id
    todo = {
        "id": _next_id,
        "title": title,
        "description": description,
        "completed": False,
        "created_at": datetime.now(timezone.utc).isoformat() + "Z",
        "updated_at": datetime.now(timezone.utc).isoformat() + "Z",
    }
    todos[_next_id] = todo
    _next_id += 1
    return todo


def update(todo_id, data):
    todo = todos.get(todo_id)
    if not todo:
        return None
    if "title" in data:
        todo["title"] = data["title"]
    if "description" in data:
        todo["description"] = data["description"]
    if "completed" in data:
        todo["completed"] = data["completed"]
    todo["updated_at"] = datetime.now(timezone.utc).isoformat() + "Z"
    return todo


def delete(todo_id):
    return todos.pop(todo_id, None)
