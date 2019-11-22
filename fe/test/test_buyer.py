import time
import pytest
from fe import conf
from fe.access import order, goods, auth


@pytest.mark.parametrize(
    "orderId",
    [
        "test_createOrder1_{}".format(time.time()),
        # "test_createOrder2_{}".format(time.time()),
        # "test_createOrder3_{}".format(time.time()),
    ],
)

def test_createOrder(orderId : str):
    # a = auth.Auth(conf.URL)
    # assert a.register("buyer", "buyer", True, True) == 200
    #
    # g = goods.Goods(conf.URL)
    # g.addGoods("111111","the little prince", "heheda", 33, 5, "ertongwenxue", "haokanhaokanhaokan", "sshuang")
    # g.addGoods("222222", "the beautiful prince", "xixiha", 33, 5, "ertongwenxue", "haokanhaokanhaokan", "sshuang")

    o = order.Order(conf.URL)
    sellerName = "sellerName" + orderId
    buyerName = "buyerName" + orderId
    orderStatus = 2
    cartlist = []
    a = ["the little prince",33,33]
    cartlist.append(a)
    b = ["the beautiful prince",33,33]
    cartlist.append(b)
    addr = "addr" + orderId

    assert o.createOrder(orderId, buyerName, sellerName, orderStatus, cartlist, addr)

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

    # test paymentOrder 这个接口我还没有测，先改后端的逻辑再修改
    # assert o.paymentOrder(orderId, "buyer")



