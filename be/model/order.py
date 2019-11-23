from itertools import product

from be.model import store
import sqlite3 as sqlite
import logging
from be.model import cart

from be.model.cart import check_num


class Order:
    orderId: str
    buyerName: str
    sellerName: str
    orderStatus: int  #0交易失败 1交易成功 2待支付 3支付成功
    goodsId: str
    goodsName: str
    goodsPrice: int
    goodsNum: int
    totalValue: int
    addr: str

    def __init__(self):
        self.orderId = ""
        self.buyerName = ""
        self.sellerName = ""
        self.orderStatus = 2
        self.goodsId = ""
        self.goodsName = ""
        self.goodsPrice = 0
        self.goodsNum = 0
        self.totalValue = 0
        self.addr = ""

    #注意这里传进来goodsidlist，是一个goodId的列表
    def createOrder(orderId, buyerName, sellerName, orderStatus, goodsidlist, addr) -> (bool):
        conn = store.get_db_conn()
        try:
            for i in goodsidlist:
                # 添加一个判断，商品是否还有库存,先到购物车表查看要买的商品的数量
                cursor = conn.execute(
                    "SELECT goodsNum from cart where goodsId=?",
                    (i,),
                )
                row = cursor.fetchone()
                #再看商品表是否有库存
                if not check_num(i, row[0]):
                    return False
                    #这里需要输出商品商品good[0]库存不够
            #进入到这个循环说明库存是够的，所以开始生成订单
            totalValue = 0
            for i in goodsidlist:
                cursor = conn.execute(
                    "SELECT goodsName, goodsPrice, goodsNum, totalValue from cart where goodsId=?",
                    (i,),
                )
                row = cursor.fetchone()
                totalValue += row[3]
                conn.execute(
                    "INSERT into orders(orderId, buyerName, sellerName, orderStatus, goodsId, goodsName, goodsPrice, goodsNum, addr) VALUES (?, ?, ?, ?, ?, ?, ?, ? ,?);",
                    (orderId, buyerName, sellerName, orderStatus, i, row[0], row[1], row[2], addr),
                )
                cursor = conn.execute("DELETE from goods where goodsId=?", (i,))
                if cursor.rowcount == 1:
                    conn.commit()
                else:
                    conn.rollback()
                    return False
            conn.execute(
                "UPDATE orders set totalValue = ? where orderId = ?",
                (totalValue, orderId),
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
            if not len(contents):
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
        b = [sameorderId, samesellerName, sameorderStatus, goodslist, sameaddr]
        orderlist.append(b)
        return True, orderlist

    def sellergetOrder(self, sellerName: str) -> (bool, list):
        Sql = "SELECT orderId, buyerName, orderStatus, goodsName, goodsPrice, totalValue, addr from orders where sellerName=?"
        return self.fetch_order(sellerName, Sql)

    def buyergetOrder(self, buyerName: str) -> (bool, list):
        Sql = "SELECT orderId, sellerName, orderStatus, goodsName, goodsPrice, totalValue, addr from orders where buyerName=?"
        return self.fetch_order(buyerName, Sql)

    def cancelOrder(orderId: str, buyerName: str) -> bool:
        conn = store.get_db_conn()
        try:
            cursor = conn.execute("DELETE from orders where buyerName=? and orderId=?", (buyerName, orderId))
            if cursor.rowcount:
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
            # 得到账户余额
            cursor = conn.execute(
                "SELECT balance from user where username=?",
                (buyerName,),
            )
            row1 = cursor.fetchone()
            buyerbalance = row1[0]
            # 应付金额
            cursor = conn.execute(
                "SELECT totalValue from orders where orderId=?",
                (orderId,),
            )
            row2 = cursor.fetchone()
            money = buyerbalance - row2[0]
            #表示买家钱不够
            if money < 0:
                return False

            #进入一下表示买家的财力是可以购买订单上的商品的，因此开始：查看库存->修改库存->修改订单状态->减少买家账户余额->增加卖家账户余额
            #库存是否足够
            cursor = conn.execute(
                "SELECT goodsId from orders where orderId=?",
                (orderId,),
            )
            goodsIdlist = cursor.fetchall()
            buygoodsnumlist = []
            for i in goodsIdlist:
                cursor = conn.execute(
                    "SELECT goodsNum from cart where goodsId=? and buyerName=?",
                    (i, buyerName),
                )
                row = cursor.fetchone()
                buygoodsnumlist.append(row[0])
                #再看商品表是否有库存
                if not check_num(i, row[0]):
                    return False
                    #这里需要输出商品库存不够
            #进入到这个循环说明库存是够的，所以开始修改库存
            for i, j in product(goodsIdlist, buygoodsnumlist):
                cursor = conn.execute(
                    "SELECT goodsNum from goods where goodsId=?",
                    (i,),
                )
                oldgoodsnum = cursor.fetchone()
                cursor = conn.execute("UPDATE goods set goodsNum = ? where goodsId = ?", (oldgoodsnum[0]-j, i))
                if cursor.rowcount:
                    conn.commit()
                else:
                    conn.rollback()
                    return False
            #修改订单状态，“3”表示支付成功
            conn.execute(
                "UPDATE orders set orderStatus = ? where orderId = ?",
                (3,orderId,),
            )
            #修改买家账户余额
            conn.execute(
                "UPDATE user set balance = ? where username = ?",
                (money,buyerName),
            )
            #修改卖家账户余额
            cursor = conn.execute(
                "SELECT sellerName,totalValue from orders where orderId=?",
                (orderId,),
            )
            row3 = cursor.fetchone()
            sellerName = row3[0]
            sellerbalance = row3[1]
            cursor = conn.execute(
                "SELECT balance from user where username=?",
                (sellerName,),
            )
            oldsellerbalance = cursor.fetchone()
            conn.execute(
                "UPDATE user set balance = ? where username = ?",
                (oldsellerbalance + sellerbalance, sellerName),
            )
            conn.commit()
        except sqlite.Error as e:
            logging.error(str(e))
            conn.rollback()
