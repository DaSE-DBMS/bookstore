from be.model import tuple
from typing import Dict
from os import path
import threading
from be.model import store
from flask import request
from flask import jsonify
from be.model import user
import sqlite3 as sqlite
import logging
import jwt
import time
from be.model.user import jwt_decode


class Order:
    orderId: str
    username: str
    orderStatus: str #0失败 1成功 2待支付
    goodsName: str
    goodsPrice: str
    totalValue: str

    def __init__(self, orderId, username, orderStatus, goodsName,goodsPrice):
        self.key = orderId
        self.username = username
        self.orderStatus = orderStatus
        self.goodsName = goodsName
        self.goodsPrice = goodsPrice


    def fetch_order(username) -> (bool, list):
        conn = store.get_db_conn()
        try:
            cursor = conn.execute(
                "SELECT orderId, orderStatus, goodsName, goodsPrice from order where username=?",
                (username),
            )
            contents = cursor.fetchall()
            if contents is None:
                return False, []
            orderlist = []
            for row in contents:
                a = [row[0], row[1], row[2], row[3]]
                orderlist.append(a)
        except sqlite.Error as e:
            logging.error(str(e))
            return False
        return True, orderlist


    def getOrder(self, username: str, token: str) -> (bool, list):
#        if not self.check_token(token):
 #           return False,[]
        return self.fetch_order(username)






