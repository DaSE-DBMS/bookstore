import requests
from urllib.parse import urljoin


class Auth:
    def __init__(self, url_prefix):
        self.url_prefix = urljoin(url_prefix, "auth/")

    def login(self, username: str, password: str, terminal: str) -> (bool, str):
        json = {"username": username, "password": password, "terminal": terminal}
        url = urljoin(self.url_prefix, "login")
        r = requests.post(url, json=json)
        if r.status_code == 200:
            token = r.json()["token"]
            return True, token
        else:
            return False, ""

    def register(self, username: str, password: str) -> bool:
        json = {"username": username, "password": password}
        url = urljoin(self.url_prefix, "register")
        r = requests.post(url, json=json)
        return r.status_code == 200

    def password(self, username: str, old_password: str, new_password: str) -> bool:
        json = {
            "username": username,
            "oldPassword": old_password,
            "newPassword": new_password,
        }
        url = urljoin(self.url_prefix, "password")
        r = requests.post(url, json=json)
        return r.status_code == 200

    def logout(self, username: str, token: str) -> bool:
        json = {"username": username}
        headers = {"token": token}
        url = urljoin(self.url_prefix, "logout")
        r = requests.post(url, headers=headers, json=json)
        return r.status_code == 200

    def unregister(self, username: str, password: str) -> bool:
        json = {"username": username, "password": password}
        url = urljoin(self.url_prefix, "unregister")
        r = requests.post(url, json=json)
        return r.status_code == 200
