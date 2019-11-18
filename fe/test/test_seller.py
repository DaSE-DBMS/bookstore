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
    goodsAuth = "goodsAuth" + goodsId
    goodsPrice = "goodsPrice" + goodsId
    goodsNum = "goodsNum" + goodsId
    goodsType = "goodsType" + goodsId
    goodsDsr = "goodsDsr" + goodsId
    sellerName = "sellerName" + goodsId

    assert g.addGoods(goodsId, goodsName, goodsAuth, goodsPrice, goodsNum,  goodsType, goodsDsr, sellerName)


    #test searchgoods()
    ok, goodslist = g.searchGoods(goodsName, goodsType)
    assert ok

    ok, goodslist = g.searchGoods("", goodsType)
    assert ok

    ok, goodslist = g.searchGoods(goodsName, "")
    assert ok

    #这里根据goodsDsr来匹配，所欲传入goodsDsr的一部分
    ok, goodslist = g.searchGoods("goodsDsr", "")
    assert ok

    ok, goodslist = g.searchGoods("", "")
    assert not ok

    ok, goodslist = g.searchGoods(goodsName + "xxx", "")
    assert not ok

    ok, goodslist = g.searchGoods(goodsName, goodsType + "xxx")
    assert not ok

    ok, goodslist = g.searchGoods(goodsName + "xxx", goodsType + "xxx")
    assert not ok







