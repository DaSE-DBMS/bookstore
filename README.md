# bookstore
[![Build Status](https://travis-ci.com/DaSE-DBMS/bookstore.svg?branch=master)](https://travis-ci.com/DaSE-DBMS/bookstore)
[![codecov](https://codecov.io/gh/DaSE-DBMS/bookstore/branch/master/graph/badge.svg)](https://codecov.io/gh/DaSE-DBMS/bookstore)

## 功能
实现一个提供网上购书功能的网站后端。<br>
网站支持书商在上面开商店，购买者可能通过网站购买。<br>
买家和买家都可以注册自己的账号。<br>
一个买家可以开一个或多个网上商店，
买家可以为自已的账户充值，在任意商店购买图书。<br>
支持下单->付款->发货->收货，流程。<br>

1.实现对应接口的功能，见doc下面的.md文件描述 （60%分数）<br>

其中包括：

1)用户权限接口，如注册、登录、登出、注销<br>

2)买家用户接口，如充值、下单、付款<br>

3)卖家用户接口，如创建店铺、填加书籍信息及描述、增加库存<br>
通过对应的功能测试，所有test case都pass <br>
测试下单及付款两个接口的性能（最好分离负载生成和后端），测出支持的每分钟交易数，延迟等 <br>

2.为项目添加其它功能 ：（40%分数）<br>

1)实现后续的流程 <br>
发货 -> 收货

2)搜索图书 <br>
用户可以通过关键字搜索，参数化的搜索方式；
如搜索范围包括，题目，标签，目录，内容；全站搜索或是当前店铺搜索。
如果显示结果较大，需要分页
(使用全文索引优化查找)

3)订单状态，订单查询和取消定单<br>
用户可以查自已的历史订单，用户也可以取消订单。<br>
取消定单（可选项，加分 +5~10），买家主动地取消定单，如果买家下单经过一段时间超时后，如果买家未付款，定单也会自动取消。 <br>

## 要求
1.可以扩展.md中的接口，但不要修改（字段可以多，不可以减少或修改参数名，减分项 -2\~5分），也不要修改test case（减分项 -2\~5分）。
测试程序如果有问题可以提bug （加分项，每提1个bug +2, 提1个pull request +5）。<br>

2.核心数据使用关系型数据库（PostgreSQL或MySQL数据库）。
blob数据（如图片和大段的文字描述）可以分离出来存其它NoSQL数据库或文件系统。 <br>

3.对所有的接口都要写test case，通过测试并计算代码覆盖率（有较高的覆盖率是加分项 +2~5）。 <br>

4.尽量使用正确的软件工程方法及工具，如，版本控制，测试驱动开发 （利用版本控制是加分项 +2~5）<br>

5.后端使用技术，实现语言不限；不要复制这个项目上的后端代码（不是正确的实践， 减分项 -2~5）<br>

6.不需要实现页面 <br>

7.最后评估分数时考虑以下要素：<br>
1）实现完整度，全部测试通过，效率合理 <br>
2）正确地使用数据库和设计分析工具，ER图，从ER图导出关系模式，规范化，事务处理，索引等 <br>
3）其它... <br>

8.3个人一组，做好分工，量化每个人的贡献度



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

### 安装配置
安装python (需要python3.6以上) 

安装依赖

    pip install -r requirements.txt


执行测试
    
    bash script/test.sh

 
 bookstore/fe/data/book.db中包含测试的数据，从豆瓣网抓取的图书信息，
 其DDL为：
 
    create table book
    (
        id TEXT primary key,
        title TEXT,
        author TEXT,
        publisher TEXT,
        original_title TEXT,
        translator TEXT,
        pub_year TEXT,
        pages INTEGER,
        price INTEGER,
        currency_unit TEXT,
        binding TEXT,
        isbn TEXT,
        author_intro TEXT,
        book_intro text,
        content TEXT,
        tags TEXT,
        picture BLOB
    );

   
更多的数据可以从网盘下载，下载地址为，链接：

    https://pan.baidu.com/s/1bjCOW8Z5N_ClcqU54Pdt8g

提取码：

    hj6q
    
这份数据同bookstore/fe/data/book.db的schema相同，但是有更多的数据(约3.5GB, 40000+行)




