## 1）getGoods-搜索商品

#### URL

POST http://[address]/goods/getgoods

#### Request

Body:
```
{
    "keywords":"[goods name/describe]",
    "goodsTypeId":"[goods type id]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
keywords | string | 商品名或描述 | Y 
goodsTypeId | string | 商品类别编号 | Y 

#### Response

Status Code:


码 | 描述
--- | ---
200 | 搜索成功 
501 | 搜索失败，暂无相关商品 

Body：

```
{ 
	"result":"[status code]",
	"errorMsg":"[Search failed, no relevant products]",
    "goodsList": [ "merchantName":"[merchant name]",
    			  "goodsName":"[goods name]",
    			  "goodsImage":"[goods image]",
  				  "origPrice":"[original price]",
 				  "salePrice":"[sale price]" ]
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
result | string | 返回码 | N
errorMsg | string | 错误信息描述 | Y 
**goodsList** |  |  |  
merchantName | string | 商家名 | N 
goodsName | string | 商品名 | N 
goodsImage | string | 商品图片 | N 
origPrice | string | 原价格 | N 
salePrice | string | 活动价 | N 

#### 接口描述

a.仅有“keywords”。搜索商品的”keywords“可以是商品的名称，如”追风筝的人“，也可以是对商品的描述，如”一本搞笑的书“；

b.仅有“goodsTypeId”。在“goodsTypeId”中选定商品的类别，如“烹饪类”，此时展示的全是和烹饪有关的书籍；

c.两个输入参数都有，表示在指定类别下根据关键词搜索；

d.两个输入参数均为空，表示没有操作。



## 2）getGoodsDetails-商品详情

#### URL
POST http://[address]/goods/getgoodsdetails

#### Request

Body:
```
{
    "merchantId":"[merchant id]",
    "goodsId":"[goods id]",
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

body：

```
{ 
	"result":"[status code]",
	"errorMsg":"[Search failed, no details about the goods]",
    "goodsName":"[goods name]",
    "goodsAuth":"[author]",
    "goodsPub":"[publishing house]",
    "OrigPrice":"[original price]",
    "salePrice":"[sale price]",
    "goodsDes":"[goods describe]",
    "isCollect":"[0/1]",
    "merchantName":"[merchant name]"    
}
```

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
 merchantName | string | 商家名 | N 

#### 接口描述

当为游客的时候，输入参数“userId”默认为空，表示“该商品未被收藏”



## 3）getMerchantInfo-查询特定商品的商家信息

#### URL
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
merchantId | string | 商家编号 | N
goodsId | string | 商品编号 | N 

#### Response

Status Code:

码 | 描述
--- | ---
200 | 查询成功 
501 | 查询失败，商家不存在 

body：

```
{ 
	"result":"[status code]",
	"errorMsg":"[Search failed, the merchant does not exist]",
	"merchantNmae":"[merchant name]",
	"merchantLoc":"[merchant location]",
	"merchantRank":"[merchant rank]",
    "goodsList": [ "merchantName":"[merchant name]",
    			  "goodsName":"[goods name]",
    			  "goodsImage":"[goods image]",
  				  "origPrice":"[original price]",
 				  "salePrice":"[sale price]" ]
}
```



变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
 result               | string | 返回码       | N          
errorMsg | string | 错误信息描述 | Y 
merchantName | string | 商家名 | N 
merchantLoc | string | 所在地 | N 
merchantRank | string | 商家星级 | N 
**goodsList** |  |  |  
（同“getGoods”接口） |  |  |  

#### 接口描述

在“商品详情”页的”商家名“可以访问到商家的详细信息；商家信息除了名称、所在地和星级外，还会显示此商家的全部商品