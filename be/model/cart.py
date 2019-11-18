from be.model import store
import sqlite3 as sqlite
import logging

#判断商品是否还有库存
def check_num(goodsId, goodsNum):
    try:
        conn = store.get_db_conn()
        cursor = conn.execute(
            "SELECT goodsNum from goods where goodsId=?",
            (goodsId),
        )
        row = cursor.fetchone()
        if row is None or row[1]-goodsNum < 0:
            return False
    except sqlite.Error as e:
        logging.error(str(e))
        return False
    return True

class Cart:
    username: str
    goodsId: str
    goodsName: str
    goodsPrice: str
    goodsNum: str
    totalValue: str

    def __init__(self, username, goodsId, goodsName, goodsPrice, goodsNum, totalValue):
        self.username = username
        self.goodsId = goodsId
        self.goodsName = goodsName
        self.goodsPrice = goodsPrice
        self.goodsNum = goodsNum
        self.totalValue = totalValue

    def addCart(username, goodsId, goodsName, goodsPrice, goodsNum, totalValue) -> bool:
        conn = store.get_db_conn()
        try:
            #添加一个判断，商品是否还有库存
            if not check_num(goodsId, goodsNum):
                return False
            conn.execute(
                "INSERT into cart(username, goodsId, goodsName, goodsPrice, goodsNum, totalValue) VALUES (?, ?, ?, ?, ?, ?);",
                (username, goodsId, goodsName, goodsPrice, goodsNum, totalValue),
            )
            conn.commit()
        except BaseException as e:
            print(e)
            conn.rollback()
            return False
        return True

    def delCart(username, goodsId, goodsNum) -> bool:
        conn = store.get_db_conn()
        try:
            cursor = conn.execute(
                "SELECT goodsNum, goodsPrice from cart where username=? and goodsId=?",
                (username, goodsId),
            )
            row = cursor.fetchone()
            if row is None:
                return False
            newgoodsNum = row[0] - goodsNum
            newtotalValue = row[1]*newgoodsNum
            if newgoodsNum == 0:
                cursor = conn.execute("DELETE from cart where username=? and goodsId=?", (username, goodsId))
            else:
                conn.execute(
                    "UPDATE cart set goodsNum = ? where username=? and goodsId=?",
                    (newgoodsNum, username, goodsId),
                )
                conn.execute(
                    "UPDATE cart set totalValue = ? where username=? and goodsId=?",
                    (newtotalValue, username, goodsId),
                )
            conn.commit()
        except BaseException as e:
            print(e)
            conn.rollback()
            return False
        return True

    def getCart(username) -> (bool, list, float):
        conn = store.get_db_conn()
        try:
            cursor = conn.execute(
                "SELECT goodsName, goodsPrice, goodsNum, totalValue from cart where username=?",
                (username),
            )
            contents = cursor.fetchall()
            if contents is None:
                return False, []
            cartlist = []
            sum = 0
            for row in contents:
                a = [row[0], row[1], row[2]]
                sum += row[3]
                cartlist.append(a)
        except sqlite.Error as e:
            logging.error(str(e))
            return False
        return True, cartlist, sum

