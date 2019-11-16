import requests
from urllib.parse import urljoin

class seller:
    def __init__(self, url_prefix):
        self.url_prefix = urljoin(url_prefix, "goods/")

    def addGoods(self, goodsId, goodsName, goodsauth, goodsPrice, goodsNum, goodsDsr) -> bool:
        json = {"goodsId": goodsId,"goodsName" : goodsName,"goodsauth": goodsauth,"goodsPrice" : goodsPrice,"goodsNum" : goodsNum,"goodsDsr": goodsDsr}
        #headers = {"token": token}
        url = urljoin(self.url_prefix, "addGoods")
        r = requests.post(url, json=json)
        return r.status_code == 200

    def getMemberInfo(self, username: str, token: str) -> (str, str, str):
        json = {"username": username}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "getMemberInfo")
        r = requests.get(url, headers=headers, json=json)
        if r.status_code == 200:
            return r.json()["name"], r.json()["sex"], r.json()["tele"]
        else:
            return "", "", ""

    def editMemberInfo(self, username: str, token: str) -> bool:
        json = {"username": username}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "editMemberInfo")
        r = requests.post(url, headers=headers, json=json)
        return r.status_code == 200

    # 1.editItem-编辑卖家商品接口
    def editItem(self, username: str, token: str) -> bool:
        json = {"username": username}
        # headers = {"token": token}
        url = urljoin(self.url_prefix, "editItem")
        r = requests.post(url, json=json)
        return r.status_code == 200

    def getSoldItem(self, username: str, token: str) -> (str, str, str, str, str):
        json = {"username": username}
        headers = {"token": token}
        url = urljoin(self.url_prefix,"getSoldItem")
        r = requests.get(url, headers=headers, json=json)
        if r.status_code == 200:
            return r.json()["orderId"], r.json()["orderDate"], r.json()["orderStatus"], r.json()["productName"], r.json()["productPrice"]
        else:
            return "", "", "", "", ""

    def getRefundItemOrder(self, username: str, token: str) -> (str, str, str):
        json = {"username": username}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "getRefundItemOrder")
        r = requests.get(url, headers=headers, json=json)
        if r.status_code == 200:
            return r.json()["orderId"], r.json()["productName"], r.json()["productPrice"]
        else:
            return "", "", ""

    # 2.sellerRefundGoods-查询卖家退货物流信息接口
    def sellerRefundGoods(self, username: str, token: str, orderId: str) -> (str, str, str):
        json = {"username": username, "orderId": orderId}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "sellerRefundGoods")
        r = requests.get(url, headers=headers, json=json)
        if r.status_code == 200:
            return r.json()["orderId"], r.json()["productName"], r.json()["address"]
        else:
            return ""
