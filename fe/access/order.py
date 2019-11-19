import requests
from urllib.parse import urljoin


class Order:
    def __init__(self, url_prefix):
        self.url_prefix = urljoin(url_prefix, "order/")

    def createOrder(self,orderId : str, sellerName : str, buyerName : str ,orderStatus : str, cartlist : list, addr : str) -> bool:
        json = { "orderId" : orderId,"sellerName" : sellerName, "buyerName" : buyerName , "orderStatus" : orderStatus ,"cartlist" : cartlist, "addr" : addr}
        url = urljoin(self.url_prefix, "createOrder")
        r = requests.post(url, json=json)
        if r.status_code == 200:
            return True
        else:
            return False


    def buyergetOrder(self, buyerName: str, token: str) -> (bool, list):
        json = {"buyerName": buyerName}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "buyergetOrder")
        r = requests.get(url, headers=headers, json=json)
        if r.status_code == 200:
            return True, r.json()["orderlist"]
        else:
            return False, ""

    def sellergetOrder(self, sellerName: str) -> (bool, list):
        json = {"sellerName": sellerName}
        url = urljoin(self.url_prefix, "sellergetOrder")
        r = requests.get(url, json=json)
        if r.status_code == 200:
            return True, r.json()["orderlist"]
        else:
            return False, ""

    def cancelOrder(self, orderno: str, token: str) -> (bool):
        json = {"orderno": orderno}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "cancelorder/")
        r = requests.post(url, headers=headers, json=json)
        return  r.status_code == 200

    def paymentOrder(self, orderId :str, buyerName: str) -> (bool):
        json = {"orderId": orderId, "buyerName": buyerName}
        url = urljoin(self.url_prefix, "paymentOrder/")
        r = requests.post(url, json=json)
        return  r.status_code == 200

