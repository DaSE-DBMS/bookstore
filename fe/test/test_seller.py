import time
import pytest
from fe import conf
from fe.access import goods

@pytest.mark.parametrize(
    "goodsId",
    [
        "test_addGoods1_{}".format(time.time()),
        "test_addGoods2_{}".format(time.time()),
        "test_addGoods3_{}".format(time.time()),
    ],
)

def test_addGoods(goodsId : str):
    g = goods.Goods(conf.URL)
    goodsName = "goodsName" + goodsId
    goodsauth = "goodsauth" + goodsId
    goodsPrice = "goodsPrice" + goodsId
    goodsNum = "goodsNum" + goodsId
    goodsDsr = "goodsDsr" + goodsId

    assert g.addGoods(goodsId, goodsName,goodsauth, goodsPrice, goodsNum,goodsDsr)



