from flask import Blueprint, jsonify, request
from . import models

bp = Blueprint("todos", __name__, url_prefix="/api/todos")


def success(data, message="Success", code=200):
    return jsonify({"status": "success", "message": message, "data": data}), code


def error(message, code=400):
    return jsonify({"status": "error", "message": message, "data": None}), code


@bp.route("/", methods=["GET"])
def get_all():
    return success(models.get_all())


@bp.route("/<int:todo_id>", methods=["GET"])
def get_one(todo_id):
    todo = models.get_by_id(todo_id)
    if not todo:
        return error("Todo not found", 404)
    return success(todo)


@bp.route("/", methods=["POST"])
def create():
    body = request.get_json(silent=True) or {}
    title = body.get("title", "").strip()
    if not title:
        return error("Field 'title' is required")
    todo = models.create(title, body.get("description", ""))
    return success(todo, "Todo created", 201)


@bp.route("/<int:todo_id>", methods=["PUT"])
def update(todo_id):
    body = request.get_json(silent=True) or {}
    todo = models.update(todo_id, body)
    if not todo:
        return error("Todo not found", 404)
    return success(todo, "Todo updated")


@bp.route("/<int:todo_id>", methods=["DELETE"])
def delete(todo_id):
    todo = models.delete(todo_id)
    if not todo:
        return error("Todo not found", 404)
    return success(None, "Todo deleted")
