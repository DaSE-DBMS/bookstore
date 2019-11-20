import logging
import os
import sqlite3 as sqlite


class Store:
    database: str

    def __init__(self, db_path):
        self.database = os.path.join(db_path, "be.db")
        self.init_tables()

    def init_tables(self):
        try:
            conn = self.get_db_conn()
            conn.execute(
                "CREATE TABLE IF NOT EXISTS user ("
                "username TEXT PRIMARY KEY, password TEXT NOT NULL, "
                "is_buyer BOOLEAN NOT NULL, is_seller BOOLEAN NOT NULL, "
                "balance INTEGER NOT NULL, token TEXT, terminal TEXT);"
            )
            conn.execute(
                "CREATE TABLE IF NOT EXISTS goods ("
                "goodsId TEXT PRIMARY KEY, goodsName TEXT NOT NULL,"
                "goodsAuth TEXT, goodsPrice INTEGER NOT NULL, goodsNum INTEGER, goodsType TEXT, goodsDsr TEXT, sellerName TEXT);"
            )
            conn.execute(
                "CREATE TABLE IF NOT EXISTS orders ("
                "orderId TEXT, buyerName TEXT ,"
                "sellerName TEXT, orderStatus INTEGER , goodsName TEXT, goodsPrice INTEGER, totalValue INTEGER, addr TEXT,"
                "PRIMARY KEY(orderId, goodsName));"
            )
            conn.execute(
                "CREATE TABLE IF NOT EXISTS cart ("
                "buyerName TEXT,sellerName TEXT , goodsId TEXT, goodsName TEXT, goodsPrice INTEGER, goodsNum INTEGER, totalValue INTEGER,"
                "PRIMARY KEY (buyerName, goodsId));"
            )
            conn.commit()
        except sqlite.Error as e:
            logging.error(e)
            conn.rollback()

    def get_db_conn(self) -> sqlite.Connection:
        return sqlite.connect(self.database)


database_instance: Store = None


def init_database(db_path):
    global database_instance
    database_instance = Store(db_path)


def get_db_conn():
    global database_instance
    return database_instance.get_db_conn()
