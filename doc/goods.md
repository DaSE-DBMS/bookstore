## getMerchantgoods-查询商家全部商品

#### URL：
POST http://[address]/goods/getmerchantgoods

#### Request

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
501 | 获取失败，商家不存在或商家无商品 


Body:
```
{
    "message":"[error message/goods info]"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 返回错误消息，成功时返回此商家全部商品信息 | N

## getGoods-搜索商品

#### URL：
POST http://[address]/goods/getgoods

#### Request

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
501 | 搜索失败，暂无相关商品 


Body:
```
{
    "message":"[error message/goods info]"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 返回错误消息，成功时返回商品信息 | N

## getGoodsDetails-商品详情（图+文）

#### URL：
POST http://[address]/goods/getgoodsdetails

#### Request

Body:
```
{
    "merchantname":"[merchant name]",
    "goodsname":"[goods name]"
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
501 | 查询失败，商品没有详细信息 

Body:
```
{
    "message":"[error message/goods details info]"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 返回错误消息，成功时返回商品详细信息 | N

## getCategory-类别查询

#### URL：
POST http://[address]/goods/category

#### Request

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
501 | 查询失败，没有商品属于此类别 

Body:
```
{
    "message":"[error message/goods info]"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 返回错误消息，成功时返回商品信息 | N

## getMerchantInfo-查询特定商品的商家信息

#### URL：
POST http://[address]/goods/getmerchantinfo

#### Request

Body:
```
{
   "merchantname":"[merchant name]",
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
501 | 查询失败，商家不存在 

Body:
```
{
    "message":"[error message/merchant info]"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 返回错误消息，成功时返回商家信息 | N
