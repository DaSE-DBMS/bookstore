from flask import Blueprint
from flask import request
from flask import jsonify
from be.model import user
from be.model import store
from be.model import order

bp_order = Blueprint("order", __name__, url_prefix="/order")


@bp_order.route("/getOrder", methods=["GET"])
def getOrder():
    username: str = request.json.get("username", "")
    token: str = request.headers.get("token", "")
    o = order.Order
    ok, orderlist = o.getOrder(username=username, token=token)
    if ok:
        return jsonify({"message": "ok", "orderlist": orderlist}), 200
    else:
        return jsonify({"message": "Inquiry failed, no order"}), 501