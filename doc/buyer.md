修改后台用POST
查询用GET

## 查询买家信息接口

#### URL：
GET http://[address]/buyer/getMemberInfo

#### Request
Body:
```
{
    "username":"[user name]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | string | 用户名 | N
token | string | 登录产生的会话标识 | N

#### Response

Status Code:

码 | 描述
--- | ---
200 | 查询成功
503 | 查询失败 返回

Body:
```
{
    "message":"[error message]"
    "sex" :"[sex]"
    "telephoneNumber":"[telephoneNumber]"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---

name | string | 查询成功返回昵称，失败返回空字串 | N
sex | string | 性别 | N
telephoneNumber | string | 手机号 | N





## 修改买家信息接口

#### URL:
POST http://[address]/buyer/editMemberInfo

#### Request
Body:
```
{
    "name":"[name]"
    "sex":"[sex]"
    "telephoneNumber":"[telephoneNumber]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
name | string | 昵称 | N
sex | string | 性别 | N
telephoneNumber | string | 手机号 | N

#### Response

Status Code:

码 | 描述
--- | ---

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 返回错误消息，成功时为"ok" | N

## 查询买家订单接口

#### URL:
GET http://[address]/buyer/getMemberOrder

#### Request
Body:
```
{
    "username":"[user name]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | string | 用户名 | N
token | string | 登录产生的会话标识 | N

#### Response

Status Code:

码 | 描述
--- | ---


变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
orderId | string | 订单号 | N



## 售后处理-退货订单查询接口

#### URL:
POST http://[address]/buyer/getRefundOrder

#### Request
Body:
```
{
    "username":"[user name]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | string | 用户名 | N
token | string | 登录产生的会话标识 | N

#### Response

Status Code:

码 | 描述
--- | ---

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
orderId | string | 退货订单ID | N


## 售后处理-退货详情接口

#### URL:
POST http://[address]/buyer/returnOrderDetail

## 售后处理-退还货物接口

#### URL:
POST http://[address]/buyer/refundsGoods

## 查询用户收获地址接口

#### URL:
GET http://[address]/buyer/getMemberConsignee

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | String | 用户名 | N

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---


## 编辑用户收获地址接口

#### URL:
POST http://[address]/buyer/editConsignee

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | String | 用户名 | N

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 
