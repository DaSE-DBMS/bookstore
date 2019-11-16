from sqlalchemy.dialects import sqlite
from be.model import store


class Goods:
    goodsId: str
    goodsName: str
    goodsauth: str
    goodsPrice: str
    goodsNum: str
    goodsDsr: str

    def __init__(self):
        self.goodsId = ""
        self.goodsName = ""
        self.goodsauth = ""
        self.goodsPrice = ""
        self.goodsNum = ""
        self.goodsDsr = ""

    def addgoods(goodsId, goodsName,goodsauth, goodsPrice, goodsNum,goodsDsr) -> bool:
        conn = store.get_db_conn()
        try:
            conn.execute(
                "INSERT into goods( goodsId, goodsName,goodsauth, goodsPrice, goodsNum,goodsDsr) VALUES (?, ?, ?, ?, ?,?);",
                (goodsId, goodsName,goodsauth, goodsPrice, goodsNum,goodsDsr),
            )
            conn.commit()
        except BaseException as e:
            print(e)
            conn.rollback()
            return False
        return True

