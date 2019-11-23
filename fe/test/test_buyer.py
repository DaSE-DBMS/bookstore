import time
import pytest
from fe import conf
from fe.access import order, cart, goods,auth


@pytest.mark.parametrize(
    "orderId",
    [
        "test_createOrder1_{}".format(time.time()),
        # "test_createOrder2_{}".format(time.time()),
        # "test_createOrder3_{}".format(time.time()),
    ],
)

def test_createOrder(orderId : str):

    o = order.Order(conf.URL)
    sellerName = "sellerName" + orderId
    buyerName = "buyerName" + orderId
    orderStatus = 2
    cartlist = ["111111","222222"]
    addr = "addr" + orderId

    # test cancelOrder
    # assert o.cancelOrder(orderId, buyerName)
    # assert not o.cancelOrder(orderId + "xxx", buyerName)
    # assert not o.cancelOrder(orderId, buyerName + "xxx")

    # test buyergetOrder and sellergetOrder
    # ok, orderlist = o.buyergetOrder(buyerName)
    # assert ok
    # ok, orderlist = o.buyergetOrder(buyerName + "xxx")
    # assert not ok

    # ok, orderlist = o.sellergetOrder(sellerName)
    # assert ok
    # ok, orderlist = o.sellergetOrder(sellerName + "xxx")
    # assert not ok


@pytest.mark.parametrize(
    "goodsId",
    [
        "test_addGoods1_{}".format(time.time()),
        "test_addGoods2_{}".format(time.time()),
        "test_addGoods3_{}".format(time.time()),
    ],
)
def test_addGoods(goodsId: str):
    g = goods.Goods(conf.URL)
    goodsName = "goodsName" + goodsId
    goodsAuth = "goodsAuth" + goodsId
    goodsPrice = 50
    goodsNum = 12
    goodsType = "goodsType" + goodsId
    goodsDsr = "goodsDsr" + goodsId
    sellerName = "sellerName" + goodsId
    buyerName = "buyerName" + goodsId
    totalValue = 1000

    assert g.addGoods(goodsId, goodsName, goodsAuth, goodsPrice, goodsNum,  goodsType, goodsDsr, sellerName)
    # test_addCart
    c = cart.Cart(conf.URL)
    assert c.addCart(buyerName, sellerName, goodsId, goodsName, goodsPrice, goodsNum)

    #test_getCart
    # c = cart.Cart(conf.URL)
    # ok, cartList,sum=c.getCart(buyerName)
    # assert ok
    #
    # #test_delCart
    # assert c.delCart(buyerName, goodsId, goodsNum)
    #
    o = order.Order(conf.URL)
    orderStatus = 2
    cartlist = [goodsId]
    addr = "addr"
    orderId = "orderId" + goodsId

    assert o.createOrder(orderId, buyerName, sellerName, orderStatus, cartlist, addr)

    # test cancelOrder
    # assert o.cancelOrder(orderId, buyerName)
    # assert not o.cancelOrder(orderId + "xxx", buyerName)
    # assert not o.cancelOrder(orderId, buyerName + "xxx")

    a = auth.Auth(conf.URL)
    username = "buyerName" + goodsId
    password = "password" + goodsId
    assert a.register(username, password) == 200
    #assert o.paymentOrder(orderId, buyerName)