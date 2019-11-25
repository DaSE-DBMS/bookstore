from fe.access.new_seller import register_new_seller
import uuid


class TestCreateStore:
    def __init__(self):
        self.user_id = "test_create_store_user_{}".format(str(uuid.uuid1()))
        self.store_id = "test_create_store_store_{}".format(str(uuid.uuid1()))
        self.password = self.user_id

    def test_ok(self):
        self.seller = register_new_seller(self.user_id, self.password)
        code = self.seller.create_store(self.store_id)
        assert code == 200

    def test_error_exist_store_id(self):
        self.seller = register_new_seller(self.user_id, self.password)
        code = self.seller.create_store(self.store_id)
        assert code == 200

        code = self.seller.create_store(self.store_id)
        assert code != 200


def test_create_store_ok():
    t = TestCreateStore()
    t.test_ok()


def test_create_store_error_exist_store_id():
    t = TestCreateStore()
    t.test_error_exist_store_id()
