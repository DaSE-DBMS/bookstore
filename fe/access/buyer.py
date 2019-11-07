import requests
from urllib.parse import urljoin

class Buyer:
    def __init__(self, url_prefix):
        self.url_prefix = urljoin(url_prefix, "buyer/")

    def getMemberInfo(self,username : str,token: str)->(str,str,str):
        json = {"username": username}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "getMemberInfo")
        r = requests.get(url, headers=headers, json=json)
        if r.status_code == 200:
            return r.json()["name"],r.json()["sex"],r.json()["tele"]
        else:
            return "","",""

    def editMemberInfo(self,username : str,token : str) ->(bool):
        json = {"username": username}
        headers = {"token": token}
        url = urljoin(self.url_prefix,"editMemberInfo")
        r = requests.post(url, headers = headers, json=json)
        return r.status_code == 200

    def getMemberOrder(self,username : str,token : str) ->(str,str,str,str,str):
        json = {"username": username}
        headers = {"token": token}
        url = urljoin(self.url_prefix,"getMemberOrder")
        r = requests.get(url, headers = headers,json=json)
        if r.status_code == 200:
            return r.json()["orderId"],r.json()["orderDate"],r.json()["orderStatus"],r.json()["productName"],r.json()["productPrice"]
        else:
            return "","","","",""

    def getRefundOrder(self,username : str,token : str)->(str,str,str):
        json = {"username": username}
        headers = {"token": token}
        url = urljoin(self.url_prefix,"getRefundOrder")
        r = requests.get(url, headers = headers,json=json)
        if r.status_code == 200:
            return r.json()["orderId"],r.json()["productName"],r.json()["productPrice"]
        else:
            return "","",""

    def getMemberConsignee(self,username : str,token : str)->(str):
        json = {"username": username}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "getMemberConsignee")
        r = requests.get(url, headers=headers, json=json)
        if r.status_code == 200:
            return r.json()["address"]
        else:
            return ""

    def editConsignee(self,username : str,token : str)->(bool):
        json = {"username": username}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "editConsignee")
        r = requests.post(url, headers=headers, json=json)
        return r.status_code == 200
