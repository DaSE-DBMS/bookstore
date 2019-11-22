import requests
from urllib.parse import urljoin


class Cart:
    def __init__(self, url_prefix):
        self.url_prefix = urljoin(url_prefix, "cart/")

    def addCart(self, buyerName: str,sellerName: str, goodsId: str, goodsName: str, goodsPrice: str, goodsNum: str, totalValue: str) -> bool:
        json = {"buyerName": buyerName,"sellerName": sellerName,"goodsId": goodsId,"goodsName": goodsName,"goodsPrice": goodsPrice,"goodsNum": goodsNum,"totalValue": totalValue}
        url = urljoin(self.url_prefix, "addCart")
        r = requests.post(url, json=json)
        print(r.json()["message"])
        return r.status_code == 200

    def delCart(self, sellerName: str, goodsId: str, goodsNum: str) -> bool:
        json = {"sellerName": sellerName,"goodsId" : goodsId,"goodsNum": goodsNum}
        url = urljoin(self.url_prefix, "delCart")
        r = requests.post(url, json=json)
        print(r.json()["message"])
        return r.status_code == 200

    def getCart(self, buyerName: str) -> (bool, list,float):
        json = {"buyerName": buyerName}
        url = urljoin(self.url_prefix, "getCart")
        r = requests.post(url, json=json)
        print(r.json()["message"])
        if r.status_code == 200:
            cartlist = r.json()["cartlist"]
            sum = r.json(["sum"])
            print(cartlist)
            return True, cartlist, sum
        else:
            return False, [], 0
