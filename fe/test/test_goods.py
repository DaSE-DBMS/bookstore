# import pytest
# import time
#
# from fe.access import goods
# from fe import conf
#
#
# @pytest.mark.parametrize(
#     "merchantname",
#     [
#         "test_getmerchantgoods1_{}".format(time.time()),
#         "test_getmerchantgoods2_{}".format(time.time()),
#         "test_getmerchantgoods3_{}".format(time.time()),
#     ],
#     "merchantname"
# )

# def test_getmerchantgoods(merchantname: str):
#     m = merchant.Merchant(conf.URL)
#     # register a merchant
#
#     password = "password_" + username
#     terminal = "terminal_" + username
#
#     assert a.register(username, password)
#
#     # search right
#     login_ok, token = m.login(username, password, terminal)
#     assert login_ok
#
#     # search wrong merchantname
#     login_ok, token = m.login(username + "xxx", password, terminal)
#     assert not login_ok
import pytest
import time
from fe.access import goods
from fe import conf


@pytest.mark.parametrize(
    "username",
    [
        "test_editGoods1_{}".format(time.time()),
        "test_editGoods2_{}".format(time.time()),
        "test_editGoods3_{}".format(time.time()),
    ],
)
def test_editGoods(username: str):
    g = goods.Goods(conf.URL)

    password = "password_" + username

    goodsid = "goodsid_" + username

    goodsName = "goodsname_" + username

    goodsPrice = "goodsPrice_" +username

    goodsNumber = "goodsNumber_" + username

    assert g.editGoods(username, goodsid, goodsName, goodsPrice, goodsNumber)

    assert not a.register(username, goodsid + "_x", goodsName + "_x", goodsPrice + "_x", goodsNumber + "_x")

