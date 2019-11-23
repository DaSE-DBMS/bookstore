## 1）addCart-添加商品到购物车

#### URL

POST http://$address$/order/addCart

#### Request

Headers:

| key   | 类型   | 描述               | 是否为空 |
| ----- | ------ | ------------------ | -------- |
| token | string | 登录产生的会话标识 | N        |

Body:

```
{
    "buyerName":"$buyer name",
    "sellerName":"$sellerr name",
    “goodsId":"$goods id",
	"goodsName":"$goods name",
	"goodsPrice":"$sale price",
	"goodsNum":"$goods number",
	"totalValue":"$total value" 
}
```

| 变量名     | 类型   | 描述     | 是否可为空 |
| ---------- | ------ | -------- | ---------- |
| buyerName  | string | 买家名   | N          |
| sellerName | string | 卖家名   | N          |
| goodsId    | string | 商品编号 | N          |
| goodsName  | string | 商品名   | N          |
| goodsPrice | string | 商品价格 | N          |
| goodsNum   | string | 商品数量 | N          |
| totalValue | string | 总价     | N          |

#### Response

Status Code:

| 码   | 描述                   |      |
| ---- | ---------------------- | ---- |
| 200  | 添加成功               |      |
| 401  | 添加失败，token错误    |      |
| 514  | 添加失败，商品库存不足 |      |

Body:

```
{
	"message":"$Insert failed, insufficient stock of goods/$Insert failed, token error/$ok"
}
```

| 变量名  | 类型   | 描述                                   | 是否可为空 |
| ------- | ------ | -------------------------------------- | ---------- |
| message | string | 失败时，为错误信息描述；成功时，为"ok" | Y          |

#### 接口描述

a.首先判断商品是否还有库存；

b.其次判断商品是否已在购物车中，存在则修改商品数量；如果不存在，则添加商品全部信息到购物车中。



## 2）delCart-删除购物车中的商品

#### URL

POST http://$address$/order/delCart

#### Request

Headers:

| key   | 类型   | 描述               | 是否为空 |
| ----- | ------ | ------------------ | -------- |
| token | string | 登录产生的会话标识 | N        |

Body:

```
{
	"buyerName":"$buyer name",
    "goodsId":"$good id",
    "goodsNum":"$goods number"
}
```

| 变量名    | 类型   | 描述     | 是否可为空 |
| --------- | ------ | -------- | ---------- |
| buyerName | string | 买家名   | N          |
| goodsId   | string | 商品编号 | N          |
| goodsNum  | string | 商品数量 | N          |

#### Response

Status Code:

| 码   | 描述                 |
| ---- | -------------------- |
| 200  | 删除成功             |
| 401  | 删除失败，token错误  |
| 513  | 删除失败，商品不存在 |

Body:

```
{
	"message":"$Delete failed, token error/$ok"
}
```

| 变量名  | 类型   | 描述                                   | 是否可为空 |
| ------- | ------ | -------------------------------------- | ---------- |
| message | string | 失败时，为错误信息描述；成功时，为"ok" | N          |

#### 接口描述

某一商品在购物车中可能数量大于一，因此删除的时候要传入需要删除的数量



## 3）getCart-查看购物车

#### URL

POST http://$address$/order/getCart

#### Request

Headers:

| key   | 类型   | 描述               | 是否为空 |
| ----- | ------ | ------------------ | -------- |
| token | string | 登录产生的会话标识 | N        |

Body:

```
{
    "buyerName":"$buyer name"
}
```

| 变量名    | 类型   | 描述   | 是否可为空 |
| --------- | ------ | ------ | ---------- |
| buyerName | string | 买家名 | N          |

#### Response

Status Code:

| 码   | 描述                |
| ---- | ------------------- |
| 200  | 访问成功            |
| 401  | 访问失败，token错误 |

body：

```
{ 
	"message":"$Access failed, token error/$ok",
	"sum":"$total value",
	"cartlist":[{"sellerName":"$seller name",
				"goodsName":"$goods name",
				"goodsPrice":"$sale price",
				"goodsNum":"$goods number"},{......}]
}
```

| 变量名       | 类型   | 描述                                                         | 是否可为空 |
| ------------ | ------ | ------------------------------------------------------------ | ---------- |
| message      | string | 失败时，为错误信息描述，且以下变量不输出；<br />成功时，为"ok"，且输出以下变量 | N          |
| sum          | string | 总金额                                                       | N          |
| **cartlist** |        | 购物车中的所有商品，且每件商品都应包含如下信息               |            |
| sellerName   | string | 卖家名                                                       |            |
| goodsName    | string | 商品名                                                       | N          |
| goodsNum     | string | 商品数量                                                     | N          |
| goodsPrice   | string | 商品价格                                                     | N          |





