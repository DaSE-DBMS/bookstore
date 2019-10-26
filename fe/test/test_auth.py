import pytest
from fe.access import auth
from fe import conf


@pytest.mark.parametrize(
    ("username", "password", "terminal"),
    [
        ("jecl", "qwertyuiohhlxgahx", "macbook"),
        ("xtybx", "xxaegsxxegsersgas", "iphoneX"),
        ("hao2145", "xagkma;jfieisae33", "dell-pc"),
    ],
)
def test_auth(username: str, password: str, terminal: str):
    a = auth.Auth(conf.URL)
    # register a user
    register_ok = a.register(username, password)
    assert register_ok

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

    # login wrong username
    unregister_ok = a.unregister(username + "xxx", password)
    assert not unregister_ok

    # login wrong password
    unregister_ok = a.unregister(username, password + "xxx")
    assert not unregister_ok

    # unregister
    unregister_ok = a.unregister(username, password)
    assert unregister_ok

    # register a user same username
    register_ok = a.register(username, password)
    assert register_ok

    # register a user same username
    register_ok = a.register(username, password)
    assert not register_ok

    # unregister
    unregister_ok = a.unregister(username, password)
    assert unregister_ok
