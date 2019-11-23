## 1）createOrder-创建订单

#### URL
POST http://$address$/order/createOrder

#### Request

Headers:

| key   | 类型   | 描述               | 是否为空 |
| ----- | ------ | ------------------ | -------- |
| token | string | 登录产生的会话标识 | N        |

Body:
```
{
	"orderId":"$order id",
	"buyerName":"$buyer name",
	"sellerName":"$seller name",
	"orderStatue":"$order status",
	"goodsidlist":"$goods id list"
	"addr":"$addr"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
orderId | stirng | 订单号 | N 
buyerName | string | 买家名 | N
sellerName | string | 卖家名 | N 
orderStatus | int | 订单状态   <br />eg：0交易失败 1交易成功 2待支付 3支付成功 | N 
goodsidlist | list | 所有购买的商品的编号 | N 
 addr        | string | 收货地址                                                   | N          

#### Response

Status Code:

码 | 描述| 
--- | ---|--- 
200 | 订单生成成功 | 
401 | 订单生成失败，token错误 | 
501 | 订单生成失败，商品暂无 | 

Body:
```
{
    "message":"$order generation failed，token error/$order generation failed，no goods/$ok"
}
```
变量名 | 类型 | 描述 | 是否可为空| 
---|---|---|---|---
 message | string | 失败时，为错误信息描述；成功时，为"ok" | N         | 



## 2）cancelOrder-取消订单

#### URL：

POST http://$address$/order/cancelOrder

#### Request

Headers:

| key   | 类型   | 描述               | 是否为空 |
| ----- | ------ | ------------------ | -------- |
| token | string | 登录产生的会话标识 | N        |

Body:

```
{
    “orderId":"$order number",
    "buyerName":"$buyer name"
}
```

| 变量名    | 类型   | 描述   | 是否可为空 |
| --------- | ------ | ------ | ---------- |
| orderId   | string | 订单号 | N          |
| buyerName | string | 买家名 | N          |

#### Response

Status Code:

| 码   | 描述                 |
| ---- | -------------------- |
| 200  | 取消成功             |
| 401  | 取消失败，token错误  |
| 513  | 取消失败，订单不存在 |

Body:

```
{
	"message":"$cancel failed, token error/$cancel failed, no order/$ok"
}
```

| 变量名  | 类型   | 描述                                  | 是否可为空 |
| ------- | ------ | ------------------------------------- | ---------- |
| message | string | 失败时，为错误信息描述；成功时，为“ok | N          |



## 3）buyergetOrder-买家查看全部订单

#### URL：

POST http://$address$/order/buyergetOrder

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
| 200  | 查询成功            |
| 401  | 查询失败，token错误 |
| 514  | 查询失败，暂无订单  |

Body:

```
{
	"message":"$Inquiry failed, token error/$Inquiry failed, no order/$ok",
	"orderlist":[{"orderId":"$order number",
    			 "sellerName":"$seller name",
    			 "orderStatus":"order status",
    			 "addr":"address"，
    			 "totalValue":"$totalValue"，
    			 "buylist":[{"goodsName":"$goods name",
						    "goodsPrice":"$goods price",
						    "goodsNum":"$goods number"},{......}]},
				  {......}]	  	
}
```

| 变量名        | 类型   | 描述                                                         | 是否可为空 |
| ------------- | ------ | ------------------------------------------------------------ | ---------- |
| errormsg      | string | 失败时，为错误信息描述，且以下变量不输出；<br />成功时，为"ok"，且输出以下变量 | Y          |
| **orderlist** |        | 用户的所有订单，且每单应该包含以下信息                       |            |
| orderId       | string | 订单号                                                       | N          |
| sellerName    | string | 卖家名                                                       | N          |
| orderStatus   | string | 订单状态，可以是：交易成功、待支付、交易失败                 | N          |
| addr          | string | 收货地址                                                     |            |
| totalValue    | string | 总价                                                         | N          |
| **buylist**   |        | 订单中的每个商品都应包含以下信息                             |            |
| goodsName     | string | 商品名                                                       | N          |
| goodsPrice    | string | 商品价格                                                     | N          |
| goodsNum      | string | 商品数量                                                     | N          |

#### 接口描述

a."orderlist"表示一个用户可能拥有多个订单；

b.单个订单可能包含多个商品，即"buylist"展示在同一个订单中的商品信息。



## 4）sellergetOrder-卖家查看全部订单

#### URL：

POST http://$address$/order/sellergetOrder

#### Request

Headers:

| key   | 类型   | 描述               | 是否为空 |
| ----- | ------ | ------------------ | -------- |
| token | string | 登录产生的会话标识 | N        |

Body:

```
{
    "sellerName":"$seller name"
}
```

| 变量名     | 类型   | 描述   | 是否可为空 |
| ---------- | ------ | ------ | ---------- |
| sellerName | string | 卖家名 | N          |

#### Response

Status Code:

| 码   | 描述                |
| ---- | ------------------- |
| 200  | 查询成功            |
| 401  | 查询失败，token错误 |
| 501  | 查询失败，暂无订单  |

Body:

```
{
	"message":"$Inquiry failed, token error/$Inquiry failed, no order/$ok",
	"orderlist":[{"orderId":"$order number",
    			 "buyerName":"$buyer name",
    			 "orderStatus":"$order status",
    			 "addr":"$address",
    			 "totalValue":"$totalValue"，
    			 "buylist":[{"goodsName":"$goods name",
				             "goodsPrice":"$goods price",
						    "goodsNum":"$goods number"},{......}]},
				  {......}]	  	
}
```

| 变量名        | 类型   | 描述                                                         | 是否可为空 |
| ------------- | ------ | ------------------------------------------------------------ | ---------- |
| errormsg      | string | 失败时，为错误信息描述，且以下变量不输出；<br />成功时，为"ok"，且输出以下变量 | Y          |
| **orderlist** |        | 用户的所有订单，且每单应该包含以下信息                       |            |
| orderId       | string | 订单号                                                       | N          |
| buyerName     | string | 买家名                                                       |            |
| orderStatus   | string | 订单状态，可以是：交易成功、待支付、交易失败                 | N          |
| addr          | string | 收货地址                                                     |            |
| totalValue    | string | 总价                                                         | N          |
| **buylist**   |        | 每个用户订单中的每个商品都应包含以下信息                     |            |
| goodsName     | string | 商品名                                                       | N          |
| goodsPrice    | string | 商品价格                                                     | N          |
| goodsNum      | string | 商品数量                                                     | N          |



## 5）paymentOrder-订单支付

#### URL：

POST http://$address$/order/paymentOrder

#### Request

Headers:

| key   | 类型   | 描述      |
| ----- | ------ | --------- |
| token | string | 访问token |

Body:

```
{
    “orderId":"$order number"，
    "buyerName":"$buyer name"
}
```

| 变量名    | 类型   | 描述   | 是否可为空 |
| --------- | ------ | ------ | ---------- |
| orderId   | string | 订单号 | N          |
| buyerName | string | 买家名 | N          |

#### Response

Status Code:

| 码   | 描述                   |      |
| ---- | ---------------------- | ---- |
| 200  | 支付成功               |      |
| 401  | 支付失败，token错误    |      |
| 515  | 支付失败，账户余额不足 |      |
| 516  | 支付失败，商品库存不足 |      |

Body:

```
{
	"message":"$payment failed, token error/$payment failed, insufficient account balance/$payment failed, insufficient goods/$ok"
}
```

| 变量名  | 类型   | 描述                                  | 是否可为空 |
| ------- | ------ | ------------------------------------- | ---------- |
| message | string | 失败时，为错误信息描述；成功时，为“ok | N          |

#### 接口描述

需要考虑到这些情况：a.账户余额不足；b.商品库存不足；

在支付成功之后，需要：买家余额减少；卖家余额增加；商品库存减少；订单状态更新。

