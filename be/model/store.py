import os
from typing import Dict
from be.model import table
from be.model import tuple
from be.model import user
import sqlite3 as sqlite


class Store:
    tables: Dict[str, table.Table]
    database: str

    def __init__(self):
        self.database = "be.db"
        self.tables = dict()
        self.create("User")
        self.create("Order")
        self.init_tables()

    def init_tables(self):
        try:
            conn = self.get_db_conn()
            conn.execute(
                "CREATE TABLE IF NOT EXISTS user ("
                "username TEXT PRIMARY KEY, password TEXT,"
                " token TEXT, terminal TEXT);"
            )
            conn.commit()
        except sqlite.Error as e:
            print(e)
            conn.rollback()

    def create(self, table_name: str):
        self.tables[table_name] = table.Table(table_name)

    def get_table(self, table_name: str) -> table.Table:
        return self.tables.get(table_name)

    def get_db_conn(self) -> sqlite.Connection:
        return sqlite.connect(self.database)


database_instance = Store()


def get_db_conn():
    return database_instance.get_db_conn()


def get_row(table_name: str, key: str) -> tuple.Tuple:
    return database_instance.get_table(table_name).get(key)


def del_row(table_name: str, key: str) -> bool:
    return database_instance.get_table(table_name).remove(key)


def put_row(table_name, row: tuple.Tuple):
    database_instance.get_table(table_name).put(row)


def put_row_absent(table_name, row: tuple.Tuple) -> (bool, tuple.Tuple):
    return database_instance.get_table(table_name).put_absent(row)
