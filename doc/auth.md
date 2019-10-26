## Register-注册

#### URL：
POST http://[address]/auth/register

#### Request

Body:
```
{
    "username":"[user name]",
    "password":"[user password]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | string | 用户名 | N
password | string | 登陆密码 | N

#### Response

Status Code:


码 | 描述
--- | ---
200 | 注册成功
401 | 注册失败，用户名重复


Body:
```
{
    "message":"[error message]"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 返回错误消息，成功时为"ok" | N

## UnRegister-注销用户

#### URL：
POST http://[address]/auth/unregister

#### Request

Body:
```
{
    "username":"[user name]",
    "password":"[user password]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | string | 用户名 | N
password | string | 登陆密码 | N

#### Response

Status Code:


码 | 描述
--- | ---
200 | 注销成功
401 | 注销失败，用户名不存在或密码不正确


Body:
```
{
    "message":"[error message]"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 返回错误消息，成功时为"ok" | N

## Login-登录

#### URL：
POST http://[address]/auth/login

#### Request

Body:
```
{
    "username":"[user name]",
    "password":"[user password]",
    "terminal":"[terminal code]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | string | 用户名 | N
password | string | 登陆密码 | N
terminal | string | 终端代码 | N

#### Response

Status Code:

码 | 描述
--- | ---
200 | 登录成功
401 | 登录失败，用户名或密码错误

Body:
```
{
    "message":"[error message]",
    "token":"[access token]"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 返回错误消息，成功时为"ok" | N
token | string | 访问token，用户登录后每个请求应在headers中传入这个token | 成功时不为空

## Password-更改密码

#### URL：
POST http://[address]/auth/password

#### Request

Body:
```
{
    "username":"[user name]",
    "oldPassword":"[old password]",
    "newPassword":"[new password]"
}
```

变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
username | string | 用户名 | N
oldPassword | string | 旧的登陆密码 | N
newPassword | string | 新的登陆密码 | N

#### Response

Status Code:

码 | 描述
--- | ---
200 | 更改密码成功
401 | 更改密码失败

Body:
```
{
    "message":"[error message]",
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 返回错误消息，成功时为"ok" | N

## Logout-登出

#### URL：
POST http://[address]/auth/logout

#### Request

Headers:

key | 类型 | 描述
---|---|---
token | string | 访问token

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
200 | 登出成功
401 | 登出失败，用户名或token错误

Body:
```
{
    "message":"[error message]"
}
```
变量名 | 类型 | 描述 | 是否可为空
---|---|---|---
message | string | 返回错误消息，成功时为"ok" | N
