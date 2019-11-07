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
    "userid":"[user id]"
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
	"errormsg":"[Access failed, token error]",
	"goodssum":"[goods sum]",
	"goodsamount":"[goods amount]",
	"itemlist":[ "cartitemid":"[cart item id]",
				"merchantname":"[merchant name]",
				"goodsname":"[goods name]",
				"goodsnumber":"[goods number]",
				"goodsimage":"[goods image]",
				"saleprice":"[sale price]" ]
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
 result   | string | 返回码       | N          
 errormsg | string | 错误信息描述 | Y          
 goodssum | string | 总商品数 | N 
 goodsamount | string | 总金额 | N 
 **itemlist** |        |              |            
 cartItemid | string | 购物项编号 | N 
 merchantname | string | 商家名 | N 
 goodsname | string | 商品名 | N 
 goodsnumber | string | 商品数量 | N 
 goodsimage | string | 商品图片 | N 
 saleprice | string | 活动价 | N 



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
    "userid":"[user id]",
    "cartitemid":"[cart item id]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
userid | string | 用户编号 | N
 cartItemid | string | 购物项编号 | N          

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
	"errormsg":"[Delete failed, token error]"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
 result   | string | 返回码                     | N          
errormsg | string | 错误信息描述，成功返回"ok" | Y 



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
    "userid":"[user id]",
    “merchantid":"[merchant id]",
    "goodsid":"[goods id]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
userid | string | 用户编号 | N
merchantid | string | 商家编号 | N
goodsid | string | 商品编号 | N 

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
	"errormsg":"[addition failed, token error]"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
 result   | string | 返回码                     | N          
errormsg | string | 错误信息描述，成功返回"ok" | Y 



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
	"userid":"[user id]",
	"goodssum":"[goods sum]",
	"goodsamount":"[goods amount]",
    "buylist":[ "merchantname":"[merchant name]",
    		   "goodsname":"[goods name]",
    		   "goodsnumber":"[goods number]"，
    		   "saleprice":"[sale price]" ]
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
userid | string | 用户编号 | N
goodssum | string | 总商品数 | N 
goodsamount | string | 总金额 | N 
**buylist** |  |  |  
 merchantname | string | 商家名 | N 
goodsname | string | 商品名 | N 
goodsnumber | string | 商品数量 | N 
saleprice | string | 活动价 | N 

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
    "errormsg":"[order generation failed，token error/order generation failed，no goods]"，
    "orderno":"[order number]"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
 result   | string | 返回码       | N          
 errormsg | string | 错误信息描述 | Y          
 orderno | sring  | 订单号       | N          



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
    “orderno":"[order number]
}
```

| 变量名  | 类型 | 描述   | 是否可为空 |
| ------- | ---- | ------ | ---------- |
| orderno | int  | 订单号 | N          |

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
	"errormsg":"[cancel failed, token error]"
}
```

| 变量名   | 类型   | 描述                       | 是否可为空 |
| -------- | ------ | -------------------------- | ---------- |
| result   | string | 返回码                     | N          |
| errormsg | string | 错误信息描述，成功时为"ok" | N          |



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
| userid  | string | 用户名 | N          |
| orderno | string | 订单号 | N          |

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
	"errormsg":"[payment failed, token error/payment failed, insufficient account balance]"
}

```

| 变量名   | 类型   | 描述                       | 是否可为空 |
| -------- | ------ | -------------------------- | ---------- |
| result   | string | 返回码                     | N          |
| errormsg | string | 错误信息描述，成功时为"ok" | N          |



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
    "userid":"[user id]"
}
```

| 变量名 | 类型   | 描述     | 是否可为空 |
| ------ | ------ | -------- | ---------- |
| userid | string | 用户编号 | N          |

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
	"errormsg":"[Inquiry failed, token error/Inquiry failed, no order]",
	"orderlist":[ "orderno":"[order number]",
    			 "orderstatus":"[order status]",
    			 "merchantname":"[merchant name]",
    			 "goodsimage":"[goods image]",
    			 "goodsname":"[goods name]",
    			 "goodsamount":"[goods amount]" ]
}
```

| 变量名        | 类型   | 描述         | 是否可为空 |
| ------------- | ------ | ------------ | ---------- |
| result        | string | 返回码       | N          |
| errormsg      | string | 错误信息描述 | Y          |
| **orderlist** |        |              |            |
| orderno       | string | 订单号       | N          |
| orderstatus   | string | 订单状态     | N          |
| merchantname  | string | 商家名       | N          |
| goodsimage    | string | 商品图片     | N          |
| goodsname     | string | 商品名       | N          |
| goodsamount   | string | 总金额       | N          |

#### 接口描述

输出参数”orderstatus“订单状态可以是：交易成功、待支付、交易失败



