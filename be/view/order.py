from flask import Blueprint
from flask import request
from flask import jsonify
from be.model import order

bp_order = Blueprint("order", __name__, url_prefix="/order")

@bp_order.route("/createOrder", methods=["POST"])
def createOrder():
    orderId: str = request.json.get("orderId", "")
    sellerName: str = request.json.get("sellerName", "")
    buyerName : str = request.json.get("buyerName", "")
    orderStatus : str = request.json.get("orderStatus","")
    goodsidlist : list = request.json.get("goodsidlist",[])
    addr : str = request.json.get("addr","")
    o = order.Order
    ok= o.createOrder(orderId = orderId, buyerName = buyerName, sellerName = sellerName, orderStatus = orderStatus, goodsidlist = goodsidlist, addr = addr)
    if ok:
        return jsonify({"message": "ok"}), 200
    else:
        return jsonify({"message": "Inquiry failed, no order"}), 501

@bp_order.route("/buyergetOrder", methods=["POST"])
def buyergetOrder():
    buyerName: str = request.json.get("buyerName", "")
    o = order.Order
    ok, orderlist = o.buyergetOrder(o, buyerName=buyerName)
    if ok:
        return jsonify({"message": "ok", "orderlist": orderlist}), 200
    else:
        return jsonify({"message": "Inquiry failed, no order", "orderlist": orderlist}), 501

@bp_order.route("/sellergetOrder", methods=["POST"])
def sellergetOrder():
    sellerName: str = request.json.get("sellerName", "")
    o = order.Order
    ok, orderlist = o.sellergetOrder(o, sellerName=sellerName)
    if ok:
        return jsonify({"message": "ok", "orderlist": orderlist}), 200
    else:
        return jsonify({"message": "Inquiry failed, no order", "orderlist": orderlist}), 501

@bp_order.route("/cancelOrder", methods=["POST"])
def cancelOrder():
    orderId: str = request.json.get("orderId", "")
    buyerName: str = request.json.get("buyerName", "")
    o = order.Order
    ok = o.cancelOrder(orderId=orderId, buyerName=buyerName)
    if ok:
        return jsonify({"message": "ok"}), 200
    else:
        return jsonify({"message": "cancel failed, no order or no buyer"}), 501

@bp_order.route("/paymentOrder", methods=["POST"])
def paymentOrder():
    orderId: str = request.json.get("orderId", "")
    buyerName: str = request.json.get("buyerName", "")
    o = order.Order
    ok = o.paymentOrder(orderId=orderId, buyerName=buyerName)
    if ok:
        return jsonify({"message": "ok"}), 200
    else:
        return jsonify({"message": "payment failed, insufficient account balance"}), 501
