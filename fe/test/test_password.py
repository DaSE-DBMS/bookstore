import pytest
import time
import logging
from fe.access import auth
from fe import conf


@pytest.mark.parametrize(
    "user_id",
    [
        "test_password1_{}".format(time.time()),
        "test_password2_{}".format(time.time()),
        "test_password3_{}".format(time.time()),
    ],
)
def test_password(user_id: str):
    a = auth.Auth(conf.URL)
    # register a user

    old_password = "old_password_" + user_id
    new_password = "new_password_" + user_id
    terminal = "terminal_" + user_id

    logging.info("test register a user properly")
    assert a.register(user_id, old_password) == 200

    logging.info("test change password with wrong user_id")
    code = a.password(user_id + "_x", old_password, new_password)
    assert code == 401

    logging.info("test change password with wrong password")
    code = a.password(user_id, old_password + "_x", new_password)
    assert code == 401

    code = a.password(user_id, old_password, new_password)
    assert code == 200

    logging.info("test login with old password, return error")
    code, new_token = a.login(user_id, old_password, terminal)
    assert code == 401

    logging.info("test login with new password properly")
    code, new_token = a.login(user_id, new_password, terminal)
    assert code == 200

    logging.info("test login out with previous token")
    code = a.logout(user_id, new_token)
    assert code == 200
