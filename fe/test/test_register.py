import time
from fe.access import auth
from fe import conf


class TestRegister:
    def __init__(self):
        self.user_id = "test_register_user_{}".format(time.time())
        self.password = "test_register_password_{}".format(time.time())
        self.auth = auth.Auth(conf.URL)

    def test_register_ok(self):
        code = self.auth.register(self.user_id, self.password)
        assert code == 200

    def test_unregister_ok(self):
        code = self.auth.register(self.user_id, self.password)
        assert code == 200

        code = self.auth.unregister(self.user_id, self.password)
        assert code == 200

    def test_unregister_error_authorization(self):
        code = self.auth.register(self.user_id, self.password)
        assert code == 200

        code = self.auth.unregister(self.user_id + "_x", self.password)
        assert code != 200

        code = self.auth.unregister(self.user_id, self.password + "_x")
        assert code != 200

    def test_register_error_exist_user_id(self):
        code = self.auth.register(self.user_id, self.password)
        assert code == 200

        code = self.auth.register(self.user_id, self.password)
        assert code != 200


def test_register_ok():
    t = TestRegister()
    t.test_register_ok()


def test_unregister_ok():
    t = TestRegister()
    t.test_unregister_ok()


def test_unregister_error_authorization():
    t = TestRegister()
    t.test_unregister_error_authorization()


def test_register_error_exist_user_id():
    t = TestRegister()
    t.test_register_error_exist_user_id()
