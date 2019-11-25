from fe.test.new_seller import register_new_seller
from fe.access import book
import pytest
import time


@pytest.mark.parametrize(
    "user_id, store_id",
    [
        ("test_add_books1_user_{}".format(time.time()),
         "test_add_books1_store_{}".format(time.time())),
        ("test_add_books2_user_{}".format(time.time()),
         "test_add_books2_store_{}".format(time.time())),
    ]
)
def test_add_books(user_id, store_id):
    s = register_new_seller(user_id)

    code = s.create_store(store_id)
    assert code == 200

    books = book.get_book_info(0, 2)
    for b in books:
        code = s.add_book(user_id, store_id, 0, b)
        assert code == 200

    for b in books:
        # non exist user id
        code = s.add_book(user_id + "x", store_id, 0, b)
        assert code == 511

    for b in books:
        # non exist store id
        code = s.add_book(user_id, store_id + "x", 0, b)
        assert code == 513

    for b in books:
        # exist book id
        code = s.add_book(user_id, store_id, 0, b)
        assert code == 516

