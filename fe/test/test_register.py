import pytest
import time
import logging
from fe.access import auth
from fe import conf


@pytest.mark.parametrize(
    "user_id",
    [
        "test_register1_{}".format(time.time()),
        "test_register2_{}".format(time.time()),
        "test_register3_{}".format(time.time()),
    ],
)
def test_register(user_id: str):
    a = auth.Auth(conf.URL)

    password = "password_" + user_id

    logging.info("test register as neither seller or buyer")
    assert a.register(user_id, password, False, False) == 512

    logging.info("test register properly")
    assert a.register(user_id, password) == 200

    logging.info("test register with a exists user_id")
    assert a.register(user_id, password) == 511

    logging.info("test unregister with a non-exists user_id")
    assert not a.unregister(user_id + "_x", password)

    logging.info("test unregister with wrong password")
    assert not a.unregister(user_id, password + "_x")

    logging.info("test unregister properly")
    assert a.unregister(user_id, password)

    logging.info("test register with previous user_id")
    assert a.register(user_id, password) == 200

    logging.info("test unregister")
    assert a.unregister(user_id, password)
