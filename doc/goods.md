## 1）getGoods-搜索商品

#### URL：
POST http://[address]/goods/getgoods

#### Request

Body:
```
{
    "keywords":"[goods name/describe]"，
    "filters":"[goods type]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
keywords | string | 商品名或描述 | N
filters | string | 过滤条件，比如商品类别 | Y 

#### Response

Status Code:


码 | 描述
--- | ---
200 | 搜索成功 
501 | 搜索失败，暂无相关商品 


返回参数：
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
result | string | 返回码 | N
errorMsg | string | 错误信息描述 | Y 
**goodsList** |  |  |  
merchantName | string | 商家名 | N 
goodsName | string | 商品名 | N 
goodsImage | string | 商品图片 | N 
OrigPrice | string | 原价格 | N 
salePrice | string | 活动价 | N 



## 2）getGoodsDetails-商品详情

#### URL：
POST http://[address]/goods/getgoodsdetails

#### Request

Body:
```
{
    "merchantId":"[merchant id]",
    "goodsId":"[goods id]"，
    "userId""[user id]
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
merchantId | string | 商家编号 | N
goodsId | string | 商品编号 | N 
userId | string | 用户编号 | Y 

#### Response

Status Code:

码 | 描述
--- | ---
200 | 查询成功 
501 | 查询失败，商品没有详细信息 

返回参数：
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
 result    | string | 返回码       | N          
 errorMsg  | string | 错误信息描述 | Y          
 goodsName | string | 商品名       | N          
 goodsAuth | string | 作者   | N          
 goodsPub | string | 出版社  | N          
 OrigPrice | string | 原价格       | N          
 salePrice | string | 活动价       | N          
 goodsDes  | string | 商品描述     | N 
 isCollect | string | 商品是否收藏 | N 



## 3）getCategory-类别查询

#### URL：
POST http://[address]/goods/goodsType

#### Request

Body:
```
{
    "goodsType":"[goods type]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
goodsType | string | 商品类别 | N

#### Response

Status Code:

码 | 描述
--- | ---
200 | 查询成功 
501 | 查询失败，此类别下暂无商品信息 

返回参数：
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
 result               | string | 返回码       | N          
 errorMsg             | string | 错误信息描述 | Y          
 **goodsList**        |        |              |            
 （同“getGoods”接口） |        |              |            



## 4）getMerchantInfo-查询特定商品的商家信息

#### URL：
POST http://[address]/goods/getmerchantinfo

#### Request

Body:
```
{
   "merchantId":"[merchant id]",
   "goodsId":"[goods id]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
merchantName | string | 商家编号 | N
goodsId | string | 商品编号 | N 

#### Response

Status Code:

码 | 描述
--- | ---
200 | 查询成功 
501 | 查询失败，商家不存在 

返回参数：
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
 result               | string | 返回码       | N          
errorMsg | string | 错误信息描述 | Y 
merchantName | string | 商家名 | N 
merchantLoc | string | 所在地 | N 
merchantRank | string | 商家星级 | N 
**goodsList** |  |  |  
（同“getGoods”接口） |  |  |  
