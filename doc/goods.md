## getMerchantgoods-查询商家全部商品

#### URL：
POST http://[address]/goods/getmerchantgoods

#### Request

Headers:

| key   | 类型   | 描述      |
| ----- | ------ | --------- |
| token | string | 访问token |

Body:
```
{
    "merchantname":"[merchant name]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
merchantname | string | 商家名 | N

#### Response

Status Code:


码 | 描述
--- | ---
200 | 获取成功 
401 | 获取失败，商家不存在 


Body:
```
{
    "message":"[error message]"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 返回错误消息，成功时为"ok" | N

## getGoods-搜索商品

#### URL：
POST http://[address]/goods/getgoods

#### Request

Headers:

| key   | 类型   | 描述      |
| ----- | ------ | --------- |
| token | string | 访问token |

Body:
```
{
    "goodsname":"[goods name]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
goodsname | string | 商品名 | N

#### Response

Status Code:


码 | 描述
--- | ---
200 | 搜索成功 
401 | 搜索失败，暂无相关商品 


Body:
```
{
    "message":"[error message]"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 返回错误消息，成功时为"ok" | N

## getGoodsDetails-商品详情（图+文）

#### URL：
POST http://[address]/goods/getgoodsdetails

#### Request

Headers:

| key   | 类型   | 描述      |
| ----- | ------ | --------- |
| token | string | 访问token |

Body:
```
{
    "merchantname":"[merchant name]",
    "goodsname":"[goods name]",
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
merchantname | string | 商家名 | N
goodsname | string | 商品名 | N 

#### Response

Status Code:

码 | 描述
--- | ---
200 | 查询成功 
401 | 查询失败，商家不存在或商品不存在 

Body:
```
{
    "message":"[error message]"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 返回错误消息，成功时为"ok" | N

## getCategory-类别查询

#### URL：
POST http://[address]/goods/category

#### Request

Headers:

| key   | 类型   | 描述      |
| ----- | ------ | --------- |
| token | string | 访问token |

Body:
```
{
    "category":"[category name]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
category | string | 类别名 | N

#### Response

Status Code:

码 | 描述
--- | ---
200 | 查询成功 
401 | 查询失败，token错误 

Body:
```
{
    "message":"[error message]",
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 返回错误消息，成功时为"ok" | N

## getMerchantInfo-查询特定商品的商家信息

#### URL：
POST http://[address]/goods/getmerchantinfo

#### Request

Headers:

key | 类型 | 描述
---|---|---
token | string | 访问token

Body:
```
{
    "goodsname":"[goods name]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
goodsname | string | 商品名 | N

#### Response

Status Code:

码 | 描述
--- | ---
200 | 查询成功 
401 | 查询失败，商品名或token错误 

Body:
```
{
    "message":"[error message]"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 返回错误消息，成功时为"ok" | N
