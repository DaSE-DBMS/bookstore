## getCart-查看购物车

#### URL：
POST http://[address]/order/getcart

#### Request

Headers:

| key   | 类型   | 描述      |
| ----- | ------ | --------- |
| token | string | 访问token |

Body:
```
{
    "username":"[user name]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | string | 用户名 | N

#### Response

Status Code:


码 | 描述
--- | ---
200 | 访问成功 
401 | 访问失败，token错误 


Body:
```
{
    "message":"[error message/cart info]"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 返回错误消息，成功时返回购物车信息 | N

## delCart-删除购物车商品

#### URL：
POST http://[address]/order/delcart

#### Request

Headers:

| key   | 类型   | 描述      |
| ----- | ------ | --------- |
| token | string | 访问token |

Body:
```
{
    "username":"[user name]",
    "goodsname":"[goods name]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | string | 用户名 | N
goodsname | string | 商品名 | N 

#### Response

Status Code:


码 | 描述
--- | ---
200 | 删除成功 
401 | 删除失败，token错误 


Body:
```
{
    "message":"[error message]"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 返回错误消息，成功时为"ok" | N

## addCart-添加商品到购物车

#### URL：
POST http://[address]/order/addcart

#### Request

Headers:

| key   | 类型   | 描述      |
| ----- | ------ | --------- |
| token | string | 访问token |

Body:
```
{
    "username":"[user name]",
    "goodsname":"[goods name]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | string | 用户名 | N
goodsname | string | 商品名 | N

#### Response

Status Code:

码 | 描述
--- | ---
200 | 添加成功 
401 | 添加失败，token错误 

Body:
```
{
    "message":"[error message]"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 返回错误消息，成功时为"ok" | N

## createOrder-生成订单

#### URL：
POST http://[address]/order/createorder

#### Request

Headers:

| key   | 类型   | 描述      |
| ----- | ------ | --------- |
| token | string | 访问token |

Body:
```
{
    “goodsset":[goods set]
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
goodsset | set  | 若干商品名 | N

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
    "message":"[error message/order info]"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 返回错误消息，成功时返回订单信息 | N

## submitOrder-提交订单

#### URL：
POST http://[address]/order/submitorder

#### Request

Headers:

key | 类型 | 描述
---|---|---
token | string | 访问token

Body:
```
{
    "username":"[user name]",
    “orderid":"[order id]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | string | 用户名 | N
orderid | int | 订单编号 | N 

#### Response

Status Code:

码 | 描述
--- | ---
200 | 登出成功
401 | 登出失败，用户名或token错误

Body:
```
{
    "message":"[error message/payment]"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 返回错误消息，成功时返回支付页面 | N

## cancelOrder-取消订单

#### URL：

POST http://[address]/order/cancelorder

#### Request

Headers:

| key   | 类型   | 描述      |
| ----- | ------ | --------- |
| token | string | 访问token |

Body:

```
{
    "username":"[user name]",
    “orderid":"[order id]
}
```

| 变量名   | 类型   | 描述     | 是否可为空 |
| -------- | ------ | -------- | ---------- |
| username | string | 用户名   | N          |
| orderid  | int    | 订单编号 | N          |

#### Response

Status Code:

| 码   | 描述                        |
| ---- | --------------------------- |
| 200  | 取消成功                    |
| 401  | 取消失败，用户名或token错误 |

Body:

```
{
    "message":"[error message/payment]"
}
```

| 变量名  | 类型   | 描述                             | 是否可为空 |
| ------- | ------ | -------------------------------- | ---------- |
| message | string | 返回错误消息，成功时返回支付页面 | N          |

## paymentOrder-订单支付

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
    "username":"[user name]",
    “orderid":"[order id]",
    “balance”:"[account balance]"
}
```

| 变量名   | 类型   | 描述     | 是否可为空 |
| -------- | ------ | -------- | ---------- |
| username | string | 用户名   | N          |
| orderid  | int    | 订单编号 | N          |
| balance  | float  | 账户余额 | N          |

#### Response

Status Code:

| 码   | 描述                        |
| ---- | --------------------------- |
| 200  | 支付成功                    |
| 401  | 支付失败，用户名或token错误 |
| 501  | 支付失败，账户余额不足      |

Body:

```
{
    "message":"[error message]"
}
```

| 变量名  | 类型   | 描述                       | 是否可为空 |
| ------- | ------ | -------------------------- | ---------- |
| message | string | 返回错误消息，成功时为"ok" | N          |

## allOrder-查看全部订单

#### URL：

POST http://[address]/order/allorder

#### Request

Headers:

| key   | 类型   | 描述      |
| ----- | ------ | --------- |
| token | string | 访问token |

Body:

```
{
    "username":"[user name]"
}
```

| 变量名   | 类型   | 描述   | 是否可为空 |
| -------- | ------ | ------ | ---------- |
| username | string | 用户名 | N          |

#### Response

Status Code:

| 码   | 描述                        |
| ---- | --------------------------- |
| 200  | 查询成功                    |
| 401  | 查询失败，用户名或token错误 |
| 501  | 查询失败，暂无订单          |

Body:

```
{
    "message":"[error message/order info]"
}
```

| 变量名  | 类型   | 描述                             | 是否可为空 |
| ------- | ------ | -------------------------------- | ---------- |
| message | string | 返回错误消息，成功时返回订单信息 | N          |





