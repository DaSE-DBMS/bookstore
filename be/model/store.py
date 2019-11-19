import sqlite3 as sqlite
import logging


class Store:
    database: str

    def __init__(self):
        self.database = "be.db"
        self.init_tables()

    def init_tables(self):
        try:
            conn = self.get_db_conn()
            conn.execute(
                "CREATE TABLE IF NOT EXISTS user ("
                "username TEXT PRIMARY KEY, password TEXT,"
                " token TEXT, terminal TEXT);"
            )
            conn.execute(
                "CREATE TABLE IF NOT EXISTS goods ("
                "goodsId TEXT PRIMARY KEY, goodsName TEXT NOT NULL,"
                "goodsAuth TEXT, goodsPrice TEXT NOT NULL, goodsNum TEXT, "
                "goodsType TEXT, goodsDsr TEXT, sellerName TEXT);"
            )
            conn.execute(
                "CREATE TABLE IF NOT EXISTS orders ("
                "orderId TEXT, buyername TEXT ,"
                "sellerName TEXT, orderStatus TEXT , goodsName TEXT, goodsPrice TEXT, totalValue TEXT, addr TEXT,"
                "PRIMARY KEY(orderId, goodsName));"
            )
            conn.commit()
        except sqlite.Error as e:
            logging.error(e)
            conn.rollback()

    def get_db_conn(self) -> sqlite.Connection:
        return sqlite.connect(self.database)


database_instance = Store()


def get_db_conn():
    return database_instance.get_db_conn()
