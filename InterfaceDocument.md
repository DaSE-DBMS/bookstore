# 一.接口描述
1. 接口连接：https://www.xxx.com/api/接口名称
2. 参数传递方式：POST方式
3. 签名规则：sign字段采用MDS加密方式
4. 返回格式json
5. 编码格式utf-8

# 二.注册登录类接口
1. Register-注册
提交URL：https://www.xxx.com/api/register

入参：
```
body={"params":{"loginName":"","loginPwd":"","terminalCode":""}}
```
传入变量

变量名 | 变量名称 | 类型 | 描述 | 是否可为空
---|---|---|---|---
loginName | 用户名 | String(20) | 用户名 | N
loginPwd | 登陆密码 | String(100) | 登陆密码 | N
terminalCode | 设备号 | String(50) | 终端编码 | N

返回参数

参数名 | 变量名称 | 类型 | 描述 | 是否可为空
---|---|---|---|---
result | 返回码 | String(1) | 0失败，1成功 | N
userId | 用户编号 | String(20) | 用户编号 | N
token | 会话token | String(50) | 会话标识 | N
errorMsg | 错误信息 | String(200) | 错误描述信息 | Y

2. login-登录接口
提交Url:https://www.xxx.com/api/login
入参：
```
body={"params":{"loginName":"","loginPwd":"","terminalCode":""}}
```
3. updatePwd-修改密码
4. logout-退出登陆
# 三.商品接口
1. getMerchant-查询商家接口，列出商家卖的全部商品
2. getProduct-查询商品接口
3. getProductSpecificationsList-查询商品规格参数列表接口，列出商品全部信息（文字+图片）
4. getBrandPresent-查询分类介绍接口，列出图书分类列表（英语/计算机/数学/...）
5. getMerchantList-查询商家接口-返回特定商品的商家信息
6. 其他接口...
# 四.订单接口
1. getMemberCart-查询购物车接口，返回购物车的购物项编号，总商品数，总商品金额
2. operateMemberCart-添加/删除购物车接口-对购物车商品进行增删操作
3. editMemberCart-编辑购物车接口，批量删除
4. createOrder-创建订单接口
5. orderPreview-订单预览接口
6. submitOrder-提交订单接口
7. paymentOrder-订单支付接口
8. getDetailOrder-订单详情接口
9. cancelOrder-订单取消接口
# 五.买家接口
1. getMemnberinfo-查询买家信息接口
2. editMemberInfo-修改买家信息接口
3. getMemberUsableMoney-查询买家可用钱（开始前给每位用户一个固定的积分，用来抵扣购物）
4. getMemberOrder-查询买家订单接口
5. getRefundOrder-售后处理-退货订单查询接口
6. returnsDetailOrder-售后处理-退货详情接口
7. refundsGoods-售后处理，退还货物接口
8. getMemberConsignee-查询用户收货地址接口
9. editConsignee-编辑用户收货地址接口
# 六.卖家接口
1. getmemberInfo-查询卖家信息
2. editMemberInfo-修改卖家信息接口
3. getMemberUsableMoney-查询卖家可用钱
4. getItem-查询可卖商品接口
5. editItem-编辑可卖商品接口
6. addItem-上架/下架商品接口
7. getSellItem-查询在售商品接口
8. getSoldItem-查询已卖出商品接口
9. getBuyerinfo-获取买家信息
10. getAwaitRefundItemOrder-查询等待退货的商品
11. getRefundItemOrder-查询正退货商品接口
12. sellerRefundGoods-查询卖家退货物流信息接口