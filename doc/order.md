## 1）getCart-查看购物车

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

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
buyerName | string | 买家名 | N

#### Response

Status Code:


码 | 描述
--- | ---
200 | 访问成功 
401 | 访问失败，token错误 

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

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
 message | string | 失败时，为错误信息描述，且以下变量不输出；<br />成功时，为"ok"，且输出以下变量 | N         
 sum | string | 总金额 | N 
 **cartlist** |        | 购物车中的所有商品，且每件商品都应包含如下信息 |            
 sellerName | string | 卖家名 | 
 goodsName | string | 商品名 | N 
 goodsNum | string | 商品数量 | N 
 goodsPrice | string | 商品价格 | N 



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

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
buyerName | string | 买家名 | N 
 goodsId | string | 商品编号 | N          
 goodsNum | string | 商品数量 | N 

#### Response

Status Code:


码 | 描述
--- | ---
200 | 删除成功 
401 | 删除失败，token错误 


Body:
```
{
	"message":"$Delete failed, token error/$ok"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 失败时，为错误信息描述；成功时，为"ok" | N 

#### 接口描述

某一商品在购物车中可能数量大于一，因此删除的时候要传入需要删除的数量



## 3）addCart-添加商品到购物车

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

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
buyerName | string | 买家名 | N 
sellerName | string | 卖家名 | N
goodsId | string | 商品编号 | N
 goodsName   | string | 商品名   | N          
 goodsPrice | string | 商品价格 | N          
 goodsNum | string | 商品数量 | N          
 totalValue | string | 总价 | N          

#### Response

Status Code:

码 | 描述| 
--- | ---|--- 
200 | 添加成功 | 
401 | 添加失败，token错误 | 
501 | 添加失败，商品库存不足 | 

Body:
```
{
	"message":"$addition failed, insufficient stock of goods/$ok"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 失败时，为错误信息描述；成功时，为"ok" | Y 

#### 接口描述

a.首先判断商品是否还有库存；

b.其次判断商品是否已在购物车中，存在则修改商品数量；如果不存在，则添加商品全部信息到购物车中。



## 4）createOrder-创建订单

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
	"addr":"$addr",
    "cartlist":[{"goodsName":"$goods name",
    		    "goodsPrice":"$sale price",
    		    "totalValue":"$totalValue"},{......} ]
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
orderId | stirng | 订单号 | N 
buyerName | string | 买家名 | N
sellerName | string | 卖家名 | N 
orderStatus | int | 订单状态   eg:0失败 1成功 2待支付 3支付成功 | N 
addr | string | 收货地址 |  
**cartlist** |  | 购买的所有商品，且每件商品都应包含如下信息 |  
goodsName | string | 商品名 | 
goodsPrice | int | 商品价格 | 
totalValue | int | 总价 | 

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
 message | string | 失败时，为错误信息描述；成功时，为“ok | N         | 



## 5）cancelOrder-取消订单

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

| 码   | 描述                |
| ---- | ------------------- |
| 200  | 取消成功            |
| 401  | 取消失败，token错误 |

Body:

```
{
	"message":"$cancel failed, token error/$ok"
}
```

| 变量名  | 类型   | 描述                                  | 是否可为空 |
| ------- | ------ | ------------------------------------- | ---------- |
| message | string | 失败时，为错误信息描述；成功时，为“ok | N          |



## 6）paymentOrder-订单支付

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

| 码   | 描述                   |
| ---- | ---------------------- |
| 200  | 支付成功               |
| 401  | 支付失败，token错误    |
| 501  | 支付失败，账户余额不足 |

Body:

```
{
	"message":"$payment failed, token error/payment failed, insufficient account balance"
}
```

| 变量名  | 类型   | 描述                                  | 是否可为空 |
| ------- | ------ | ------------------------------------- | ---------- |
| message | string | 失败时，为错误信息描述；成功时，为“ok | N          |



## 7）buyergetOrder-买家查看全部订单

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
| 501  | 查询失败，暂无订单  |

Body:

```
{
	"message":"$Inquiry failed, token error/$Inquiry failed, no order/$ok",
	"orderlist":[{"orderId":"$order number",
    			 "orderStatus":"$order status",
    			 "addr":"address"，
    			 "buylist":[{"sellerName":"$seller name",
				             "goodsName":"$goods name",
						    "goodsPrice":"$goods price",
						    "totalValue":"$totalValue"},{......}]},
				  {......}]	  	
}
```

| 变量名        | 类型   | 描述                                                         | 是否可为空 |
| ------------- | ------ | ------------------------------------------------------------ | ---------- |
| errormsg      | string | 失败时，为错误信息描述，且以下变量不输出；<br />成功时，为"ok"，且输出以下变量 | Y          |
| **orderlist** |        | 用户的所有订单，且每单应该包含以下信息                       |            |
| orderId       | string | 订单号                                                       | N          |
| orderStatus   | string | 订单状态，可以是：交易成功、待支付、交易失败                 | N          |
| addr          | string | 收货地址                                                     |            |
| **buylist**   |        | 订单中的每个商品都应包含以下信息                             |            |
| sellerName    | string | 卖家名                                                       | N          |
| goodsName     | string | 商品名                                                       | N          |
| goodsPrice    | string | 商品价格                                                     | N          |
| totalValue    | string | 总价                                                         | N          |

#### 接口描述

a."orderlist"表示一个用户可能拥有多个订单；

b.单个订单可能包含多个商品，即"buylist"展示在同一个订单中的商品信息。



## 8）sellergetOrder-卖家查看全部订单

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
    			 "buylist":[{"goodsName":"$goods name",
				             "goodsPrice":"$goods price",
						    "totalValue":"$totalValue"},{......}]},
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
| **buylist**   |        | 每个用户订单中的每个商品都应包含以下信息                     |            |
| goodsName     | string | 商品名                                                       | N          |
| goodsPrice    | string | 商品价格                                                     | N          |
| totalValue    | string | 总价                                                         | N          |

