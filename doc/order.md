## 1）getCart-查看购物车

#### URL
POST http://[address]/order/getcart

#### Request

Headers:

| key   | 类型   | 描述               | 是否为空 |
| ----- | ------ | ------------------ | -------- |
| token | string | 登录产生的会话标识 | N        |

Body:
```
{
    "userId":"[user id]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
userId | string | 用户编号 | N

#### Response

Status Code:


码 | 描述
--- | ---
200 | 访问成功 
401 | 访问失败，token错误 

body：

```
{ 
	"result":"[status code]",
	"errorMsg":"[Access failed, token error]",
	"goodsSum":"[goods sum]",
	"goodsAmount":"[goods amount]",
	"itemList":[ "cartItemId":"[cart item id]",
				"merchantName":"[merchant name]",
				"goodsName":"[goods name]",
				"goodsNumber":"[goods number]",
				"goodsImage":"[goods image]",
				"salePrice":"[sale price]" ]
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
 result   | string | 返回码       | N          
 errorMsg | string | 错误信息描述 | Y          
 goodsSum | string | 总商品数 | N 
 goodsAmount | string | 总金额 | N 
 **itemList** |        |              |            
 cartItemId | string | 购物项编号 | N 
 merchantName | string | 商家名 | N 
 goodsName | string | 商品名 | N 
 goodsNumber | string | 商品数量 | N 
 goodsImage | string | 商品图片 | N 
 salePrice | string | 活动价 | N 



## 2）delCart-删除购物车商品

#### URL
POST http://[address]/order/delcart

#### Request

Headers:

| key   | 类型   | 描述               | 是否为空 |
| ----- | ------ | ------------------ | -------- |
| token | string | 登录产生的会话标识 | N        |

Body:
```
{
    "userId":"[user id]",
    "cartItemId":"[cart item id]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
userId | string | 用户编号 | N
 cartItemId | string | 购物项编号 | N          

#### Response

Status Code:


码 | 描述
--- | ---
200 | 删除成功 
401 | 删除失败，token错误 


Body:
```
{
	"result":"[status code]",
	"errorMsg":"[Delete failed, token error]"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
 result   | string | 返回码                     | N          
errorMsg | string | 错误信息描述，成功返回"ok" | Y 



## 3）addCart-添加商品到购物车

#### URL
POST http://[address]/order/addcart

#### Request

Headers:

| key   | 类型   | 描述               | 是否为空 |
| ----- | ------ | ------------------ | -------- |
| token | string | 登录产生的会话标识 | N        |

Body:
```
{
    "userId":"[user id]",
    “merchantId":"[merchant id]",
    "goodsId":"[goods id]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
userId | string | 用户编号 | N
merchantId | string | 商家编号 | N
goodsId | string | 商品编号 | N 

#### Response

Status Code:

码 | 描述
--- | ---
200 | 添加成功 
401 | 添加失败，token错误 

Body:
```
{
	"result":"[status code]",
	"errorMsg":"[addition failed, token error]"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
 result   | string | 返回码                     | N          
errorMsg | string | 错误信息描述，成功返回"ok" | Y 



## 4）createOrder-创建订单

#### URL
POST http://[address]/order/createorder

#### Request

Headers:

| key   | 类型   | 描述               | 是否为空 |
| ----- | ------ | ------------------ | -------- |
| token | string | 登录产生的会话标识 | N        |

Body:
```
{
	"userId":"[user id]",
	"goodsSum":"[goods sum]",
	"goodsAmount":"[goods amount]",
    "buyList":[ "merchantName":"[merchant name]",
    		   "goodsName":"[goods name]",
    		   "goodsNumber":"[goods number]"，
    		   "salePrice":"[sale price]" ]
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
userId | string | 用户编号 | N
goodsSum | string | 总商品数 | N 
goodsAmount | string | 总金额 | N 
**buyList** |  |  |  
 merchantName | string | 商家名 | N 
goodsName | string | 商品名 | N 
goodsNumber | string | 商品数量 | N 
salePrice | string | 活动价 | N 

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
	"result":"[status code]",	
    "message":"[order generation failed，token error/order generation failed，no goods]"，
    "orderNo":"[order number]"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
 result   | string | 返回码       | N          
 errorMsg | string | 错误信息描述 | Y          
 orderNo  | sring  | 订单号       | N          



## 5）cancelOrder-取消订单

#### URL：

POST http://[address]/order/cancelorder

#### Request

Headers:

| key   | 类型   | 描述               | 是否为空 |
| ----- | ------ | ------------------ | -------- |
| token | string | 登录产生的会话标识 | N        |

Body:

```
{
    “orderNo":"[order number]
}
```

| 变量名  | 类型 | 描述   | 是否可为空 |
| ------- | ---- | ------ | ---------- |
| orderNo | int  | 订单号 | N          |

#### Response

Status Code:

| 码   | 描述                |
| ---- | ------------------- |
| 200  | 取消成功            |
| 401  | 取消失败，token错误 |

Body:

```
{
	"result":"[status code]",
	"errorMsg":"[cancel failed, token error]"
}
```

| 变量名   | 类型   | 描述                       | 是否可为空 |
| -------- | ------ | -------------------------- | ---------- |
| result   | string | 返回码                     | N          |
| errorMsg | string | 错误信息描述，成功时为"ok" | N          |



## 6）paymentOrder-订单支付

#### URL：

POST http://[address]/order/paymentorder

#### Request

Headers:

| key   | 类型   | 描述      |
| ----- | ------ | --------- |
| token | string | 访问token |

Body:

```
{
    "userId":"[user id]",
    “orderNo":"[order No]"
}
```

| 变量名  | 类型   | 描述   | 是否可为空 |
| ------- | ------ | ------ | ---------- |
| userId  | string | 用户名 | N          |
| orderNo | string | 订单号 | N          |

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
	"result":"[status code]",
	"errorMsg":"[payment failed, token error/payment failed, insufficient account balance]"
}

```

| 变量名   | 类型   | 描述                       | 是否可为空 |
| -------- | ------ | -------------------------- | ---------- |
| result   | string | 返回码                     | N          |
| errorMsg | string | 错误信息描述，成功时为"ok" | N          |



## 7）allOrder-查看全部订单

#### URL：

POST http://[address]/order/allorder

#### Request

Headers:

| key   | 类型   | 描述               | 是否为空 |
| ----- | ------ | ------------------ | -------- |
| token | string | 登录产生的会话标识 | N        |

Body:

```
{
    "userId":"[user id]"
}
```

| 变量名 | 类型   | 描述     | 是否可为空 |
| ------ | ------ | -------- | ---------- |
| userId | string | 用户编号 | N          |

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
	"result":"[status code]",
	"errorMsg":"[Inquiry failed, token error/Inquiry failed, no order]",
	"orderList":[ "orderNo":"[order number]",
    			 "orderStatus":"[order status]",
    			 "merchantName":"[merchant name]",
    			 "goodsImage":"[goods image]",
    			 "goodsName":"[goods name]",
    			 "goodsAmount":"[goods amount]" ]
}
```

| 变量名        | 类型   | 描述         | 是否可为空 |
| ------------- | ------ | ------------ | ---------- |
| result        | string | 返回码       | N          |
| errorMsg      | string | 错误信息描述 | Y          |
| **orderList** |        |              |            |
| orderNo       | string | 订单号       | N          |
| orderStatus   | string | 订单状态     | N          |
| merchantName  | string | 商家名       | N          |
| goodsImage    | string | 商品图片     | N          |
| goodsName     | string | 商品名       | N          |
| goodsAmount   | string | 总金额       | N          |

#### 接口描述

输出参数”orderStatus“订单状态可以是：交易成功、待支付、交易失败



