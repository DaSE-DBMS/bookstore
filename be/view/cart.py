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
    c = cart.Cart
    ok = c.addCart(buyerName, sellerName, goodsId, goodsName, goodsPrice, goodsNum)
    if ok == 2:
        return jsonify({"message": "ok"}), 200
    elif ok == 1:
        return jsonify({"message": "Insert failed, insufficient stock of goods"}), 514
    else:
        return jsonify({"message": "Insert failed, token error"}), 401

@bp_cart.route("/delCart", methods=["POST"])
def delCart():
    buyerName : str = request.json.get("buyerName","")
    goodsId : str = request.json.get("goodsId","")
    goodsNum : str = request.json.get("goodsNum","")
    c = cart.Cart
    ok = c.delCart(buyerName, goodsId, goodsNum)
    if ok == 2:
        return jsonify({"message": "ok"}), 200
    elif ok == 1:
        return jsonify({"message": "Delete failed, no goods"}), 513
    else:
        return jsonify({"message": "Delete failed, token error"}), 401

@bp_cart.route("/getCart", methods=["POST"])
def getCart():
    buyerName: str = request.json.get("buyerName", "")
    c = cart.Cart
    ok, cartlist, sum = c.getCart(buyerName)
    #ok, cartlist = c.getCart(buyerName)
    if ok:
        return jsonify({"message": "ok", "cartlist": cartlist, "sum": sum}), 200
    else:
        return jsonify({"message": "Access failed, token error"}), 401