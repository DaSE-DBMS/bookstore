import logging
import uuid
import random
import threading
from fe.access import book
from fe.access.new_seller import register_new_seller
from fe.access.new_buyer import register_new_buyer
from fe.access.buyer import Buyer
from fe import conf


class NewOrder:
    def __init__(self, buyer: Buyer, store_id, book_id_and_count):
        self.buyer = buyer
        self.store_id = store_id
        self.book_id_and_count = book_id_and_count

    def run(self) -> (bool, str):
        code, order_id = self.buyer.new_order(self.store_id, self.book_id_and_count)
        return code == 200, order_id


class Payment:
    def __init__(self, buyer:Buyer, order_id):
        self.buyer = buyer
        self.order_id = order_id

    def run(self) -> bool:
        code = self.buyer.payment(self.order_id)
        return code == 200


class Workload:
    def __init__(self):
        self.uuid = str(uuid.uuid1())
        self.book_ids = []
        self.buyer_ids = []
        self.store_ids = []
        self.book_db = book.BookDB(conf.Use_Large_DB)
        self.row_count = self.book_db.get_book_count()

        self.book_num_per_store = conf.Book_Num_Per_Store
        if self.row_count < self.book_num_per_store:
            self.book_num_per_store = self.row_count
        self.store_num_per_user = conf.Store_Num_Per_User
        self.seller_num = conf.Seller_Num
        self.buyer_num = conf.Buyer_Num
        self.session = conf.Session
        self.stock_level = conf.Default_Stock_Level
        self.user_funds = conf.Default_User_Funds
        self.batch_size = conf.Data_Batch_Size
        self.procedure_per_session = conf.Request_Per_Session

        self.n_new_order = 0
        self.n_payment = 0
        self.n_new_order_ok = 0
        self.n_payment_ok = 0
        self.time_new_order = 0
        self.time_payment = 0
        self.lock = threading.Lock()

    def to_seller_id_and_password(self, no: int) -> (str, str):
        return "seller_{}_{}".format(no, self.uuid), "password_seller_{}_{}".format(no, self.uuid)

    def to_buyer_id_and_password(self, no: int) -> (str, str):
        return "buyer_{}_{}".format(no, self.uuid), "buyer_seller_{}_{}".format(no, self.uuid)

    def to_store_id(self, seller_no: int, i):
        return "store_s_{}_{}_{}".format(seller_no, i, self.uuid)

    def gen_database(self):
        logging.info("load data")
        for i in range(1, self.seller_num + 1):
            user_id, password = self.to_seller_id_and_password(i)
            seller = register_new_seller(user_id, password)
            for j in range(1, self.store_num_per_user + 1):
                store_id = self.to_store_id(i, j)
                code = seller.create_store(store_id)
                assert code == 200
                self.store_ids.append(store_id)
                row_no = 0

                while row_no < self.book_num_per_store:
                    books = self.book_db.get_book_info(row_no, self.batch_size)
                    if len(books) == 0:
                        break
                    for bk in books:
                        code = seller.add_book(store_id, self.stock_level, bk)
                        assert code == 200
                        if i == 1 and j == 1:
                            self.book_ids.append(bk.id)
                    row_no = row_no + len(books)
        logging.info("seller data loaded.")
        for k in range(1, self.buyer_num + 1):
            user_id, password = self.to_buyer_id_and_password(k)
            buyer = register_new_buyer(user_id, password)
            buyer.add_funds(self.user_funds)
            self.buyer_ids.append(user_id)
        logging.info("buyer data loaded.")

    def get_new_order(self) -> NewOrder:
        n = random.randint(1, self.buyer_num)
        buyer_id, buyer_password = self.to_buyer_id_and_password(n)
        store_no = int(random.uniform(0, len(self.store_ids) - 1))
        store_id = self.store_ids[store_no]
        books = random.randint(1, 10)
        book_id_and_count = []
        for i in range(0, books):
            book_no = int(random.uniform(0, len(self.book_ids) - 1))
            book_id = self.book_ids[book_no]
            count = random.randint(1, 10)
            book_id_and_count.append((book_id, count))
        b = Buyer(url_prefix=conf.URL, user_id=buyer_id, password=buyer_password)
        new_ord = NewOrder(b, store_id, book_id_and_count)
        return new_ord

    def update_stat(self, n_new_order, n_payment,
                    n_new_order_ok, n_payment_ok,
                    time_new_order, time_payment):
        self.lock.acquire()
        self.n_new_order = self.n_new_order + n_new_order
        self.n_payment = self.n_payment + n_payment
        self.n_new_order_ok = self.n_new_order_ok + n_new_order_ok
        self.n_payment_ok = self.n_payment_ok + n_payment_ok
        self.time_new_order = self.time_new_order + time_new_order
        self.time_payment = self.time_payment + time_payment
        if self.n_payment != 0 and self. n_new_order != 0 \
                and (self.time_payment + self.time_new_order):
            logging.info("TPS_C={}, NO=OK:{} TOTAL:{} LATENCY:{}, P=OK:{} TOTAL:{} LATENCY:{}".format(
                         int(self.n_new_order_ok / (self.time_payment + self.time_new_order)),
                         self.n_new_order_ok, self.n_new_order, self.time_new_order / self.n_new_order,
                         self.n_payment_ok, self.n_payment, self.time_payment / self.n_payment))
        self.lock.release()
