import sqlite3 as sqlite
import uuid
import json
from be.model import store
from be.model import db_conn
from be.model import error


class Buyer(db_conn.DBConn):
    def __init__(self):
        db_conn.DBConn.__init__(self)

    def new_order(self, user_id: str, store_id: str, id_and_count: [(str, int)]) -> (int, str, str):
        order_id = ""
        try:
            if not self.user_id_exist(user_id):
                return error.error_non_exist_user_id(user_id) + (order_id, )
            if not self.store_id_exist(store_id):
                return error.error_non_exist_store_id(store_id) + (order_id, )

            for book_id, count in id_and_count:
                cursor = self.conn.execute("SELECT book_id, stock_level FROM store WHERE store_id = ? AND book_id = ?;",
                                           (store_id, book_id))
                row = cursor.fetchone()
                if row is None:
                    return error.error_non_exist_book_id(book_id) + (order_id, )

                stock_level = row[1]
                if stock_level < count:
                    return error.error_stock_level_low(book_id) + (order_id,)

                cursor = self.conn.execute(
                        "UPDATE store set stock_level = stock_level - ?"
                        "WHERE store_id = ? and book_id = ? and stock_level >= ?; ",
                        (count, store_id, book_id, count))
                if cursor.rowcount == 0:
                    return error.error_stock_level_low(book_id) + (order_id, )

            uid = "{}_{}_{}".format(user_id, store_id, str(uuid.uuid1()))
            for book_id, count in id_and_count:
                self.conn.execute(
                        "INSERT INTO order_detail(order_id, book_id, count) "
                        "VALUES(?, ?, ?);",
                        (uid, book_id, count))
            self.conn.execute(
                "INSERT INTO new_order(order_id, store_id, buyer_id) "
                "VALUES(?, ?, ?);",
                (uid, store_id, user_id))
            self.conn.commit()
            order_id = uid
        except sqlite.Error as e:
            return 528, "{}".format(str(e)), ""
        except BaseException as e:
            return 530, "{}".format(str(e)), ""

        return 200, "ok", order_id

    def payment(self, user_id: str, order_id: str) -> (int, str):
        conn = store.get_db_conn()
        try:
            cursor = conn.execute("SELECT order_id, buyer_id, store_id FROM new_order WHERE order_id = ?", (order_id,))
            row = cursor.fetchone()
            if row is None:
                return error.error_invalid_order_id(order_id)

            order_id = row[0]
            buyer_id = row[1]
            store_id = row[2]

            if buyer_id != user_id:
                return error.error_authorization_fail()

            cursor = conn.execute("SELECT balance count FROM user WHERE user_id = ?;", (buyer_id,))
            row = cursor.fetchone()
            if row is None:
                return error.error_non_exist_user_id(buyer_id)
            balance = row[0]

            cursor = conn.execute("SELECT store_id, user_id FROM user_store WHERE store_id = ?;", (store_id,))
            row = cursor.fetchone()
            if row is None:
                return error.error_non_exist_store_id(store_id)

            seller_id = row[1]

            if not self.user_id_exist(seller_id):
                return error.error_non_exist_user_id(seller_id)

            cursor = conn.execute("SELECT book_id, count FROM order_detail WHERE order_id = ?;", (order_id,))
            total_price = 0
            for row in cursor:
                book_id = row[0]
                count = row[1]
                cursor = conn.execute("SELECT book_id, book_info FROM store WHERE store_id = ? AND book_id = ?;",
                                      (store_id, book_id))
                row = cursor.fetchone()
                if row is None:
                    return error.error_non_exist_book_id(book_id)

                book_info = row[1]
                book_info_json = json.loads(book_info)
                price = book_info_json.get("price")
                total_price = total_price + price * count
            if balance < total_price:
                return error.error_not_sufficient_funds(order_id)

            cursor = conn.execute("UPDATE user set balance = balance - ?"
                                  "WHERE user_id = ? AND balance >= ?",
                                  (total_price, buyer_id, total_price))
            if cursor.rowcount == 0:
                return error.error_not_sufficient_funds(order_id)

            cursor = conn.execute("UPDATE user set balance = balance + ?"
                                  "WHERE user_id = ?",
                                  (total_price, buyer_id))
            if cursor.rowcount == 0:
                return error.error_non_exist_user_id(buyer_id)

            conn.commit()

        except sqlite.Error as e:
            return 528, "{}".format(str(e))

        except BaseException as e:
            return 530, "{}".format(str(e))

        return 200, "ok"
