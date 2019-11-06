import requests
from urllib.parse import urljoin

class Buyer:
    def __init__(self, url_prefix):
        self.url_prefix = urljoin(url_prefix, "buyer/")

    def getMemberInfo(self,username : str,token: str)->(str,str,str):
        json = {"username": username}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "getMemberInfo")
        r = requests.post(url, headers=headers, json=json)
        if r.status_code == 200:
            return r.json()["name"],r.json()["sex"],r.json()["tele"]
        else:
            return "","",""

    def editMemberInfo(self):
        json = {}
        url = urljoin()
        r = requests.post(url, json=json)

    def getMemberOrder(self):
        json = {}
        url = urljoin()
        r = requests.post(url, json=json)

    def getRefundOrder(self):
        json = {}
        url = urljoin()
        r = requests.post(url, json=json)

    def returnDetailOrder(self):
        json = {}
        url = urljoin()
        r = requests.post(url, json=json)

    def refundsGoods(self):
        json = {}
        url = urljoin()
        r = requests.post(url, json=json)

    def getMemberConsignee(self):
        json = {}
        url = urljoin()
        r = requests.post(url, json=json)

    def editConsignee(self):
        json = {}
        url = urljoin()
        r = requests.post(url, json=json)
