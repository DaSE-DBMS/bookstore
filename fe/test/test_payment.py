from fe.test.new_seller import register_new_seller
from fe.test.gen_book_data import GenBook
from fe.test.new_buyer import register_new_buyer
from fe.access import auth
from fe.access import buyer
from fe.access.book import Book
from fe import conf
import pytest
import time


@pytest.mark.parametrize(
    "not_suff_funds",
    [
        True,
        False,
    ]
)
def test_payment(not_suff_funds: bool):
    seller_id = "test_payment_seller_id_{}".format(time.time())
    store_id = "test_payment_store_id_{}".format(time.time())
    buyer_id = "test_payment_buyer_id_{}".format(time.time())
    gen_book = GenBook(seller_id, store_id)
    ok, buy_book_id_list = gen_book.gen(non_exist_book_id=False, low_stock_level=False, max_book_count=5)
    buy_book_info_list = gen_book.buy_book_info_list
    assert ok
    b = register_new_buyer(buyer_id)
    code, order_id = b.new_order(store_id, buy_book_id_list)
    assert code == 200

    total_price = 0
    for item in buy_book_info_list:
        book: Book = item[0]
        num = item[1]
        total_price = total_price + book.price * num

    if not_suff_funds:
        code = b.add_funds(total_price - 1)
        assert code == 200

        code = b.payment(order_id)
        assert code == 519
    else:
        code = b.add_funds(total_price)
        assert code == 200
        code = b.payment(order_id)
        assert code == 200

