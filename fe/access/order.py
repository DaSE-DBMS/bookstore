import requests
from urllib.parse import urljoin


class Order:
    def __init__(self, url_prefix):
        self.url_prefix = urljoin(url_prefix, "order/")

    def getOrder(self, username: str, token: str) -> (bool, list):
        json = {"username": username}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "getOrder")
        r = requests.get(url, headers=headers, json=json)
        if r.status_code == 200:
            return True, r.json()["orderlist"]
        else:
            return False, ""

    def getcart(self, userid: str, token: str) -> (bool, list):
        json = {"userid": userid}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "getcart/")
        r = requests.post(url, headers=headers, json=json)
        if r.status_code == 200:
            goodssum = r.json()["goodssum"]
            goodsamount = r.json()["goodsamount"]
            itemlist = r.json()["litemlist"]
            cartinfo = [goodssum, goodsamount, itemlist]
            return True, cartinfo
        else:
            return False, ""

    def delcart(self, userid: str, cartitemid: str, token: str) -> (bool):
        json = {"userid": userid, "cartitemid": cartitemid}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "delcart/")
        r = requests.post(url, headers=headers, json=json)
        return r.status_code == 200

    def addcart(self, userid: str, merchantid: str, goodsid: str, token: str) -> (bool):
        json = {"userid": userid, "merchantid": merchantid, "goodsname": goodsid}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "addcart/")
        r = requests.post(url, headers=headers, json=json)
        return r.status_code == 200

    def createorder(self, userid: str, goodssum: str, goodsamount: str, buylist: list, token: str) -> (bool, str):
        json = {"userid": userid, "goodssum": goodssum, "goodsamount": goodsamount, "buylist": buylist}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "createorder/")
        r = requests.post(url, headers=headers, json=json)
        if r.status_code == 200:
            orderno = r.json()["orderno"]
            return True, orderno
        else:
            return False, ""

    def cancelorder(self, orderno: str, token: str) -> (bool):
        json = {"orderno": orderno}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "cancelorder/")
        r = requests.post(url, headers=headers, json=json)
        return  r.status_code == 200

    def paymentorder(self, userid: str, orderno: str, token: str) -> (bool):
        json = {"userid": userid, "orderno": orderno}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "paymentorder/")
        r = requests.post(url, headers=headers, json=json)
        return  r.status_code == 200

    def allorder(self, userid: str, token: str) -> (bool, list):
        json = {"userid": userid}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "allorder/")
        r = requests.post(url, headers=headers, json=json)
        if r.status_code == 200:
            orderlist = r.json()["orderlist"]
            return True, orderlist
        else:
            return False, ""


