from fe.test.new_seller import register_new_seller
from fe.test.gen_book_data import GenBook
from fe.test.new_buyer import register_new_buyer
from fe.access import buyer
from fe import conf
import pytest
import time


@pytest.mark.parametrize(
    "non_exist_book_id, low_stock_level",
    [
        (True, True),
        (True, False),
        (False, True),
        (False, False)
    ]
)
def test_new_order(non_exist_book_id: bool, low_stock_level: bool):
    seller_id = "test_new_order_seller_id_{}".format(time.time())
    store_id = "test_new_order_store_id_{}".format(time.time())
    buyer_id = "test_new_order_buyer_id_{}".format(time.time())
    gen_book = GenBook(seller_id, store_id)
    ok, buy_book_id_list = gen_book.gen(non_exist_book_id=non_exist_book_id, low_stock_level=low_stock_level)
    assert ok

    b = register_new_buyer(buyer_id)
    code, order_id = b.new_order(store_id, buy_book_id_list)

    if not non_exist_book_id and not low_stock_level:
        assert code == 200
    elif non_exist_book_id and not low_stock_level:
        assert code == 515
    elif not non_exist_book_id and low_stock_level:
        assert code == 517
    elif non_exist_book_id and low_stock_level:
        assert code == 515 or code == 517

