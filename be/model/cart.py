from be.model import store
import sqlite3 as sqlite
import logging

#判断商品是否还有库存
def check_num(goodsId, goodsNum):
    try:
        conn = store.get_db_conn()
        cursor = conn.execute(
            "SELECT goodsNum from Goods where goodsId=?",
            (goodsId,),
        )
        row = cursor.fetchone()
        if row is None or row[0]-goodsNum < 0:
            return False
    except sqlite.Error as e:
        logging.error(str(e))
        return False
    return True

class Cart:
    buyerName: str
    sellerName: str
    goodsId: str
    goodsName: str
    goodsPrice: int
    goodsNum: int
    totalValue: int

    def __init__(self):
        self.buyerName = ""
        self.sellerName = ""
        self.goodsId = ""
        self.goodsName = ""
        self.goodsPrice = 0
        self.goodsNum = 0
        self.totalValue = 0

    def addCart(buyerName, sellerName, goodsId, goodsName, goodsPrice, goodsNum, totalValue) -> bool:
        conn = store.get_db_conn()
        try:
            #添加一个判断，商品是否还有库存
            if not check_num(goodsId, goodsNum):
                return False
            #判断买家购物车是否已有该商品，没有就加入这个商品，有就改变数量
            cursor = conn.execute(
                "SELECT goodsNum from cart where buyerName=? and goodsId=?",
                (buyerName, goodsId,),
            )
            row = cursor.fetchone()
            if row is None:
                conn.execute(
                    "INSERT into cart(buyerName, sellerName, goodsId, goodsName, goodsPrice, goodsNum, totalValue) VALUES (?, ?, ?, ?, ?, ?, ?);",
                    (buyerName,sellerName, goodsId, goodsName, goodsPrice, goodsNum, totalValue),
                )
            else:
                newgoodsNum = row[0] + goodsNum
                cursor = conn.execute(
                    "SELECT totalValue from cart where buyerName=? and goodsId=?",
                    (buyerName, goodsId,),
                )
                row = cursor.fetchone()
                newtotalValue = row[0] + goodsPrice*goodsName
                conn.execute(
                    "UPDATE cart set goodsNum=?, totalValue = ? where buyerName=? and goodsId=?",
                    (newgoodsNum, newtotalValue, buyerName, goodsId),
                )
            conn.commit()
        except BaseException as e:
            print(e)
            conn.rollback()
            return False
        return True

    def delCart(buyerName, goodsId, goodsNum) -> bool:
        conn = store.get_db_conn()
        try:
            cursor = conn.execute(
                "SELECT goodsNum, goodsPrice from cart where buyerName=? and goodsId=?",
                (buyerName, goodsId,),
            )
            row = cursor.fetchone()
            if row is None:
                return False
            newgoodsNum = row[0] - goodsNum
            newtotalValue = row[1] * newgoodsNum
            if newgoodsNum == 0:
                cursor = conn.execute("DELETE from cart where buyerName=? and goodsId=?", (buyerName, goodsId))
            else:
                conn.execute(
                    "UPDATE cart set goodsNum = ?, totalValue = ? where buyerName=? and goodsId=?",
                    (str(newgoodsNum), str(newtotalValue), buyerName, goodsId),
                )
            conn.commit()
        except BaseException as e:
            print(e)
            conn.rollback()
            return False
        return True

    def getCart(buyerName) -> (bool, list, int):
        conn = store.get_db_conn()
        try:
            cursor = conn.execute(
                "SELECT sellerName, goodsName, goodsPrice, goodsNum, totalValue from cart where buyerName = ?",
                (buyerName,),
            )
            contents = cursor.fetchall()
            if not contents:
                return False, [], 0
            cartlist = []
            sum = 0
            for row in contents:
                a = [row[0], row[1], row[2], row[3]]
                sum += row[4]
                cartlist.append(a)
        except sqlite.Error as e:
            logging.error(str(e))
            return False
        return True, cartlist, sum

