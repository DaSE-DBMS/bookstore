from be.model import store
import sqlite3 as sqlite
import logging


class Order:
    orderId: str
    buyername: str
    sellerName: str
    orderStatus: str #0失败 1成功 2待支付 3支付成功
    goodsName: str
    goodsPrice: str
    totalValue: str
    addr: str

    def __init__(self, orderId, buyername, sellerName, orderStatus, goodsName, goodsPrice, totalValue, addr):
        self.orderId = orderId
        self.buyername = buyername
        self.sellerName = sellerName
        self.orderStatus = orderStatus
        self.goodsName = goodsName
        self.goodsPrice = goodsPrice
        self.totalValue = totalValue
        self.addr = addr

    def fetch_order(name: str, Sql: str) -> (bool, list):
        conn = store.get_db_conn()
        try:
            cursor = conn.execute(
                Sql,(name),
            )
            contents = cursor.fetchall()
            if contents is None:
                return False, []
            orderlist = []
            for row in contents:
                a = [row[0], row[1], row[2], row[3], row[4], row[5]]
                orderlist.append(a)
        except sqlite.Error as e:
            logging.error(str(e))
            return False
        return True, orderlist

    #注意这里传进来carlist是很多商品信息，包括goodsName，goodsPrice，totalValue
    def createOrder(orderId, sellerName, buyerName, orderStatus, cartlist, addr):
        conn = store.get_db_conn()
        try:
            for good in cartlist:
                conn.execute(
                    "INSERT into orders(orderId, buyerName, sellerName , orderStatus, goodsName, goodsPrice, totalValue, addr) VALUES (?, ?, ?, ?, ?, ?, ? ,?);",
                    (orderId, buyerName ,sellerName , orderStatus, good[0], good[1], good[2], addr),
                )
                conn.commit()
        except sqlite.Error as e:
            print(e)
            conn.rollback()
            return False
        return True

    def buyergetOrder(self, buyerName: str, token: str) -> (bool, list):
        # if not self.check_token(token):
        #    return False,[]
        Sql = "SELECT orderId, sellerName, orderStatus, goodsName, goodsPrice, totalValue, addr from order where buyerName=?"
        return self.fetch_order(buyerName, Sql)

    def sellergetOrder(self, sellerName: str) -> (bool, list):
        Sql = "SELECT orderId, buyerName, orderStatus, goodsName, goodsPrice, totalValue, addr from order where sellerName=?"
        return self.fetch_order(sellerName, Sql)

    def cancelOrder(orderId: str, buyerName: str) -> bool:
        conn = store.get_db_conn()
        try:
            cursor = conn.execute("DELETE from order where buyerName=? and orderId=?", (buyerName, orderId))
            if cursor.rowcount == 1:
                conn.commit()
            else:
                conn.rollback()
        except sqlite.Error as e:
            logging.error(str(e))
            conn.rollback()

    def paymentOrder(orderId: str, buyerName: str) -> bool:
        conn = store.get_db_conn()
        try:
            cursor = conn.execute(
                "SELECT balance from user where buyerName=?",
                (buyerName,),
            )
            row = cursor.fetchone()
            balance = float(row[0])
            cursor = conn.execute(
                "SELECT totalValue from order where orderId=?",
                (orderId,),
            )
            row = cursor.fetchone()
            money = balance-float(row[0])
            if money < 0:
                return False
            conn.execute(
                "UPDATE order set orderStatus = ? where orderId = ?",
                ("3",),
            )
            conn.execute(
                "UPDATE user set balance = ? where buyerName = ?",
                (str(money),),
            )
            conn.commit()
        except sqlite.Error as e:
            logging.error(str(e))
            conn.rollback()
