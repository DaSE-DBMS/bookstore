import time
import pytest
from fe import conf
from fe.access import order, cart


@pytest.mark.parametrize(
    "orderId",
    [
        "test_createOrder1_{}".format(time.time()),
        "test_createOrder2_{}".format(time.time()),
        "test_createOrder3_{}".format(time.time()),
    ],
)

def test_createOrder(orderId : str):
    o = order.Order(conf.URL)
    sellerName = "selelrName" + orderId
    buyerName = "buyerName" + orderId
    orderStatus = "orderStatus" + orderId
    cartlist = []
    a = [sellerName, buyerName, orderStatus]
    cartlist.append(a)
    b = [sellerName+"x", buyerName+"x", orderStatus+"x"]
    cartlist.append(b)
    addr = "addr" + orderId

    assert o.createOrder(orderId, sellerName, buyerName, orderStatus, cartlist, addr)



