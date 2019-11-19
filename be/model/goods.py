import sqlite3 as sqlite
import logging
from be.model import store


class Goods:
    goodsId: str
    goodsName: str
    goodsAuth: str
    goodsPrice: str
    goodsNum: str
    goodsType: str
    goodsDsr: str
    sellerName: str

    def __init__(self):
        self.goodsId = ""
        self.goodsName = ""
        self.goodsAuth = ""
        self.goodsPrice = ""
        self.goodsNum = ""
        self.goodsType = ""
        self.goodsDsr = ""
        self.sellerName = ""

    def addGoods(goodsId, goodsName, goodsAuth, goodsPrice, goodsNum, goodsType, goodsDsr, sellerName) -> bool:
        conn = store.get_db_conn()
        try:
            conn.execute(
                "INSERT into goods(goodsId, goodsName, goodsAuth, goodsPrice, goodsNum, goodsType, goodsDsr, sellerName) VALUES (?, ?, ?, ?, ?, ?, ?, ?);",
                (goodsId, goodsName, goodsAuth, goodsPrice, goodsNum, goodsType, goodsDsr, sellerName),
            )
            conn.commit()
        except BaseException as e:
            print(e)
            conn.rollback()
            return False
        return True

    def searchGoods(keywords, goodsType) -> (bool, list):
            conn = store.get_db_conn()
            try:
                if keywords == "" and goodsType == "":
                    return False, []

                elif keywords != "" and goodsType == "":
                    cursor = conn.execute(
                        "SELECT goodsId, goodsName, goodsAuth, goodsPrice, goodsNum, goodsType, goodsDsr,sellerName from goods where goodsname=?",
                        (keywords,),
                    )
                    contents = cursor.fetchall()
                    if not contents:
                        cursor = conn.execute(
                            "SELECT goodsId, goodsName, goodsAuth, goodsPrice, goodsNum, goodsType, goodsDsr,sellerName from goods where goodsDsr LIKE ?",
                            ('%' + keywords + '%',),
                        )
                        contents = cursor.fetchall()
                        if not contents:
                            return False, []

                elif keywords == "" and goodsType != "":
                    cursor = conn.execute(
                        "SELECT goodsId, goodsName, goodsAuth, goodsPrice, goodsNum, goodsType, goodsDsr,sellerName from goods where goodsType=?",
                        (goodsType,),
                    )
                    contents = cursor.fetchall()
                    if not contents:
                        return False, []
                else:
                    cursor = conn.execute(
                        "SELECT goodsId, goodsName, goodsAuth, goodsPrice, goodsNum, goodsType, goodsDsr,sellerName from goods where goodsType=? and goodsname=?",
                        (goodsType, keywords),
                    )
                    contents = cursor.fetchall()
                    if not contents:
                        return False, []

                goodslist = []
                for row in contents:
                    a = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
                    goodslist.append(a)

            except sqlite.Error as e:
                logging.error(str(e))
                return False, []
            return True, goodslist

