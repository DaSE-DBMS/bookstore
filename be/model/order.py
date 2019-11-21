from be.model import store
import sqlite3 as sqlite
import logging


class Order:
    orderId: str
    buyerName: str
    sellerName: str
    orderStatus: int  #0交易失败 1交易成功 2待支付 3支付成功
    goodsName: str
    goodsPrice: int
    totalValue: int
    addr: str

    def __init__(self):
        self.orderId = ""
        self.buyerName = ""
        self.sellerName = ""
        self.orderStatus = 2
        self.goodsName = ""
        self.goodsPrice = 0
        self.totalValue = 0
        self.addr = ""

    #注意这里传进来carlist是很多商品信息，包括goodsName，goodsPrice，totalValue
    def createOrder(orderId, sellerName, buyerName, orderStatus, cartlist, addr):
        conn = store.get_db_conn()
        try:
            for good in cartlist:
                conn.execute(
                    "INSERT into orders(orderId, buyerName, sellerName , orderStatus, goodsName, goodsPrice, totalValue, addr) VALUES (?, ?, ?, ?, ?, ?, ? ,?);",
                    (orderId, buyerName, sellerName, orderStatus, good[0], good[1], good[2], addr),
                )
                conn.commit()
        except sqlite.Error as e:
            print(e)
            conn.rollback()
            return False
        return True

    def fetch_order(userName: str, Sql: str) -> (bool, list):
        conn = store.get_db_conn()
        try:
            cursor = conn.execute(Sql, (userName,))
            contents = cursor.fetchall()
            if contents is None:
                return False, []
            orderlist = []
            goodslist = []
            sameorderId = contents[0][0]
            for row in contents:
                if (sameorderId == row[0]):
                    samesellerName = row[1]
                    sameorderStatus = row[2]
                    sameaddr = row[6]
                    a = [row[3], row[4], row[5]]
                    goodslist.append(a)
                else:
                    b = [sameorderId, samesellerName, sameorderStatus, goodslist,sameaddr]
                    orderlist.append(b)
                    goodslist.clear()
                    sameorderId == row[0]
                    a = [row[3], row[4], row[5]]
                    goodslist.append(a)
        except sqlite.Error as e:
            logging.error(str(e))
            return False
        return True, orderlist

    def sellergetOrder(self, sellerName: str) -> (bool, list):
        Sql = "SELECT orderId, buyerName, orderStatus, goodsName, goodsPrice, totalValue, addr from orders where sellerName=?"
        return self.fetch_order(sellerName, Sql)

    def buyergetOrder(self, buyerName: str) -> (bool, list):
        Sql =  "SELECT orderId, sellerName, orderStatus, goodsName, goodsPrice, totalValue, addr from orders where buyerName=?"
        return self.fetch_order(buyerName, Sql)

    def cancelOrder(orderId: str, buyerName: str) -> bool:
        conn = store.get_db_conn()
        try:
            cursor = conn.execute("DELETE from orders where buyerName=? and orderId=?", (buyerName, orderId))
            if cursor.rowcount == 1:
                conn.commit()
            else:
                conn.rollback()
                return False
        except sqlite.Error as e:
            logging.error(str(e))
            conn.rollback()
        return True

    def paymentOrder(orderId: str, buyerName: str) -> bool:
        conn = store.get_db_conn()
        try:
            cursor = conn.execute(
                "SELECT balance from user where buyerName=?",
                (buyerName,),
            )
            row = cursor.fetchone()
            balance = row[0]
            cursor = conn.execute(
                "SELECT totalValue from order where orderId=?",
                (orderId,),
            )
            row = cursor.fetchone()
            money = balance-row[0]
            if money < 0:
                return False
            conn.execute(
                "UPDATE order set orderStatus = ? where orderId = ?",
                (3,),
            )
            conn.execute(
                "UPDATE user set balance = ? where buyerName = ?",
                (money,),
            )
            conn.commit()
        except sqlite.Error as e:
            logging.error(str(e))
            conn.rollback()
