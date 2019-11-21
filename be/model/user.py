from be.model import store
import jwt
import time
import logging
import sqlite3 as sqlite


# encode a json string like:
#   {
#       "username": [user name],
#       "terminal": [terminal code],
#       "timestamp": [ts]} to a JWT
#   }


def jwt_encode(username: str, terminal: str) -> str:
    encoded = jwt.encode(
        {"username": username, "terminal": terminal, "timestamp": time.time()},
        key=username,
        algorithm="HS256",
    )
    return encoded.decode("utf-8")


# decode a JWT to a json string like:
#   {
#       "username": [user name],
#       "terminal": [terminal code],
#       "timestamp": [ts]} to a JWT
#   }
def jwt_decode(encoded_token, username: str) -> str:
    decoded = jwt.decode(encoded_token, key=username, algorithms="HS256")
    return decoded


class User:
    username: str
    password: str
    token: str
    terminal: str
    balance: int
    token_lifetime: int = 3600  # 3600 second
    is_buyer: bool = False
    is_seller: bool = False

    def __init__(self):
        self.username = ""
        self.password = ""
        self.token = ""
        self.terminal = ""

    def check_token(self, token) -> bool:
        try:
            if self.token != token:
                return False
            jwt_text = jwt_decode(encoded_token=token, username=self.username)
            ts = jwt_text["timestamp"]
            if ts is not None:
                now = time.time()
                if self.token_lifetime > now - ts >= 0:
                    return True
        except jwt.exceptions.InvalidSignatureError as e:
            logging.error(str(e))
            return False

    def fetch_user(self, username) -> bool:
        try:
            conn = store.get_db_conn()
            cursor = conn.execute(
                "SELECT username, password, token, terminal from user where username=?",
                (username,),
            )
            row = cursor.fetchone()
            if row is None:
                return False
            self.username = username
            self.password = row[1]
            self.token = row[2]
            self.terminal = row[3]
        except sqlite.Error as e:
            logging.error(str(e))
            return False
        return True

    def update_token(self):
        conn = store.get_db_conn()
        try:
            conn.execute(
                "UPDATE user set token = ?, terminal = ? where username=?",
                (self.token, self.terminal, self.username),
            )
            conn.commit()
        except sqlite.Error as e:
            logging.error(str(e))
            conn.rollback()

    def update_password(self):
        conn = store.get_db_conn()
        try:
            conn.execute(
                "UPDATE user set password = ?, token= ? , terminal = ? where username = ?",
                (self.password, self.token, self.terminal, self.username),
            )
            conn.commit()
        except sqlite.Error as e:
            logging.error(str(e))
            conn.rollback()

    def delete_user(self):
        conn = store.get_db_conn()
        try:
            cursor = conn.execute("DELETE from user where username=?", (self.username,))
            if cursor.rowcount == 1:
                conn.commit()
            else:
                conn.rollback()
        except sqlite.Error as e:
            logging.error(str(e))
            conn.rollback()

    def login(self, username: str, password: str, terminal: str) -> (bool, str):
        if not self.fetch_user(username):
            return False, ""

        if self.password == password:
            self.token = jwt_encode(username, terminal)
            self.terminal = terminal

            self.update_token()
            return True, self.token
        else:
            return False, ""

    def logout(self, username: str, token: str) -> bool:
        if not self.fetch_user(username):
            return False
        if not self.check_token(token):
            return False
        self.token = jwt_encode(self.username, terminal="default")
        self.update_token()
        return True

    def register(
        self, username: str, password: str, is_buyer: bool, is_seller: bool
    ) -> bool:
        self.username = username
        self.password = password
        self.is_buyer = is_buyer
        self.is_seller = is_seller
        return self.insert_user()

    def insert_user(self) -> bool:
        conn = store.get_db_conn()
        try:
            conn.execute(
                "INSERT into user(username, password, is_buyer, is_seller, balance, token, terminal) "
                "VALUES (?, ?, ?, ?, ?, '', '');",
                (self.username, self.password, self.is_buyer, self.is_seller, 0),
            )
            conn.commit()
        except sqlite.Error as e:
            print(e)
            conn.rollback()
            return False
        return True

    def unregister(self, username: str, password: str) -> bool:
        if not self.fetch_user(username):
            return False
        if self.password == password:
            self.delete_user()
            return True
        else:
            return False

    def change_password(
        self, username: str, old_password: str, new_password: str
    ) -> bool:
        if not self.fetch_user(username):
            return False
        if self.password != old_password:
            return False

        self.password = new_password
        self.token = ""
        self.terminal = ""
        self.update_password()
        return True
