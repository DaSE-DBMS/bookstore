import requests
from urllib.parse import urljoin
from fe.access import book
import simplejson


class Seller:
    def __init__(self, url_prefix, seller_id: str, password: str):
        self.url_prefix = urljoin(url_prefix, "seller/")
        self.seller_id = seller_id
        self.password = password

    def create_store(self, store_id):
        json = {
            "seller_id": self.seller_id,
            "store_id": store_id,
        }
        #print(simplejson.dumps(json))
        url = urljoin(self.url_prefix, "create_store")
        r = requests.post(url, json=json)
        return r.status_code

    def add_book(self, seller_id: str, store_id: str, stock_level: int, book_info: book.Book) -> int:
        json = {
            "seller_id": seller_id,
            "store_id": store_id,
            "book_info": book_info.__dict__,
            "stock_level": stock_level
        }
        #print(simplejson.dumps(json))
        url = urljoin(self.url_prefix, "add_book")
        r = requests.post(url, json=json)
        return r.status_code

    def add_stock_level(self, seller_id: str, store_id: str, book_id: str, add_stock_num: int) -> int:
        json = {
            "seller_id": seller_id,
            "store_id": store_id,
            "book_id": book_id,
            "add_stock_level": add_stock_num
        }
        print(simplejson.dumps(json))
        url = urljoin(self.url_prefix, "add_stock_level")
        r = requests.post(url, json=json)
        return r.status_code
