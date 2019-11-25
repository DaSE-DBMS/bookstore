from flask import Blueprint
from flask import request
from flask import jsonify
from be.model import user

bp_auth = Blueprint("auth", __name__, url_prefix="/auth")


@bp_auth.route("/login", methods=["POST"])
def login():
    user_id = request.json.get("user_id", "")
    password = request.json.get("password", "")
    terminal = request.json.get("terminal", "")
    u = user.User()
    ok, token = u.login(user_id=user_id, password=password, terminal=terminal)
    if ok:
        return jsonify({"message": "ok", "token": token}), 200
    else:
        return jsonify({"message": "Invalid user_id or password"}), 401


@bp_auth.route("/logout", methods=["POST"])
def logout():
    user_id: str = request.json.get("user_id", "")
    token: str = request.headers.get("token", "")
    u = user.User()
    if u.logout(user_id=user_id, token=token):
        return jsonify({"message": "ok"}), 200
    else:
        return jsonify({"message": "Invalid token"}), 401


@bp_auth.route("/register", methods=["POST"])
def register():
    user_id = request.json.get("user_id", "")
    password = request.json.get("password", "")
    is_buyer = request.json.get("isBuyer", False)
    is_seller = request.json.get("isSeller", False)
    u = user.User()
    if not is_buyer and not is_seller:
        return jsonify({"message": "fail, register as a seller/buyer"}), 512
    if u.register(
        user_id=user_id, password=password, is_buyer=is_buyer, is_seller=is_seller
    ):
        return jsonify({"message": "ok"}), 200
    else:
        return jsonify({"message": "fail, user_id has exists"}), 511


@bp_auth.route("/unregister", methods=["POST"])
def unregister():
    user_id = request.json.get("user_id", "")
    password = request.json.get("password", "")
    u = user.User()
    if u.unregister(user_id=user_id, password=password):
        return jsonify({"message": "ok"}), 200
    else:
        return jsonify({"message": "Invalid user_id or password"}), 401


@bp_auth.route("/password", methods=["POST"])
def change_password():
    user_id = request.json.get("user_id", "")
    old_password = request.json.get("oldPassword", "")
    new_password = request.json.get("newPassword", "")
    u = user.User()
    if u.change_password(
        user_id=user_id, old_password=old_password, new_password=new_password
    ):
        return jsonify({"message": "ok"}), 200
    else:
        return jsonify({"message": "Invalid user_id or password"}), 401


@bp_auth.route("/add_funds", methods=["POST"])
def user_add_funds():
    user_id = request.json.get("user_id")
    password = request.json.get("password")
    add_value = request.json.get("add_value")
    u = user.User()
    code, message = u.add_funds(user_id, password, add_value)
    return jsonify({"message": message}), code
