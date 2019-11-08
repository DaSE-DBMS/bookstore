修改后台用POST
查询用GET

## 查询卖家信息接口

#### URL：
GET http://[address]/seller/getMemberInfo

#### Request
Headers:

key | 类型 | 描述 | 是否可为空
---|---|---|---
token | string | 登录产生的会话标识 | N

Body:
```
{
    "username":"$user name"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | string | 用户名 | N

#### Response
Status Code:
码 | 描述
--- | ---
200 | 查询成功
501 | 查询失败 
Body:
```
{
    "errormsg":"$Access failed, token error",
    "name":"$name",
    "sex":"$sex",
    "telephoneNumber":"$telephone number"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
errormsg | string | 	失败时，为错误信息描述，且以下变量不输出；成功时，此变量为空，且输出以下变量 | Y
name | string | 查询成功返回昵称，失败返回空字串 | N
sex | string | 性别 | N
telephoneNumber | string | 手机号 | N

## 编辑卖家商品接口

#### URL:
POST http://[address]/seller/getItem

#### Request
Headers:
key | 类型 | 描述 | 是否可为空
---|---|---|---
token | string | 登录产生的会话标识 | N
Body:
```
{
    "username":"$user name",
    "buylist":[{"goodsname":"$goods name",
				"goodsnumber":"$goods number",
				"goodsprice":"$goods price",},{...}]
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | string | 用户名 | N
**goodslist** |  | **商家店铺的所有商品信息，每件商品都应包含如下信息** | 
goodsname | string | 商品名称 | N
goodsprice | string | 价格 | N
goodsnumber | string | 商品数量 | N

#### Response
Status Code:
码 | 描述
--- | ---
200 | 修改成功
501 | 修改失败

Body:
```
{
    "errormsg":"$Access failed, token error",
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
errormsg | string | 返回错误消息，成功时为"ok" | Y

## 查询卖家订单接口

#### URL:
GET http://[address]/seller/getMemberOrder

#### Request
Headers:
key | 类型 | 描述 | 是否可为空
---|---|---|---
token | string | 登录产生的会话标识 | N
Body:
```
{
    "username":"$user name"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | string | 用户名 | N

#### Response
Status Code:
码 | 描述
--- | ---
200 | 查询成功
503 | 查询失败
Body:
```
{
    "errormsg":"$Access failed, token error",
    "orderlist":[{"orderid":"$oder id",
                "oderdate":"$order date",
                "orderstatus":"$order status",
                "goodsname":"$goods name",
                "goodsprice":"$goods price"},{...}]
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
errormsg | string | 返回错误消息，成功时为"ok" | Y
**orderlist** |  | **卖家所有订单信息，且每件订单都应包含如下信息** |  
orderid | string | 订单号 | N
orderdate | string | 下单时间 | N
orderstatus | string | 订单状态 | N
goodsname | string | 商品名称 | N
goodsprice | string | 价格 | N


## 售后处理-退货订单查询接口

#### URL:
GET http://[address]/seller/getRefundOrder

#### Request
Headers:
key | 类型 | 描述 | 是否可为空
---|---|---|---
token | string | 登录产生的会话标识 | N
Body:
```
{
    "username":"$user name"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | string | 用户名 | N

#### Response
Status Code:
码 | 描述
--- | ---
200 | 查询成功
503 | 查询失败
Body:
```
{
    "errormsg":"$Access failed, token error",
    "RefundOrderList":[{"orderid":"$oder id",
                        "oderdate":"$order date",
                        "orderstatus":"$order status"},{...}]
    
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
errormsg | string | 返回错误消息，成功时为"ok" | Y
**RefundOrderList** |  | **商家所有的退货订单，且每个订单都应包括以下信息** | 
orderid | string | 退货订单ID | N
orderdate | string | 下单时间 | N
orderstatus | string | 订单状态 | N

## 查询卖家退货物流信息接口

#### URL:
GET http://[address]/seller/sellerRefundGoods  
#### Request
Headers:
key | 类型 | 描述 | 是否可为空
---|---|---|---
token | string | 登录产生的会话标识 | N
Body:
```
{
    "username":"$user name"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | String | 用户名 | N

#### Response
Status Code:
码 | 描述
--- | ---
200 | 查询成功
503 | 查询失败
Body:
```
{
    "errormsg":"$Access failed, token error",
    "RefundOrderAddrList":[{"orderid":"$oder id",
                        "oderdate":"$order date",
                        "orderstatus":"$order status",
                        "goodsame":"$goods name",
                        "address":"$address"},{...}]
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
errormsg | string | 返回错误消息，成功时为"ok" | Y
**RefundOrderAddrList** |  | **商家所有退货订单，且每个订单都应包括以下信息** | 
orderId | string | 退货订单ID | N
oderdate | string | 订单时间 | N 
orderstatus | string | 订单状态                                         | N
goodsname | string | 商品名称 | N
address | string | 收获地址 | N


