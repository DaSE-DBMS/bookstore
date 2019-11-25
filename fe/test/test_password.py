import uuid
from fe.access import auth
from fe import conf


class TestPassword:
    def __init__(self):
        self.auth = auth.Auth(conf.URL)
        # register a user
        self.user_id = "test_password_{}".format(str(uuid.uuid1()))
        self.old_password = "old_password_" + self.user_id
        self.new_password = "new_password_" + self.user_id
        self.terminal = "terminal_" + self.user_id

        assert self.auth.register(self.user_id, self.old_password) == 200

    def test_ok(self):
        code = self.auth.password(self.user_id, self.old_password, self.new_password)
        assert code == 200

        code, new_token = self.auth.login(self.user_id, self.old_password, self.terminal)
        assert code != 200

        code, new_token = self.auth.login(self.user_id, self.new_password, self.terminal)
        assert code == 200

        code = self.auth.logout(self.user_id, new_token)
        assert code == 200

    def test_error_password(self):
        code = self.auth.password(self.user_id, self.old_password + "_x", self.new_password)
        assert code != 200

        code, new_token = self.auth.login(self.user_id, self.new_password, self.terminal)
        assert code != 200

    def test_error_user_id(self):
        code = self.auth.password(self.user_id + "_x", self.old_password, self.new_password)
        assert code != 200

        code, new_token = self.auth.login(self.user_id, self.new_password, self.terminal)
        assert code != 200


def test_password_ok():
    t = TestPassword()
    t.test_ok()


def test_password_error_user_id():
    t = TestPassword()
    t.test_error_user_id()


def test_password_error_password():
    t = TestPassword()
    t.test_error_password()
