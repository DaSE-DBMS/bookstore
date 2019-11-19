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
        if row is None or float(row[0])-float(goodsNum) < 0:
            return False
    except sqlite.Error as e:
        logging.error(str(e))
        return False
    return True

class Cart:
    sellerName: str
    goodsId: str
    goodsName: str
    goodsPrice: str
    goodsNum: str
    totalValue: str

    def __init__(self, sellerName, goodsId, goodsName, goodsPrice, goodsNum, totalValue):
        self.sellerName = sellerName
        self.goodsId = goodsId
        self.goodsName = goodsName
        self.goodsPrice = goodsPrice
        self.goodsNum = goodsNum
        self.totalValue = totalValue

    def addCart(sellerName, goodsId, goodsName, goodsPrice, goodsNum, totalValue) -> bool:
        conn = store.get_db_conn()
        try:
            #添加一个判断，商品是否还有库存
            if not check_num(goodsId, goodsNum):
                return False
            #判断买家购物车是否已有该商品，没有就加入这个商品，有就改变数量
            cursor = conn.execute(
                "SELECT goodsNum from cart where sellerName=? and goodsId=?",
                (sellerName, goodsId),
            )
            row = cursor.fetchone()
            if row is None:
                conn.execute(
                    "INSERT into cart(sellerName, goodsId, goodsName, goodsPrice, goodsNum, totalValue) VALUES (?, ?, ?, ?, ?, ?);",
                    (sellerName, goodsId, goodsName, goodsPrice, goodsNum, totalValue),
                )
            else:
                newgoodsNum = float(row[0]) + float(goodsNum)
                cursor = conn.execute(
                    "SELECT totalValue from cart where sellerName=? and goodsId=?",
                    (sellerName, goodsId),
                )
                row = cursor.fetchone()
                newtotalValue = float(row[0]) + float(goodsPrice)*float(goodsName)
                conn.execute(
                    "UPDATE cart set goodsNum=?, totalValue = ? where sellerName=? and goodsId=?",
                    (str(newgoodsNum), str(newtotalValue), sellerName, goodsId),
                )
            conn.commit()
        except BaseException as e:
            print(e)
            conn.rollback()
            return False
        return True

    def delCart(sellerName, goodsId, goodsNum) -> bool:
        conn = store.get_db_conn()
        try:
            cursor = conn.execute(
                "SELECT goodsNum, goodsPrice from cart where sellerName=? and goodsId=?",
                (sellerName, goodsId),
            )
            row = cursor.fetchone()
            if row is None:
                return False
            newgoodsNum = float(row[0]) - float(goodsNum)
            newtotalValue = float(row[1])*float(newgoodsNum)
            if newgoodsNum == 0:
                cursor = conn.execute("DELETE from cart where sellerName=? and goodsId=?", (sellerName, goodsId))
            else:
                conn.execute(
                    "UPDATE cart set goodsNum = ?, totalValue = ? where sellerName=? and goodsId=?",
                    (str(newgoodsNum), str(newtotalValue), sellerName, goodsId),
                )
            conn.commit()
        except BaseException as e:
            print(e)
            conn.rollback()
            return False
        return True

    def getCart(sellerName) -> (bool, list, float):
        conn = store.get_db_conn()
        try:
            cursor = conn.execute(
                "SELECT goodsName, goodsPrice, goodsNum, totalValue from carts where sellerName=?",
                (sellerName),
            )
            contents = cursor.fetchall()
            if contents:
                return False, [], 0
            cartlist = []
            sum = 0.0
            for row in contents:
                a = [row[0], row[1], row[2]]
                sum += float(row[3])
                cartlist.append(a)
        except sqlite.Error as e:
            logging.error(str(e))
            return False
        return True, cartlist, sum

