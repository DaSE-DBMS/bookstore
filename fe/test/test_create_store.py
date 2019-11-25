from fe.test.new_seller import register_new_seller
import pytest
import time


@pytest.mark.parametrize(
    "user_id",
    [
        "test_create_store1_user_{}".format(time.time()),
        "test_create_store2_user_{}".format(time.time()),
    ]
)
def test_create_store(user_id):
    s = register_new_seller(user_id)

    store_id = "new_store_{}".format(time.time())
    code = s.create_store(store_id)
    assert code == 200

    code = s.create_store(store_id)
    # exist store name
    assert code == 514
