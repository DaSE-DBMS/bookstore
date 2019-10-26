from flask import Blueprint
from flask import request
from flask import jsonify
from be.model import user

bp_auth = Blueprint("auth", __name__, url_prefix="/auth")


@bp_auth.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", "")
    password = request.json.get("password", "")
    terminal = request.json.get("terminal", "")
    u = user.User(username=username, password=password, terminal=terminal)
    ok, token = u.login()
    if ok:
        return jsonify({"message": "ok", "token": token}), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401


@bp_auth.route("/logout", methods=["POST"])
def logout():
    username: str = request.json.get("username", "")
    token: str = request.headers.get("token", "")
    u = user.User(username=username, token=token)
    if token == "":
        return jsonify({"message": "Invalid token"}), 401

    if u.logout():
        return jsonify({"message": "ok"}), 200
    else:
        return jsonify({"message": "Invalid token"}), 401


@bp_auth.route("/register", methods=["POST"])
def register():
    username = request.json.get("username", "")
    password = request.json.get("password", "")
    u = user.User(username=username, password=password)
    if u.register():
        return jsonify({"message": "ok"}), 200
    else:
        return jsonify({"message": "fail, username has exists"}), 401


@bp_auth.route("/unregister", methods=["POST"])
def unregister():
    username = request.json.get("username", "")
    password = request.json.get("password", "")
    u = user.User(username=username, password=password)
    if u.unregister():
        return jsonify({"message": "ok"}), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401
