import pytest
import time
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

    assert a.register(username, password)

    # login right
    login_ok, token = a.login(username, password, terminal)
    assert login_ok

    my_token = token

    # login wrong username
    login_ok, token = a.login(username + "xxx", password, terminal)
    assert not login_ok

    # login wrong password
    login_ok, token = a.login(username, password + "xxx", terminal)
    assert not login_ok

    # logout wrong token
    logout_ok = a.logout(username, my_token + "xxx")
    assert not logout_ok

    # logout wrong username
    logout_ok = a.logout(username + "xxx", my_token)
    assert not logout_ok

    # logout right
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

    assert a.register(username, old_password)

    assert a.password(username, old_password, new_password)

    ok, new_token = a.login(username, old_password, terminal)
    assert not ok

    ok, new_token = a.login(username, new_password, terminal)
    assert ok

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

    assert a.register(username, password)

    assert not a.unregister(username + "xxx", password)

    assert not a.unregister(username, password + "xxx")

    assert a.unregister(username, password)

    assert a.register(username, password)

    assert a.unregister(username, password)
