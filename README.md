# bookstore
[![Build Status](https://travis-ci.com/DaSE-DBMS/bookstore.svg?branch=master)](https://travis-ci.com/DaSE-DBMS/bookstore)
[![codecov](https://codecov.io/gh/DaSE-DBMS/bookstore/branch/master/graph/badge.svg)](https://codecov.io/gh/DaSE-DBMS/bookstore)

## 功能
实现一个提供网上购书功能的网站后端。
网站支持书商在上面开商店，购买者可能通过网站购买。
买家和买家都可以注册自己的账号。
支持购物车->下单->付款->发货
具体功能见doc下面的.md接口描述（JSON接口）。

## 要求
1.实现对应接口的功能，见doc下面的.md文件描述
2.通过对应的性能和功能测试，所有test都pass
3.使用关系型数据库（PostgreSQL或MySQL数据库），blob存储可以分离出来存其它NoSQL数据库或文件系统

## 项目目录结构
```
bookstore
  |-- be                            mock backend
        |-- model
        |-- view
        |-- ....
  |-- doc                           API specification
  |-- fe                            frontend
        |-- access
        |-- bench                   performance test
        |-- data                    sqlite database(book.db)
        |-- test                    functionality test
        |-- ....
  |-- ....
```
## 下载book数据

同bookstore/fe/data/book.db的schema相同，但是有更多的数据(约3.5GB, 40000+行)

链接：

    https://pan.baidu.com/s/1bjCOW8Z5N_ClcqU54Pdt8g

提取码：

    hj6q
