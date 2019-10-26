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
        if password != "":
            self.password = password
        if token != "":
            self.token = token
        if terminal != "":
            self.terminal = terminal

    def check_token(self, token) -> bool:
        try:
            jwt_text = jwt_decode(encoded_token=token, username=self.username)
            if (
                jwt_text["username"] == self.username
                and jwt_text["terminal"] == self.terminal
            ):
                ts = jwt_text["timestamp"]
                if ts is not None:
                    now = time.time()
                    if self.token_lifetime > now - ts >= 0:
                        return True
        except jwt.exceptions.InvalidSignatureError:
            return False
        return False

    def login(self) -> (bool, str):
        u: User = store.get_row(User.__name__, self.username)
        if u is None:
            return False, ""

        if u.password == self.password:
            u.token = jwt_encode(self.username, self.terminal)
            u.terminal = self.terminal
            return True, u.token
        return False, ""

        return u.login(password)

    def logout(self) -> bool:
        u: User = store.get_row(User.__name__, self.username)
        if u is None:
            return False

        if not u.check_token(self.token):
            return False

        u.token = jwt_encode(u.username, terminal="default")
        return True

    def register(self) -> bool:
        u = User(self.username, self.password)
        ok, _ = store.put_row_absent(User.__name__, u)
        return ok

    def unregister(self) -> bool:
        u: User = store.get_row(User.__name__, self.username)
        if u is None:
            return False

        if u.password == self.password:
            store.del_row(User.__name__, self.username)
            return True
        else:
            return False
