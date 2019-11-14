import requests
from urllib.parse import urljoin


class Goods:
    def __init__(self, url_prefix):
        self.url_prefix = urljoin(url_prefix, "goods/")

    def editGoods(self, username: str, goodsid: str, goodsName: str, goodsPrice: str, goodsNumber: str) -> bool:
        json = {"username": username, "goodsid": goodsid, "goodsName": goodsName, "goodsPrice": goodsPrice, "goodsNumber":goodsNumber}
        # headers = {"token": token}
        url = urljoin(self.url_prefix, "editGoods")
        r = requests.post(url, json=json)
        return r.status_code == 200

    def searchgoods(self, keywords: str, goodstypeid: str) -> (bool, list):
        json = {"keyeords": keywords, "goodsTypeId": goodstypeid}
        url = urljoin(self.url_prefix, "searchgoods/")
        r = requests.post(url, json=json)
        if r.status_code == 200:
            goodslist = r.json()["goodslist"]
            return True, goodslist
        else:
            return False, ""

    def getgoodsdetails(self, merchantid: str, goodsid: str, userid: str) -> (bool, list):
        json = {"merchantid": merchantid, "goodsid": goodsid, "userid": userid}
        url = urljoin(self.url_prefix, "getgoodsdetails/")
        r = requests.post(url, json=json)
        if r.status_code == 200:
            goodsname = r.json()["goodsname"]
            goodsauth = r.json()["goodsauth"]
            goodspub = r.json()["goodspub"]
            origprice = r.json()["origprice"]
            saleprice = r.json()["saleprice"]
            goodsdes = r.json()["goodsdes"]
            iscollect = r.json()["iscollect"]
            merchantname = r.json()["merchantname"]
            goodsdetailslist = [goodsname, goodsauth, goodspub, origprice, saleprice, goodsdes, iscollect,  merchantname]
            return True, goodsdetailslist
        else:
            return False, ""

    def getmerhantinfo(self, merchantid: str, goodsid: str) -> (bool, list):
        json ={"merchantid": merchantid, "goodsid":goodsid}
        url = urljoin(self.url_prefix, "getmerchantinfo/")
        r = requests.post(url, json=json)
        if r.status_code == 200:
            merchantname = r.json()["merchantname"]
            merchantloc = r.json()["merchantloc"]
            merchantRank = r.json()["merchantRank"]
            goodslist = r.json()["goodslist"]
            merchantinfo = [merchantname, merchantloc, merchantRank, goodslist]
            return True, merchantinfo
        else:
            return False, ""

