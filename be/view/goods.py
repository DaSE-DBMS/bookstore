from flask import Blueprint
from flask import request
from flask import jsonify
from be.model import user, goods

bp_goods = Blueprint("goods", __name__, url_prefix="/goods")

@bp_goods.route("/addGoods", methods=["POST"])
def addGoods():
    goodsId : str = request.json.get("goodsId","")
    goodsName: str = request.json.get("goodsName","")
    goodsauth : str = request.json.get("goodsauth","")
    goodsPrice : str = request.json.get("goodsPrice","")
    goodsNum : str = request.json.get("goodsNum","")
    goodsDsr : str = request.json.get("goodsDsr","")
    g = goods.Goods
    ok = g.addgoods(goodsId, goodsName,goodsauth, goodsPrice, goodsNum,goodsDsr)
    if ok:
        return jsonify({"message": "ok"}), 200
    else:
        return jsonify({"message": "Insert failed"}), 501

