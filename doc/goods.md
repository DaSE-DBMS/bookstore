## 1）searchGoods-搜索商品

#### URL

POST http://[address]/goods/searchgoods

#### Request

Body:
```
{
    "keywords":"[goods name/describe]",
    "goodstypeid":"[goods type id]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
keywords | string | 商品名或描述 | Y 
goodstypeid | string | 商品类别编号 | Y 

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
	"errormsg":"[Search failed, no relevant products]",
    "goodslist": [ "merchantname":"[merchant name]",
    			  "goodsname":"[goods name]",
    			  "goodsimage":"[goods image]",
  				  "origprice":"[original price]",
 				  "saleprice":"[sale price]" ]
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
result | string | 返回码 | N
errormsg | string | 错误信息描述 | Y 
**goodslist** |  |  |  
merchantname | string | 商家名 | N 
goodsname | string | 商品名 | N 
goodsimage | string | 商品图片 | N 
origprice | string | 原价格 | N 
saleprice | string | 活动价 | N 

#### 接口描述

a.仅有“keywords”。搜索商品的”keywords“可以是商品的名称，如”追风筝的人“，也可以是对商品的描述，如”一本搞笑的书“；

b.仅有“goodstypeid”。在“goodstypeid”中选定商品的类别，如“烹饪类”，此时展示的全是和烹饪有关的书籍；

c.两个输入参数都有，表示在指定类别下根据关键词搜索；

d.两个输入参数均为空，表示没有操作。



## 2）getGoodsDetails-商品详情

#### URL
POST http://[address]/goods/getgoodsdetails

#### Request

Body:
```
{
    "merchantid":"[merchant id]",
    "goodsid":"[goods id]",
    "userid":"[user id]
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
merchantid | string | 商家编号 | N
goodsid | string | 商品编号 | N 
userid | string | 用户编号 | Y 

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
	"errormsg":"[Search failed, no details about the goods]",
    "goodsname":"[goods name]",
    "goodsauth":"[author]",
    "goodspub":"[publishing house]",
    "origprice":"[original price]",
    "saleprice":"[sale price]",
    "goodsdes":"[goods describe]",
    "iscollect":"[0/1]",
    "merchantname":"[merchant name]"    
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
 result    | string | 返回码       | N          
 errormsg | string | 错误信息描述 | Y          
 goodsname | string | 商品名       | N          
 goodsauth | string | 作者   | N          
 goodspub | string | 出版社  | N          
 origprice | string | 原价格       | N          
 saleprice | string | 活动价       | N          
 goodsdes | string | 商品描述     | N 
 iscollect | string | 商品是否收藏 | N 
 merchantname | string | 商家名 | N 

#### 接口描述

当为游客的时候，输入参数“userid”默认为空，表示“该商品未被收藏”



## 3）getMerchantInfo-查询特定商品的商家信息

#### URL
POST http://[address]/goods/getmerchantinfo

#### Request

Body:
```
{
   "merchantid":"[merchant id]",
   "goodsid":"[goods id]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
merchantid | string | 商家编号 | N
goodsid | string | 商品编号 | N 

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
	"errormsg":"[Search failed, the merchant does not exist]",
	"merchantname":"[merchant name]",
	"merchantloc":"[merchant location]",
	"merchantrank":"[merchant rank]",
    "goodslist": [ "merchantname":"[merchant name]",
    			  "goodsname":"[goods name]",
    			  "goodsimage":"[goods image]",
  				  "origprice":"[original price]",
 				  "saleprice":"[sale price]" ]
}
```



变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
 result               | string | 返回码       | N          
errormsg | string | 错误信息描述 | Y 
merchantname | string | 商家名 | N 
merchantloc | string | 所在地 | N 
merchantrank | string | 商家星级 | N 
**goodslist** |  |  |  
（同“searchGoods”接口） |  |  |  

#### 接口描述

在“商品详情”页的”商家名“可以访问到商家的详细信息；商家信息除了名称、所在地和星级外，还会显示此商家的全部商品