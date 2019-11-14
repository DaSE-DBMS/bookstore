from be.model import tuple
from be.model import store
import jwt
import time

class Goods(tuple.Tuple):
    username: str
    goodsid: str
    goodsName: str
    goodsPrice: str
    goodsNumber: str

    def __init__(self, username, goodsId, goodsName, goodsPrice, goodsNumber):
        self.key = goodsId
        self.username = username
        self.goodsName = goodsName
        self.goodsPrice = goodsPrice
        self.goodsNumber = goodsNumber


def editGoods(username: str, goodsid: str, goodsName: str, goodsPrice: str, goodsNumber: str) -> bool:
    g = Goods(username, goodsid, goodsName, goodsPrice, goodsNumber)
    ok, _ = store.put_row_absent(Goods.__name__, g)
    return ok
