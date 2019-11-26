import pytest
import time
import logging
from fe.access import auth
from fe import conf
from fe.test.new_buyer import register_new_buyer

@pytest.mark.parametrize(
    "user_id",
    [
        "test_add_funds1_{}".format(time.time()),
        "test_add_funds2_{}".format(time.time()),
        "test_add_funds3_{}".format(time.time()),
    ],
)
def test_add_funds(user_id: str):
    buyer = register_new_buyer(user_id)

    code = buyer.add_funds(1000)
    assert code == 200

    buyer.add_funds(-1000)
    assert code == 200

    buyer.user_id = buyer.user_id + "_x"
    code = buyer.add_funds(10)
    assert code == 401

    buyer.password = buyer.password + "_x"
    code = buyer.add_funds(10)
    assert code == 401
