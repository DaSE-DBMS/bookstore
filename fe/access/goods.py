import requests
from urllib.parse import urljoin


class Goods:
    def __init__(self, url_prefix):
        self.url_prefix = urljoin(url_prefix, "goods/")

    def addGoods(self, goodsId: str, goodsName: str, goodsAuth: str, goodsPrice: str, goodsNum: str, goodsType: str, goodsDsr: str,sellerName: str) -> bool:
        json = {"goodsId": goodsId,"goodsName" : goodsName,"goodsAuth": goodsAuth,"goodsPrice": goodsPrice,"goodsNum": goodsNum,"goodsType": goodsType,"goodsDsr": goodsDsr,"sellerName": sellerName}
       # headers = {"token": token}
        url = urljoin(self.url_prefix, "addGoods")
        r = requests.post(url, json=json)
        print(r.json()["message"])
        return r.status_code == 200

    def delGoods(self, goodsId: str, sellerName: str) -> bool:
        json = {"goodsId": goodsId, "sellerName": sellerName}
       # headers = {"token": token}
        url = urljoin(self.url_prefix, "delGoods")
        r = requests.post(url, json=json)
        print(r.json()["message"])
        return r.status_code == 200

    def searchGoods(self, keywords: str, goodstype: str) -> (bool, list):
        json = {"keywords": keywords, "goodsType": goodstype}
        url = urljoin(self.url_prefix, "searchGoods")
        r = requests.get(url, json=json)
        print(r.json()["message"])
        if r.status_code == 200:
            goodslist = r.json()["goodslist"]
            print(goodslist)
            return True, goodslist
        else:
            return False, []


