

class Cart:
    username: str
    goodsId: str
    goodsName: str
    goodsPrice: str
    goodsNum: str
    totalValue: str

    def __init__(self, goodsId, goodsName, goodsPrice, goodsNum):
        self.key = goodsId
        self.goodsName = goodsName
        self.goodsPrice = goodsPrice
        self.goodsNum = goodsNum
