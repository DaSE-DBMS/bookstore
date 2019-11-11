from be.model import tuple
from typing import Dict
from os import path
import threading
from be.model import store
from flask import request
from be.model import user
from flask import jsonify
from be.model import user

class Order(tuple.Tuple):
    orderId: str
    username: str
    orderStatus: str
    goodsName: str
    goodsPrice: str

    def __init__(self, orderId, username, orderStatus, goodsName,goodsPrice):
        self.key = orderId
        self.username = username
        self.orderStatus = orderStatus
        self.goodsName = goodsName
        self.goodsPrice = goodsPrice

    def getOrder(self, username: str) -> (bool, list):
        if self.username == username:
            orderList = [self.orderId, self.orderStatus, self.goodsName, self.goodsPrice]
            return True, orderList
        return False, ""


def getOrder(username: str):
    o: Order = store.get_row(Order.__name__, username)
    if o is None:
        return False, ""
    else:
        return o.getOrder(username)



