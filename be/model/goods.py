from be.model import tuple
from be.model import store
import jwt
import time

def jwt_encode(goodsname: str) -> str:
    encoded = jwt.encode(
        {"goodsname": goodsname},
        key=goodsname,
        algorithm="HS256",
    )
    return encoded.decode("utf-8")


def jwt_decode(goodsname: str) -> str:
    decoded = jwt.decode(key=goodsname, algorithms="HS256")
    return decoded


class Goods(tuple.Tuple):
    goodsname: str


    def __init__(self, goodsname):
        self.key = goodsname
        self.goodsame = goodsname
