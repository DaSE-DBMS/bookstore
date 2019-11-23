## 1）searchGoods-搜索商品

#### URL

POST http://$address$/goods/searchGoods

#### Request

Body:
```
{
    "keywords":"$goods name/describe",
    "goodstype":"$goods type"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
keywords | string | 商品名或描述 | Y 
goodstype | string | 商品类别 | Y 

#### Response

Status Code:


码 | 描述
--- | ---
200 | 搜索成功 
512 | 搜索失败，暂无相关商品 

Body：

```
{ 
	"message":"$Search failed, no relevant products/$ok",
    "goodslist": [{"goodsId":"$goods id",
    			  "goodsName":"$goods name",
  				  "goodsAuth":"$goods author",
 				  "goodsPrice":"$sale price",
 				  "goodsNum":"$goods number",
 				  "goodsType":"$goods type",
 				  "goodsDsr":"$goods describe"
 				  "sellerName":"$sellerName"},{......}]
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 失败时，为错误信息描述，且以下变量不输出；<br />成功时，为"ok"，且输出以下变量 | N 
**goodslist** |  | 满足搜索条件的所有商品，且每件商品都应包含如下信息 |  
goodsId | string | 商品编号 | N 
goodsName | string | 商品名 | N 
 goodsAuth | string | 图书作者 | Y 
goodsPrice | int | 商品价格 | N 
goodsNum | int | 商品数量 | Y 
goodsType | string | 商品类别，eg：烹饪类、计算机类、经济类、艺术类...... | Y 
goodsDsr | string | 商品描述，用于在搜索商品的时候进行模糊匹配 | Y 
sellerName | string | 卖家名 |  

#### 接口描述

a.输入参数仅有“keywords”。搜索商品的”keywords“可以是商品的名称，如”追风筝的人“，也可以是对商品的描述，如”一本搞笑的书“；

b.输入参数仅有“goodstypeid”。在“goodstypeid”中选定商品的类别，如“烹饪类”，此时展示的全是和烹饪有关的书籍；

c.两个输入参数都有，表示在“指定类别”下根据“书名”搜索；

d.两个输入参数均为空，表示没有操作。



## 2）addGoods-卖家添加商品

#### URL
POST http://$address$/goods/addGoods

#### Request

Headers:

| key   | 类型   | 描述               | 是否为空 |
| ----- | ------ | ------------------ | -------- |
| token | string | 登录产生的会话标识 | N        |

Body:
```
{
   "goodsId":"$goods id",
   "goodsName":"$goods name",
   "goodsAuth":"$goods author",
   "goodsPrice":"$sale price",
   "goodsNum":"$goods number",
   "goodsType":"$goods type",
   "goodsDsr":"$goods describe",
   "sellerName":"$sellerName"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
goodslist | (同上goodslist中的变量) |  | N

#### Response

Status Code:

码 | 描述
--- | ---
200 | 插入成功 
401 | 插入失败，token错误 

body：

```
{ 
	"message":"$Insert failed, token error/$ok"
}
```



变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 失败时，错误信息描述；成功时，为"ok" | N 



## 3）delGoods-卖家删除商品

#### URL

POST http://$address$/goods/delGoods

#### Request

Headers:

| key   | 类型   | 描述               | 是否为空 |
| ----- | ------ | ------------------ | -------- |
| token | string | 登录产生的会话标识 | N        |

Body:

```
{
   "goodsId":"$goods id"
   "sellerName":"$seller name"
}
```

| 变量名     | 类型   | 描述     | 是否可为空 |
| ---------- | ------ | -------- | ---------- |
| goodsId    | string | 商品编号 | N          |
| sellerName | string | 卖家名   | N          |

#### Response

Status Code:

| 码   | 描述                |
| ---- | ------------------- |
| 200  | 删除成功            |
| 401  | 删除失败，token错误 |

body：

```
{ 
	"message":"$delete failed, error token/$ok"
}
```



| 变量名  | 类型   | 描述                                 | 是否可为空 |
| ------- | ------ | ------------------------------------ | ---------- |
| message | string | 失败时，错误信息描述；成功时，为"ok" | N          |

