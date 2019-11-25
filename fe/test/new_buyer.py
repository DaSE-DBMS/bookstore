from fe import conf
from fe.access import buyer, auth


def register_new_buyer(user_id) -> buyer.Buyer:
    a = auth.Auth(conf.URL)
    password = user_id
    code = a.register(user_id, password, is_buyer=True, is_seller=True)
    assert code == 200
    s = buyer.Buyer(conf.URL, user_id, password)
    return s
