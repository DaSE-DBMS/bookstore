import pytest
import time
import logging
from fe.access import auth
from fe import conf


@pytest.mark.parametrize(
    "user_id",
    [
        "test_add_funds1_{}".format(time.time()),
        "test_add_funds2_{}".format(time.time()),
        "test_add_funds3_{}".format(time.time()),
    ],
)
def test_add_funds(user_id: str):
    a = auth.Auth(conf.URL)
    # register a user

    password = "password_" + user_id
    logging.info("test register a user properly")
    assert a.register(user_id, password, True, True) == 200

    code = a.add_funds(user_id, password, 1000)
    assert code == 200

    a.add_funds(user_id, password, -1000)
    assert code == 200

    code = a.add_funds(user_id, password + "x", 10)
    assert code == 401

    code = a.add_funds(user_id + "x", password, 10)
    assert code == 401
