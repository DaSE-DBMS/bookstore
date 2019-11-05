import requests
from urllib.parse import urljoin


class Order:
    def __init__(self, url_prefix):
        self.url_prefix = urljoin(url_prefix, "order/")

    def getcart(self, username: str, token: str) -> (bool):
        json = {"username": username}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "getcart/")
        r = requests.post(url, headers=headers, json=json)
        return r.status_code == 200

    def delcart(self, username: str, goodsname: str, token: str) -> (bool):
        json = {"username": username, "goodsname": goodsname}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "delcart/")
        r = requests.post(url, headers=headers, json=json)
        return  r.status_code == 200

    def addcart(self, username: str, merchantname: str, goodsname: str, token: str) -> (bool):
        json = {"username": username, "merchantname": merchantname, "goodsname": goodsname}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "addcart/")
        r = requests.post(url, headers=headers, json=json)
        return r.status_code == 200

    def createorder(self, username: str, goodsset: set, token: str) -> (bool):
        json = {"username": username, "goodsset": goodsset}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "createorder/")
        r = requests.post(url, headers=headers, json=json)
        if r.status_code == 200:
            orderinfo = r.json()["orderinfo"]
            return True, orderinfo
        else:
            return False, ""

    def submitorder(self, username: str, orderid: int, token: str) -> (bool):
        json = {"username": username, "orderid": orderid}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "submitorder/")
        r = requests.post(url, headers=headers, json=json)
        if r.status_code == 200:
            orderinfo = r.json()["orderinfo"]
            return True, orderinfo
        else:
            return False, ""

    def cancelorder(self, username: str, orderid: int, token: str) -> (bool):
        json = {"username": username, "orderid": orderid}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "cancelorder/")
        r = requests.post(url, headers=headers, json=json)
        return  r.status_code == 200

    def paymentorder(self, username: str, orderid: int, balance: float, token: str) -> (bool):
        json = {"username": username, "orderid": orderid, "balance": balance}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "paymentorder/")
        r = requests.post(url, headers=headers, json=json)
        return  r.status_code == 200

    def allorder(self, username: str, token: str) -> (bool):
        json = {"username": username}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "allorder/")
        r = requests.post(url, headers=headers, json=json)
        if r.status_code == 200:
            orderinfo = r.json()["orderinfo"]
            return True, orderinfo
        else:
            return False, ""
