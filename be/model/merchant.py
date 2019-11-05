from be.model import tuple
from be.model import store
import jwt
import time



def jwt_encode(merhcantname: str, terminal: str) -> str:
    encoded = jwt.encode(
        {"merchantname": merhcantname, "terminal": terminal, "timestamp": time.time()},
        key=merhcantname,
        algorithm="HS256",
    )
    return encoded.decode("utf-8")

def jwt_decode(encoded_token, merhcantname: str) -> str:
    decoded = jwt.decode(encoded_token, key=merhcantname, algorithms="HS256")
    return decoded


class Merchant(tuple.Tuple):
    merchantname: str
    password: str
    token: str
    terminal: str
    token_lifetime: int = 3600  # 3600 second

    def __init__(self, merchantname, password="", token="", terminal=""):
        self.key = merchantname
        self.username = merchantname
        self.password = password
        self.token = token
        self.terminal = terminal

    def check_token(self, token) -> bool:
        try:
            if self.token != token:
                return False
            jwt_text = jwt_decode(encoded_token=token, merchantname=self.merchantname)
            ts = jwt_text["timestamp"]
            if ts is not None:
                now = time.time()
                if self.token_lifetime > now - ts >= 0:
                    return True
        except jwt.exceptions.InvalidSignatureError:
            return False