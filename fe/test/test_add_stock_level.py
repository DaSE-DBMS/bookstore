from fe.test.new_seller import register_new_seller
from fe.access import book
import pytest
import time


@pytest.mark.parametrize(
    "user_id, store_id",
    [
        ("test_add_book_stock_level1_user_{}".format(time.time()),
         "test_add_book_stock_level1_store_{}".format(time.time())),
        ("test_add_book_stock_level2_user_{}".format(time.time()),
         "test_add_book_stock_level2_store_{}".format(time.time())),
    ]
)
def test_add_stock_level(user_id, store_id):
    s = register_new_seller(user_id)

    code = s.create_store(store_id)
    assert code == 200

    books = book.get_book_info(0, 5)
    for b in books:
        code = s.add_book(user_id, store_id, 0, b)
        assert code == 200

    for b in books:
        book_id = b.id
        code = s.add_stock_level(user_id, store_id, book_id, 10)
        assert code == 200

    for b in books:
        book_id = b.id
        # non exist user id
        code = s.add_stock_level(user_id + "x", store_id, book_id, 10)
        assert code == 511

    for b in books:
        book_id = b.id
        # non exist store id
        code = s.add_stock_level(user_id, store_id + "x", book_id, 10)
        assert code == 513

    for b in books:
        book_id = b.id
        # non exist book id
        code = s.add_stock_level(user_id, store_id, book_id + "x", 10)
        assert code == 515
