from flask import Blueprint
from flask import request
from flask import jsonify
from be.model import cart

bp_cart = Blueprint("cart", __name__, url_prefix="/cart")

@bp_cart.route("/addCart", methods=["POST"])
def addCart():
    buyerName: str = request.json.get("buyerName", "")
    sellerName : str = request.json.get("sellerName","")
    goodsId : str = request.json.get("goodsId","")
    goodsName: str = request.json.get("goodsName","")
    goodsPrice : str = request.json.get("goodsPrice","")
    goodsNum : str = request.json.get("goodsNum","")
    totalValue : str = request.json.get("totalValue","")
    c = cart.Cart
    ok = c.addCart(buyerName, sellerName, goodsId, goodsName, goodsPrice, goodsNum, totalValue)
    if ok:
        return jsonify({"message": "ok"}), 200
    else:
        return jsonify({"message": "addition failed, insufficient stock of goods"}), 501

@bp_cart.route("/delCart", methods=["POST"])
def delCart():
    sellerName : str = request.json.get("sellerName","")
    goodsId : str = request.json.get("goodsId","")
    goodsNum : str = request.json.get("goodsNum","")
    c = cart.Cart
    ok = c.delCart(sellerName, goodsId, goodsNum)
    if ok:
        return jsonify({"message": "ok"}), 200
    else:
        return jsonify({"message": "Delete failed, token error"}), 401

@bp_cart.route("/getCart", methods=["POST"])
def getCart():
    sellerName: str = request.json.get("sellerName", "")
    c = cart.Cart
    ok, cartlist, sum = c.getCart(sellerName)
    if ok:
        return jsonify({"message": "ok", "cartlist": cartlist, "sum": sum}), 200
    else:
        return jsonify({"message": "Access failed, token error"}), 401