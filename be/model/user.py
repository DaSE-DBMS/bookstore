from be.model import tuple
from be.model import store
import jwt
import time


# encode a json string like:
#   {
#       'username': [user name],
#       'terminal': [terminal code],
#       'timestamp': [ts]} to a JWT
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
#       'username': [user name],
#       'terminal': [terminal code],
#       'timestamp': [ts]} to a JWT
#   }
def jwt_decode(encoded_token, username: str) -> str:
    decoded = jwt.decode(encoded_token, key=username, algorithms="HS256")
    return decoded


class User(tuple.Tuple):
    username: str
    password: str
    token: str
    terminal: str
    token_lifetime: int = 3600  # 3600 second

    def __init__(self, username, password="", token="", terminal=""):
        self.key = username
        self.username = username
        self.password = password
        self.token = token
        self.terminal = terminal

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
        except jwt.exceptions.InvalidSignatureError:
            return False

    def login(self, password: str, terminal: str) -> (bool, str):
        if self.password == password:
            self.token = jwt_encode(self.username, terminal)
            self.terminal = terminal
            return True, self.token
        return False, ""

    def logout(self, token: str) -> bool:
        if not self.check_token(token):
            return False
        self.token = jwt_encode(self.username, terminal="default")
        return True

    def unregister(self, password: str) -> bool:
        if password == self.password:
            store.del_row(User.__name__, self.username)
            return True
        else:
            return False

    def change_password(self, old_password: str, new_password: str) -> bool:
        if self.password != old_password:
            return False

        self.password = new_password
        self.token = jwt_encode(self.username, self.terminal)
        return True


def login(username: str, password: str, terminal: str):
    u: User = store.get_row(User.__name__, username)
    if u is None:
        return False, ""
    else:
        return u.login(password, terminal)


def logout(username: str, token: str):
    u: User = store.get_row(User.__name__, username)
    if u is None:
        return False
    else:
        return u.logout(token)


def register(username: str, password: str) -> bool:
    u = User(username, password)
    ok, _ = store.put_row_absent(User.__name__, u)
    return ok


def unregister(username: str, password: str) -> bool:
    u: User = store.get_row(User.__name__, username)
    if u is None:
        return False
    else:
        return u.unregister(password)


def change_password(username: str, old_password: str, new_password: str) -> bool:
    u: User = store.get_row(User.__name__, username)
    if u is not None:
        return u.change_password(old_password, new_password)
    else:
        return False
