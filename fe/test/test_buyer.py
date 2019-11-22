import random
import time
import pytest
from fe import conf
from fe.access import order, cart, goods


# @pytest.mark.parametrize(
#     "orderId",
#     [
#         "test_createOrder1_{}".format(time.time()),
#         "test_createOrder2_{}".format(time.time()),
#         "test_createOrder3_{}".format(time.time()),
#     ],
# )
#
# def test_createOrder(orderId : str):
#     o = order.Order(conf.URL)
#     sellerName = "selelrName" + orderId
#     buyerName = "buyerName" + orderId
#     orderStatus = "orderStatus" + orderId
#     cartlist = []
#     a = [sellerName, buyerName, orderStatus]
#     cartlist.append(a)
#     b = [sellerName+"x", buyerName+"x", orderStatus+"x"]
#     cartlist.append(b)
#     addr = "addr" + orderId
#
#     assert o.createOrder(orderId, sellerName, buyerName, orderStatus, cartlist, addr)
#
#     assert o.cancelOrder(orderId, buyerName)

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
    # goodsPrice = "goodsPrice" + goodsId
    goodsPrice = random.randint(100,200)
    goodsNum = 12
    goodsType = "goodsType" + goodsId
    goodsDsr = "goodsDsr" + goodsId
    sellerName = "sellerName" + goodsId
    buyerName = "buyerName" + goodsId
    totalValue = 1000

    assert g.addGoods(goodsId, goodsName, goodsAuth, goodsPrice, goodsNum,  goodsType, goodsDsr, sellerName)
    # test_addCart
    c = cart.Cart(conf.URL)
    assert c.addCart(buyerName,sellerName,goodsId,goodsName,goodsPrice,3,totalValue)

    # test_delCart
    # buyerName, goodsId, goodsNum
    # assert c.delCart(buyerName,goodsId,1)

    # test_getCart
    # buyerName
    # assert c.getCart(buyerName)


