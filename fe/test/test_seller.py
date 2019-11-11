import pytest
import time
from fe.access import seller
from fe import conf
from fe.access import order


@pytest.mark.parametrize(
    "username",
    [
        "test_getorder1_{}".format(time.time()),
        "test_getorder2_{}".format(time.time()),
        "test_getoreder3_{}".format(time.time()),
    ],
)


def test_getorder(username: str):
    o = order.Order(conf.URL)
    # register a user

    orderId = "orderId" + username
    orderStatus = "terminal_" + username

    assert o.getOrder(username)

    # getorder right
    getorder_ok, orderlist = o.getOrder(username)
    assert not getorder_ok


    # getorder wrong username
    getorder_ok, orderlist = o.getOrder(username+"username")
    assert not getorder_ok
