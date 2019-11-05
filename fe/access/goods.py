import requests
from urllib.parse import urljoin


class Goods:
    def __init__(self, url_prefix):
        self.url_prefix = urljoin(url_prefix, "goods/")

    def getmerchantgoods(self, merchantname: str) -> (bool):
        json = {"merchantname": merchantname}
        url = urljoin(self.url_prefix, "getmerchantgoods")
        r = requests.post(url, json=json)
        if r.status_code == 200:
            goodsinfo = r.json()["goodstuple"]
            return True, goodsinfo
        else:
            return False, ""

    def getgoods(self, goodsname: str) -> (bool):
        json = {"goodsname": goodsname}
        url = urljoin(self.url_prefix, "getgoods")
        r = requests.post(url, json=json)
        if r.status_code == 200:
            goodsinfo = r.json()["goodstuple"]
            return True, goodsinfo
        else:
            return False, ""

    def getgoodsdetails(self, merchantname: str, goodsname: str) -> (bool):
        json = {"merchantname": merchantname, "goodsname": goodsname}
        url = urljoin(self.url_prefix, "getgoodsdetails")
        r = requests.post(url, json=json)
        if r.status_code == 200:
            goodsinfo = r.json()["goodstuple"]
            return True, goodsinfo
        else:
            return False, ""

    def getcategory(self, category: str) -> (bool):
        json = {"category": category}
        url = urljoin(self.url_prefix, "getcategory")
        r = requests.post(url, json=json)
        if r.status_code == 200:
            goodsinfo = r.json()["goodstuple"]
            return True, goodsinfo
        else:
            return False, ""

    def getmerhantinfo(self, goodsname: str) -> (bool):
        json ={"goodsname": goodsname}
        url = urljoin(self.url_prefix, "getmerchantinfo")
        r = requests.post(url, json=json)
        if r.status_code == 200:
            merchantinfo = r.json()["merchanttuple"]
            return True, merchantinfo
        else:
            return False, ""

