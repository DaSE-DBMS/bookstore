from flask import Blueprint
from flask import request
from flask import jsonify
from be.model import user

bp_goods = Blueprint("goods", __name__, url_prefix="/goods")

@bp_goods.route("/getmerchantgoods", methods=["POST"])
def getmerchantgoods():
    merchantname = request.json.get("merchantname", "")
    ok, goodstuple = user.searchmerchantgoods(merchantname=merchantname)
    if ok:
        return jsonify({"message": "ok", "goodstuple": goodstuple}), 200
    else:
        return jsonify({"message": "Inexistent Merchant or Goods"}), 501