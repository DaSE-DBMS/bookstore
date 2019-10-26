from be.model import tuple
from typing import Dict
from os import path
import threading


class Table:
    table_name: str
    path: str
    tuples: Dict[str, tuple.Tuple]
    lock: threading.Lock

    def __init__(self, table_name):
        self.table_name = table_name
        self.tuples = dict()
        self.lock = threading.Lock()

    def __json_path__(self):
        json = "{}.json".format(self.table_name)
        return path.join(self.path, json)

    # return value (put success, previous value in dict)
    def put_absent(self, row: tuple.Tuple) -> (bool, tuple.Tuple):
        with self.lock:
            if row.key in self.tuples:
                return False, self.tuples[row.key]
            else:
                self.tuples[row.key] = row
                return True, None

    def put(self, row: tuple.Tuple):
        with self.lock:
            self.tuples[row.key] = row

    def get(self, key: str) -> tuple.Tuple:
        with self.lock:
            if key in self.tuples:
                return self.tuples[key]
            else:
                return None

    def remove(self, key: str) -> bool:
        with self.lock:
            if key in self.tuples:
                del self.tuples[key]
                return True
            else:
                return False
