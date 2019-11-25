import pytest
import uuid
from fe.access.new_buyer import register_new_buyer


class TestAddFunds:
    def __init__(self):
        self.user_id = "test_add_funds_{}".format(str(uuid.uuid1()))
        self.password = self.user_id
        self.buyer = register_new_buyer(self.user_id, self.password)

    def test_ok(self):
        code = self.buyer.add_funds(1000)
        assert code == 200

        code = self.buyer.add_funds(-1000)
        assert code == 200

    def test_error_user_id(self):
        self.buyer.user_id = self.buyer.user_id + "_x"
        code = self.buyer.add_funds(10)
        assert code != 200

    def test_error_password(self):
        self.buyer.password = self.buyer.password + "_x"
        code = self.buyer.add_funds(10)
        assert code != 200


def test_add_funds_ok():
    t = TestAddFunds()
    t.test_ok()


def test_add_funds_error_user_id():
    t = TestAddFunds()
    t.test_error_user_id()


def test_add_funds_error_password():
    t = TestAddFunds()
    t.test_error_password()
