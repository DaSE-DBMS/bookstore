from flask import Blueprint
from flask import request
from flask import jsonify
from be.model import user
from be.model import store
from be.model import order

bp_order = Blueprint("order", __name__, url_prefix="/order")

@bp_order.route("/createOrder", methods=["POST"])
def createOrder():
    orderId: str = request.json.get("orderId", "")
    sellerName: str = request.json.get("sellerName", "")
    buyerName : str = request.json.get("buyerName", "")
    orderStatus : str = request.json.get("orderStatus","")
    cartlist : list = request.json.get("cartlist",[])
    addr : str = request.json.get("addr","")
    o = order.Order
    ok= o.createOrder(orderId = orderId, sellerName = sellerName, buyerName = buyerName, orderStatus = orderStatus, cartlist = cartlist, addr = addr)
    if ok:
        return jsonify({"message": "ok"}), 200
    else:
        return jsonify({"message": "Inquiry failed, no order"}), 501

@bp_order.route("/getOrder", methods=["POST"])
def getOrder():
    username: str = request.json.get("username", "")
    token: str = request.headers.get("token", "")
    o = order.Order
    ok, orderlist = o.getOrder(username=username, token=token)
    if ok:
        return jsonify({"message": "ok", "orderlist": orderlist}), 200
    else:
        return jsonify({"message": "Inquiry failed, no order"}), 501

@bp_order.route("/cancelOrder", methods=["POST"])
def cancelOrder():
    orderId: str = request.json.get("orderId", "")
    o = order.Order
    ok = o.cancelOrder(orderId=orderId)
    if ok:
        return jsonify({"message": "ok"}), 200
    else:
        return jsonify({"message": "cancel failed, token error"}), 401