from flask import Blueprint
from flask import request
from flask import jsonify
from be.model import goods


bp_goods = Blueprint("goods", __name__, url_prefix="/goods")

@bp_goods.route("/addGoods", methods=["POST"])
def addGoods():
    goodsId : str = request.json.get("goodsId","")
    goodsName: str = request.json.get("goodsName","")
    goodsAuth : str = request.json.get("goodsAuth","")
    goodsPrice : str = request.json.get("goodsPrice","")
    goodsNum : str = request.json.get("goodsNum","")
    goodsType : str = request.json.get("goodsType","")
    goodsDsr : str = request.json.get("goodsDsr","")
    sellerName : str = request.json.get("sellerName","")
    g = goods.Goods
    ok = g.addGoods(goodsId, goodsName, goodsAuth, goodsPrice, goodsNum, goodsType, goodsDsr,sellerName)
    if ok:
        return jsonify({"message": "ok"}), 200
    else:
        return jsonify({"message": "Insert failed"}), 501

@bp_goods.route("/searchGoods", methods=["GET"])
def searchGoods():
    keywords : str = request.json.get("keywords","")
    goodsType: str = request.json.get("goodsType","")
    g = goods.Goods
    ok, goodslist = g.searchGoods(keywords, goodsType)
    if ok:
        return jsonify({"message": "ok", "goodslist": goodslist}), 200
    else:
        return jsonify({"message": "Search failed, no relevant products"}), 501
