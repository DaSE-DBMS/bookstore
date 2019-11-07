修改后台用POST
查询用GET

## 查询买家信息接口

#### URL：
GET http://[address]/buyer/getMemberInfo

#### Request
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | string | 用户名 | N
token | string | 登录产生的会话标识 | N

#### Response
Status Code:
码 | 描述
--- | ---
200 | 查询成功
503 | 查询失败 


变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
name | string | 查询成功返回昵称，失败返回空字串 | N
sex | string | 性别 | N
telephoneNumber | string | 手机号 | N





## 修改买家信息接口

#### URL:
POST http://[address]/buyer/editMemberInfo

#### Request
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | string | 用户名 | N
token | string | 登录产生的会话标识 | N
name | string | 昵称 | N
sex | string | 性别 | N
telephoneNumber | string | 手机号 | N

#### Response
Status Code:
码 | 描述
--- | ---
200 | 修改成功
503 | 修改失败 

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 返回错误消息，成功时为"ok" | N

## 查询买家订单接口

#### URL:
GET http://[address]/buyer/getMemberOrder

#### Request
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | string | 用户名 | N
token | string | 登录产生的会话标识 | N

#### Response
Status Code:
码 | 描述
--- | ---
200 | 查询成功
503 | 查询失败

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
orderId | string | 订单号 | N
orderDate | string | 下单时间 | N
orderStatus | string | 订单状态 | N
productName | string | 商品名称 | N
productPrice | string | 价格 | N


## 售后处理-退货订单查询接口

#### URL:
POST http://[address]/buyer/getRefundOrder

#### Request
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | string | 用户名 | N
token | string | 登录产生的会话标识 | N

#### Response
Status Code:
码 | 描述
--- | ---
200 | 查询成功
503 | 查询失败

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
orderId | string | 退货订单ID | N
productName | string | 商品名称 | N
productPrice | string | 价格 | N


## 查询用户收获地址接口

#### URL:
GET http://[address]/buyer/getMemberConsignee

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | String | 用户名 | N
token | string | 登录产生的会话标识 | N

#### Response
Status Code:
码 | 描述
--- | ---
200 | 查询成功
503 | 查询失败

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
address | string | 收获地址 | N

## 编辑用户收获地址接口

#### URL:
POST http://[address]/buyer/editConsignee
token | string | 登录产生的会话标识 | N

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | String | 用户名 | N

#### Response
Status Code:
码 | 描述
--- | ---
200 | 编辑成功
503 | 编辑失败

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 返回错误消息，成功时为"ok" | N
