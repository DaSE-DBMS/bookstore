import pytest
import time
import logging
from fe.access import auth
from fe import conf


@pytest.mark.parametrize(
    "user_id",
    [
        "test_login1_{}".format(time.time()),
        "test_login2_{}".format(time.time()),
        "test_login3_{}".format(time.time()),
    ],
)
def test_login(user_id: str):
    a = auth.Auth(conf.URL)
    # register a user

    password = "password_" + user_id
    terminal = "terminal_" + user_id
    logging.info("test register a user properly")
    assert a.register(user_id, password, True, True) == 200

    # login right
    logging.info("test user login properly")
    code, token = a.login(user_id, password, terminal)
    assert code == 200

    my_token = token

    # login wrong user_id
    logging.info("test user login with a wrong user name")
    code, token = a.login(user_id + "xxx", password, terminal)
    assert code == 401

    # login wrong password
    logging.info("test user login with a wrong user password")
    code, token = a.login(user_id, password + "xxx", terminal)
    assert code == 401

    # logout wrong token
    logging.info("test user logout with a wrong token")
    code = a.logout(user_id, my_token + "xxx")
    assert code == 401

    # logout wrong user_id
    logging.info("test user logout with a wrong user_id")
    code = a.logout(user_id + "xxx", my_token)
    assert code == 401

    # logout right
    logging.info("test user logout properly")
    code = a.logout(user_id, my_token)
    assert code == 200
