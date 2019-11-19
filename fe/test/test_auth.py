import pytest
import time
import logging
from fe.access import auth
from fe import conf


@pytest.mark.parametrize(
    "username",
    [
        "test_login1_{}".format(time.time()),
        "test_login2_{}".format(time.time()),
        "test_login3_{}".format(time.time()),
    ],
)
def test_login(username: str):
    a = auth.Auth(conf.URL)
    # register a user

    password = "password_" + username
    terminal = "terminal_" + username
    logging.info("test register a user properly")
    assert a.register(username, password)

    # login right
    logging.info("test user login properly")
    login_ok, token = a.login(username, password, terminal)
    assert login_ok

    my_token = token

    # login wrong username
    logging.info("test user login with a wrong user name")
    login_ok, token = a.login(username + "xxx", password, terminal)
    assert not login_ok

    # login wrong password
    logging.info("test user login with a wrong user password")
    login_ok, token = a.login(username, password + "xxx", terminal)
    assert not login_ok

    # logout wrong token
    logging.info("test user logout with a wrong token")
    logout_ok = a.logout(username, my_token + "xxx")
    assert not logout_ok

    # logout wrong username
    logging.info("test user logout with a wrong username")
    logout_ok = a.logout(username + "xxx", my_token)
    assert not logout_ok

    # logout right
    logging.info("test user logout properly")
    logout_ok = a.logout(username, my_token)
    assert logout_ok


@pytest.mark.parametrize(
    "username",
    [
        "test_password1_{}".format(time.time()),
        "test_password2_{}".format(time.time()),
        "test_password3_{}".format(time.time()),
    ],
)
def test_password(username: str):
    a = auth.Auth(conf.URL)
    # register a user

    old_password = "old_password_" + username
    new_password = "new_password_" + username
    terminal = "terminal_" + username

    logging.info("test register a user properly")
    assert a.register(username, old_password)

    logging.info("test change password with wrong username")
    assert not a.password(username + "_x", old_password, new_password)

    logging.info("test change password with wrong password")
    assert not a.password(username, old_password + "_x", new_password)
    assert a.password(username, old_password, new_password)

    logging.info("test login with old password, return error")
    ok, new_token = a.login(username, old_password, terminal)
    assert not ok

    logging.info("test login with new password properly")
    ok, new_token = a.login(username, new_password, terminal)
    assert ok

    logging.info("test login out with previous token")
    assert a.logout(username, new_token)


@pytest.mark.parametrize(
    "username",
    [
        "test_register1_{}".format(time.time()),
        "test_register2_{}".format(time.time()),
        "test_register3_{}".format(time.time()),
    ],
)
def test_register(username: str):
    a = auth.Auth(conf.URL)

    password = "password_" + username

    logging.info("test register properly")
    assert a.register(username, password)

    logging.info("test register with a exists username")
    assert not a.register(username, password)

    logging.info("test unregister with a non-exists username")
    assert not a.unregister(username + "_x", password)

    logging.info("test unregister with wrong password")
    assert not a.unregister(username, password + "_x")

    logging.info("test unregister properly")
    assert a.unregister(username, password)

    logging.info("test register with previous username")
    assert a.register(username, password)

    logging.info("test unregister")
    assert a.unregister(username, password)
