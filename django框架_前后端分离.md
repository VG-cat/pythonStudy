

## 二、前后端分离

### 1、前后端分离流程

- 前端服务器[<font color=red>Nginx</font>]

  专门处理客户端的所有请求，返回html、css、js

- 后端服务器[<font color=red>Django</font>]

  专门负责数据返回[<font color=red>return JsonResponse()</font>]

- 流程

  1. 浏览器发起请求 ---> Nginx前端服务器
  2. Nginx服务器[<font color=red>/var/www/html/</font>]返回html ---> 浏览器
  3. HTML源码 ---> XHR请求到后端 ---> Django服务器数据查询
  4. Django服务器 将数据返回给浏览器
  5. 浏览器获取到数据后，进行数据渲染

### 2、前后端分离判定标准

- Django中是否使用模板层，分离后，相当于把cMTV中的T分离出去
- 视图函数中，返回 JsonResponse()

### 3、前后端分离优点

1. 各司其职，发挥各自特长
2. 后端可以灵活搭配各类前端[<font color=red>PC端、安卓、IOS端</font>]
3. 并发开发，提高开发效率

### 4、前后端分离带来的问题

1. 如何解决http无状态

   不分离时，使用Cookie和Session

   分离后，使用token[<font color=red>JWT</font>]

2. 如何解决跨域问题

   不分离时，使用jsonp[只能处理GET请求]

   分离后，使用跨域资源共享CORS

## 三、加密算法

### 1、BASE64

- 关于base64
  1. base64不是加密，只是编码
  2. base64编码后的长度，一定是4的倍数
  3. base64编码后的结果末尾可能有 0个、1个、2个 等于号
  4. base64编码和解码方法的 <font color=red>参数和结果都是字节串</font>
- 相关方法
  1. base64.b64encode("xxx".encode())
  2. base64.b64decode("xxx".encode())
  3. base64.urlsafe_b64encode("xxx".encode())
  4. base64.urlsafe_b64decode("xxx".encode())

### 2、SHA256

- hash三大特性

  定长输出、不可逆、雪崩

- hash算法的选择

  1. 如果加密的字符串用于<font color=red>存储</font>，使用md5
  2. 如果加密的字符串用于<font color=red>计算</font>，使用sha系列

- 使用示例

  ```python
  import hashlib
  
  # 1.创建加密对象
  # 2.使用加密算法进行加密
  # 3.获取加密结果[十六进制(hexdigest()) 二进制(digest())]
  
  s = hashlib.sha256()
  s.update("xxx".encode())
  s.hexdigest()
  ```

### 3、HMAC-SHA256

校验数据完整性和来源性

```python
import hmac

# key:公司密钥[bytes]
# msg:欲加密的字节串[bytes]
# digestmod:加密算法
hm = hmac.new(key, msg, digestmod="SHA256")
```

## 四、JWT

- 作用

  <font color=red>**会话保持**</font>

- JWT三大组成部分

  1. header

     指定加密算法和token类型：`{"alg": "HS256", "typ": "JWT"}`

     对以上字典进行base64的编码

  2. payload

     公有声明和私有声明：`{"exp": xxx, "iss": "xxx", "username": "xxx"}`

     <font color=red>对以上字典进行base64编码</font>

  3. sign

     `sign = hmac.new(key, "前两部分之和", digestmod="SHA256").hexdigest()`

     `sign = base.urlsafe_b64encode(sign.encode())`

- 需要注意细节

  1. json.dumps()

     separators=(",", ":")参数：指定多个kv之间的分隔符，及k和v之间的分隔符

  2. base64编码后的结果可能会有=，为了节约公司带宽，使用replase()方法将其去掉

## 五、PYJWT模块

- 在线安装

  1. Linux 

     `sudo pip3 install pyjwt -i pip源`

     **pip源**

     ```python
     1.阿里云 
     	http://mirrors.aliyun.com/pypi/simple/
     2.豆瓣
     	http://pypi.douban.com/simple/
     3.清华大学
     	https://pypi.tuna.tsinghua.edu.cn/simple/
     4.中国科学技术大学
     	http://pypi.mirrors.ustc.edu.cn/simple/
     5.华中科技大学
     	http://pypi.hustunique.com/
     ```

  2. Windows

     `python -m pip install pyjwt -i pip源`

     `cmd - 管理员身份打开cmd命令行 - 执行pip安装指令`

- 离线安装模块

  1. 官网下载安装包[xxx.tar.gz]

  2. 解压[tar -zxvf  xxx.tar.gz]

  3. 进入到解压的文件夹，找 <font color=red>setup.py文件</font>

     `sudo python3 setup.py install`

     如果没有setup.py，找 README.rst，找安装步骤

- 常用方法

  1. encode()生成token

     `token = jwt.encode(payload={},key="",algorithm="HS256")`

     <font color=red>**token是字节串**</font>

  2. decode()校验token

     `payload = jwt.decode(token=b'', key="", algorithms="HS256")`

     <font color=red>**payload是字典，里面是公有声明和私有声明**</font>

- jwt特点

  1. jwt模块非常强硬，一旦token校验失败，则抛出异常

  <font color=red>**未来在项目中一旦用到token校验，则一定要加try语句**</font>



## 一、跨域资源共享CORS

- 协商式跨域

  浏览器和服务器进行协商，浏览器告诉服务器它来自哪里，如果协商通过则允许跨域，否则不允许跨域

- 简单请求

  - 请求头：Origin
  - 响应头：Access-Control-Allow-Origin 浏览器只要拿到此头则跨域成功

- 预检请求

  1. OPTIONS请求阶段

     - 请求头

       Origin

       Access-Control-Request-Headers

       Access-Control-Request-Methods

     - 响应头

       Access-Control-Allow-Origin

       Access-Control-Allow-Headers

       Access-Control-Allow-Methods

  2. 主请求阶段

     - 请求头

       Origin

     - 响应头

       Access-Control-Allow-Origin

- Django配置cors跨域-settings.py

  - 添加cors应用

    `INSTALLED_APPS: corsheaders`

  - 添加cors中间件

    `MIDDLEWARES: corsheaders.middleware.CorsMiddleware`

  - 设置允许的域

    `CORS_ORIGIN_ALLOW_ALL = True | False`

    `CORS_ORIGIN_WHILELIST = ['', '', ...]`

  - 设置允许的头

    `CORS_ALLOW_HEADERS = ()`

  - 设置允许的方法

    `CORS_ALLOW_METHODS = ()`

## 二、前后端分离环境

### 1、搭建前端环境【Nginx】

- 安装Nginx：sudo apt-get install nginx

- 启动Nginx：sudo /etc/init.d/nginx  start | stop | restart | status | reload

- 配置文件[/etc/nginx/conf.d/dadashop.conf]

  `listen 7000   root /var/www/html`

- 拷贝前端文件

  `sudo mkdir /var/www/html/dadashop`

  `sudo cp client/.  /var/www/html/dadashop`

- <font color=blue>**有问题，看日志**</font>

  ```python
  1.nginx日志文件
    /var/log/nginx/error.log
  2.查看日志文件
    tail -50 /var/log/nginx/error.log
  3.根据错误日志去解决问题
  ```

### 2、搭建后端环境【Django】

- 创建项目：dashopt
- 数据库：dashopt
- 常规配置启动项目，配置cors跨域

## 三、前后端分离项目细节

- API文档已写好，所有的请求路由、请求体数据、响应格式，请查看API文档

- 响应数据的整体格式

  1. 正确响应

     `{"code": 200, "data": "xxx"}`

  2. 错误响应

     `{"code": 错误状态码, "error": "错误原因"}`

- 关于错误状态码

1. 用户模块：10100 - 10199

   10100：用户名已存在

   10101：用户名长度大于11位

   ... .... {"code": 10100, "error": "用户名已存在"}

2. 商品模块：10200 - 10299

3. 购物车模块：10300 -10399

4. 订单模块：10400 -10499

5. 支付模块：10500 -10599

## 四、RESTFUL API

- 一套规范，完全以入职后公司的风格为准，最大限度减少前后端沟通成本
- 规范
  1. 域名中尽量体现 api 字样
  2. API尽量名词化，避免出现动词
  3. 增加版本号
  4. 对资源动作操作，使用HTTP的METHODS来表示
     - GET : SELECT
     - POST : INSERT
     - PUT : UPDATE
     - DELETE : DELETE

   

## 一、DJANGO-REDIS

### 1、安装

`sudo pip3 install django-redis -i pip源`

### 2、使用流程

- settings.py中定义缓存配置项

  ```python
  CACHES = {
      # 1.邮件激活随机数
      "default": {
          "BACKEND": "django_redis.cache.RedisCache",
          "LOCATION": "redis://127.0.0.1:6379/1",
          # 默认过期时间未300秒,如果设置永久有效,设置为None
          "TIMEOUT": None,
          "OPTIONS": {
              "CLIENT_CLASS": "django_redis.client.DefaultClient",
              # Redis数据库服务器密码
              "PASSOWRD": "123456",
          }
      },
      # 2.短信验证码缓存配置项
      "sms": {
          "BACKEND": "django_redis.cache.RedisCache",
          "LOCATION": "redis://127.0.0.1:6379/2",
          # 默认过期时间未300秒,如果设置永久有效,设置为None
          "TIMEOUT": 300,
          "OPTIONS": {
              "CLIENT_CLASS": "django_redis.client.DefaultClient",
              # Redis数据库服务器密码
              "PASSOWRD": "123456",
          }
      },
      # 3.网站首页缓存配置项
      "goods_index": {},
      # 4.商品详情页缓存配置项
      "goods_detail": {}
  }
  ```

- 视图函数中直接调用即可

  1. 获取 **default** 缓存配置项

     `from django.core.cache import cache`

     `cache.set(key, value, expire)`

     `cache.get(key)`

     `cache.delete(key)`

     `cache.clear()`  清除当前库

  2. 获取 **所有** 缓存配置项

     `from django.core.cache import caches`

     `caches["sms"].set(key, value, expire)`

     `caches["sms"].get(key)`

     `caches["sms"].delete(key)`

     `caches["sms"].clear()`

- django_redis操作复杂的数据类型

  ```python
  from django_redis import get_redis_connection
  
  r = get_redis_connection()
  r.hset(key, field, value)
  r.sadd(key, member)
  r.lpush(key, element)
  r.brpop(key, timeout)
  ```

## 二、达达商城邮件激活功能会议

时间：2022年1月22日 09:30分

地点：快乐编程大厦1016室

参会人员：产品经理、前端工程师、后端工程师



### **1、流程思考**

1. 用户点击注册，发送激活邮件给用户邮箱，邮件内容必须有激活链接

  2. 用户点开收件箱，点击激活链接，跳转到 激活页面
  3. 激活页面中，用户点击 是，向后端XHR请求，后端更新该用户is_active的值

### **2、具体细节思考[责任划分]**

1. 发邮件【后端】：from django.core.mail import send_mail

2. 激活链接【前端】

   http://127.0.0.1:7000/dadashop/templates/active.html

3. 激活页面【前端】

   active.html

4. 【后端】用户点击 是，发送请求到后端，后端视图函数中 更新is_active



### **3、如何加入用户标识**

激活链接中通过查询字符串添加用户标识

http://127.0.0.1:7000/dadashop/templates/active.html?code=xxxx

**方案1：**code=zhaoliying     # 明文，不太安全

**方案2：**code=base64.urlsafe_b64encode(b"zhaoliying")  # 相对好一些

**方案3：**code=base64.urlsafe_b64encode(b"1016_zhaoliying")



### 4、随机数缓存到Redis

随机数存储到redis数据库并设置有效期3天：

`set avtive_email_zhaoliying  1016`

## 三、DJANGO发送邮件

### 1、业务场景

- 业务邮件告警
- 邮件激活验证
- 找回密码

### 2、收发邮件的三个协议

1. SMTP：发邮件协议【推送型协议】

2. IMAP：收邮件协议【拉取型协议】

   摘要浏览功能，客户端和邮件服务器交互，比如星标邮件、拉取部分内容等

3. POP3：收邮件协议【拉取型协议】

   单向协议

### 3、Django配置发送邮件

- 给django授权一个邮箱，作为邮件客户端

  1. 获取qq邮箱授权码

     `QQ邮箱->设置->帐户->“POP3/IMAP......服务`

  2. settings.py中相关配置

     ```python
     EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # 固定写法
     EMAIL_HOST = 'smtp.qq.com' # 腾讯QQ邮箱 SMTP 服务器地址
     EMAIL_PORT = 25  # SMTP服务的端口号
     EMAIL_HOST_USER = '***'  # 发送邮件的QQ邮箱
     EMAIL_HOST_PASSWORD = '***'  # 在QQ邮箱->设置->帐户->“POP3/IMAP......服务” 里得到的在第三方登录QQ邮箱授权码
     EMAIL_USE_TLS = True  # 与SMTP服务器通信时，是否启动TLS链接(安全链接)默认false
     ```

- 直接调用django封装的接口即可

  ```python
  from django.core.mail import send_mail
  
  send_mail(subject="邮件标题", message="文本内容", from_email="发件人", recipient_list=["收件人列表"], html_message="html")
  ```




## 一、DJANGO和CELERY结合

- celery定义

  简单、灵活、可靠的处理大量消息的分布式系统

- 核心组件

  1. **Django**：生产者，Django 中生产一些阻塞任务【异步任务】
  2. **broker**：消息中间件【存储异步任务】- Redis | RQ
  3. **worker**：消费者，执行异步任务
  4. **backend**：存储异步任务执行结果，一般不到万不得已不使用

- 使用流程

  1. 创建celery配置文件【和settings.py同路径】

     ```python
     import os
     from celery import Celery
     from django.conf import settings
     
     # 1.设置环境变量
     # 2.初始化celery应用
     # 3.设置自动发现django项目中的异步任务
     
     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dashopt.settings")
     app = Celery("dashopt", broker="", backend="")
     app.autodiscover_tasks(settings.INSTALLED_APPS)
     ```

  2. 在应用下创建tasks.py【存放异步任务】

     ```python
     from dashopt.celery import app
     
     @app.task
     def async_xxx(xx,xx):
         pass
     ```

  3. 视图函数中调用异步任务【delay(参数1, 参数2)】

     ```python
     from .tasks import async_xxx
     
     async_xxx.delay(xx, xx)
     ```

  4. 终端启动celery

     `celery -A dashopt worker -P gevent -c 1000 -l info`

- 并发模型

  - 默认使用多进程[prefork]

    `celery -A 项目名 worker -l info`

  - 使用协程[gevent]

    `celery -A 项目名 worker -P gevent -c 1000 -l info`

  <font color=orange>**1000为协程数量，生产环境一般1000-2000不等**</font>

  <font color=orange>**如果使用多进程，则进程数量和CPU核数保持一致**</font>

- 生产环境后台启动

  `nohup celery -A 项目名 worker -P gevent -c 1000 > celery.log 2>&1 &`

## 二、FBV和CBV

### 1、定义

- FBV

  函数视图，Function Base View

- CBV

  类视图，Class Base View

### 2、关于CBV

- 应用场景

  一个路由提供多种HTTP请求方法时，使用类视图，类视图更符合RESTFUL语义

- CBV优点

  1. 代码可读性好
  2. 类视图对于函数视图有更高的复用性，如果项目中的其他功能模块需要用到某个类视图中的某个特定功能逻辑时，直接继承该类即可

- CBV使用流程

  1. views.py中定义视图类[<font color=green>**继承View**</font>]

     ```python
     # 继承django中的View,会进行方法的转发
     from django.views import View
     
     class XxxView(View):
         def get(self, request):
             pass
     ```

  2. urls.py中匹配路由[<font color=green>**as_view()**</font>]

     ```python
     path("xxxx", views.XxxView.as_view())
     ```

- 注意

  <font color=green>**类视图中，如果发了请求，但是在类视图中没有对应的方法时，会返回405的状态码**</font>

   

## 一、抽象模型类

- 作用

  用来归纳一些公共属性字段，为普通模型类补充字段

- 使用示例

  ```python
  from django.db import models
  
  class BaseModel(models.Model):
    	created_time = xxx
      updated_time = xxx
      
      class Meta:
        	abstract = True
  ```

## 二、CBV之dispatch()方法

- django的类视图[CBV]中，所有过来的请求都会经过 Django.views.View 中的 dispatch()方法进行分发

- 可以通过重写dispatch()方法，实现一些权限的校验，比如校验登录状态token等

- 示例

  ```python
  from django.views import View
  
  class XxxView(View):
    	def dispatch(self, request, *args, **kwargs):
        	# 1.通用逻辑、校验逻辑 
          # 2.执行原有的分发逻辑 super()
          return super().dispatch(request, *args, **kwargs)
        
      def get(self, request):
        	pass
  ```

path('user/\<str:username\>')   username会作为参数传入

## 三、mysql事务

### 1、事务四大特性

- 原子性：事务中的各个操作要么全都执行，要么全都不执行
- 一致性：数据库必须从一个一致性的状态转为另一个一致性的状态
- 隔离性：每个事务之间的操作是互相隔离的
- 持久性：一旦对数据库数据做了修改，则修改是永久性的

### 2、事务支持

- MySQL命令行

  1. 开启事务：mysql> begin;  |  start transaction;
  2. 提交事务：mysql> commit;
  3. 事务回滚：mysql> rollback;

- Django事务支持

  模块：**from django.db import transaction**

  1. 开启事务

     **with transaction.atomic():**

  2. 创建存储点

     **sid = transaction.savepoint()**

  3. 事务中的各个操作  

  4. 提交事务

     **transaction.savepoint_commit(sid)**

  5. 回滚事务

     **transaction.savepoint_rollback(sid)**

## 四、requests模块

### 1、介绍

- 定义

  非常优秀的第三方请求模块，支持多种HTTP请求方式，

  在开发中经常用来做单元测试；

  在数据获取中经常用来做爬虫。

- 安装

  `sudo pip3 install requests`

- 常用方法

  1. requests.get(url="http://www.baidu.com/", headers={})
  2. requests.post(url="URL地址", json={} , headers={})
  3. requests.put(url="URL地址", json={}, headers={})
  4. requests.delete(url="URL地址", json={}, headers={})

- 参数

  - url : 请求URL地址
  - json = {} ：请求体数据，request.body  ---->  {"username": xxx, "password": xxx}
  - data = {} ：请求体数据，request.body ----> "username=xxx&password=xxx"
  - headers = {} ：请求头 {"authorization": "xxxxxxx"}

- 响应对象的属性

  - resp.text  ：获取响应内容 - 字符串
  - resp.json() ：获取响应内容，自动将json格式的字符串转为python对象【等价于json.loads()】
  - resp.content ：获取响应内容 - 字节串
  - resp.status_code ：http响应码

- 示例

  1. POST测试登录功能

     ```python
     """
         测试达达商城登录功能
         请求地址：http://127.0.0.1:8000/v1/tokens
         请求方式：POST
         请求体： {"username":xxx, "password":xxx, "carts":xx}
     """
     
     import requests
     
     url = "http://127.0.0.1:8000/v1/tokens"
     data = {
         "username": "zhaoliying",
         "password": "123456",
         "carts": 0
     }
     
     resp = requests.post(url=url, json=data)
     
     print(resp.json())
     ```

  2. GET测试地址查询功能

     ```python
     import requests
     
     
     url = "http://127.0.0.1:8000/v1/users/zhaoliying/address"
     headers = {
         "authorization": "自己的token",
     }
     
     html = requests.get(url=url, headers=headers).json()
     print(html)
     ```

  3. DELETE请求测试地址删除功能

     ```python
     import requests
     
     
     url = "http://127.0.0.1:8000/v1/users/zhaoliying/address/3"
     data = {"id": "3"}
     headers = {
         "authorization": "自己的token",
     }
     
     html = requests.delete(url=url, json=data, headers=headers).json()
     print(html)
     ```


   

## 一、第三方网站对接流程

- 注册平台开发者账号，查看接口文档
- 依据接口文档的详细步骤，编写对接该平台的接口[utils/sms.py]
- 项目业务逻辑中，直接调用该接口即可

## 二、达达商城短信验证码实现

### 1、短信验证码发送

- 注册页面[register_sms.html]，点击发送短信验证码
- 后端路由分布式路由[v1/users/sms/code]，对应视图
- 视图函数中思路
  - 获取请求体的数据[手机号]
  - 先到Redis中确认3分钟之内是否发过
    1. 未发过：则直接调用短信平台接口发送短信，发送完成后将验证码存入Redis中，一个有效期设置为3分钟用来控制频率，另一个有效期设置为10分钟控制短信验证码有效期
    2. 发过：直接返回

### 2、短信验证码校验

- 前端页面输入注册信息，点击提交注册信息，发送XHR请求到后端
- 后端视图[校验]
  - 获取请求体数据[短信验证码]
  - 和Redis中存储的验证码[600秒]对比校验[注意数据类型问题]

## 三、容联云短信平台对接

### 1、接口文档

#### 1.1 请求URL地址：url参数

- URL地址：https://app.cloopen.com:8883/2013-12-26/Accounts/{}/SMS/TemplateSMS?sig={}
  - accountSid: 控制台获取
  - **Sig**：md5(账户id + 授权令牌 + 时间戳)

#### 1.2 请求头：headers参数

- headers

  Accept:application/json;

  Content-Type:application/json;charset=utf-8;

  Content-Length:256; 

  **Authorization**:  base64(账户id + 冒号 + 时间戳)

#### 1.3 请求体：json参数

- to ：接收短信的手机号
- appId ：官网控制台获取
- templateId ：短信模板id，测试模板为 1
- datas ：【替换模板短信中的 {}, 比如 短信验证码、几分钟内正确输入】

<font color=red>**requests.post(url=url, headers=headers, json=data)**</font>

## 四、MySQL常见面试题

### 1、说几条常用的Linux命令

- ps -aux  
- kill
- chmod
- chown
- ping
- grep
- df -h :查看磁盘使用情况

### 2、介绍MySQL的引擎

- InnoDB

  MySQL中默认的存储引擎，支持外键、支持事务和事务回滚、支持行级锁，写操作多的表一般使用InnoDB引擎

- MyISAM

  不支持外键，支持表级锁[读锁和写锁]，读操作多的表使用MyISAM存储引擎

- MEMORY

  表记录存储在内存中，一旦主机重启或服务重启，数据丢失，一般临时表或中间表可以使用MEMORY

### 3、数据库和数据仓库的区别

- 数据体量

  从数据量上来说，数据库的数据体量和数据仓库根本不在一个层级，数据仓库存储的是海量数据，数据量以TB级别开始算

- 数据来源

  数据仓库中的数据由多种异构数据源组成，比如数据库中数据、网络爬虫数据、网络日志... ...

- 技术工具

  数据库：MySQL、Oracle、MongoDB、Redis ... ...

  数据仓库：Java、Hadoop、Hive、HBase、Spark、Storm ... ...

- 应用场景

  数据库更加侧重于数据存储；

  数据仓库更加侧重于数据分析和数据挖掘

   

## 一、OAuth2.0授权协议

- 定义

  第三方授权协议

- 授权交互模式

  - **授权码模式**
  - 应用授信模式
  - 用户授信模式
  - 简化模式

  <font color=red>**其中授权码模式被广泛应用于互联网开放平台，通过第三方登录是最常见的应用场景**</font>

   

## 一、数据库三范式

### 1、意义

尽全力减少数据的冗余

### 2、三范式-3NF

- 1NF

​	拆字段，字段是最小的粒度不能再拆分，比如：地址表中拆地址

- 2NF

​	拆表，满足1NF，表中的字段必须依赖于全部主键而非部分主键，

​	比如：商品表中商品的id和分类的id是复合主键，但是分类名仅仅依靠分类id就能索引到，所以将其拆分为 商品表、分类表、定价表

- 3NF

​	拆表，满足2NF，表中非主键字段之间不能有传递性依赖，

​	比如：商品表中仓库负责人依赖于仓库，拆表，将商品表拆分为 商品表 和 仓库表

### 3、反范式

- 定义

  适当增加数据冗余，多张表中冗余相同的字段，比如销量、地址等

- 意义

  - 适当的冗余增加查询效率[冗余销量字段]
  - 适当的冗余可以保证数据真实性[订单表冗余地址相关字段]

## 二、电商网站相关名词

- SPU：标准化产品单元
- SKU：库存量单位
- 销售属性名：比如 颜色、尺寸... ...
- 销售属性值：比如 中国红、可可茶金、16寸... ...
- 规格属性名：比如 产地、毛重... ...
- 规格属性值：比如 中国香港、200g... ...

## 三、数据导入和导出

### 1、导出[备份]-dumpdata

备份模型实例和数据库

- 备份所有数据

  `python3 manage.py dumpdata > xxx.json`

- 备份指定应用数据

  `python3 manage.py dumpdata 应用名 > xxx.json`

- 备份指定应用指定表数据

  `python3 manage.py dumpdata 应用名.表名 > xxx.json`

### 2、导入[恢复]-loaddata

`python3 manage.py loaddata xxx.json`

## 四、商品模块首页展示

- 应用名：goods

- 配置图片类请求路由

  - 表中字段数据类型[存储图片在服务器上的路径]

    `models.ImageField(upload_to="sku")`

  - 配置路由

    ```python
    from django.conf import settings
    from django.conf.urls.static import static
    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    # settings.py
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
    ```

- 项目中创建media文件夹，并把对应商品图片拷贝到此目录

- 查看接口文档，配置路由，完成视图函数

  数据查询[ORM查询]

## 五、首页缓存配置

使用django自带的缓存装饰器

1. 独立缓存区域

   ```python
   urlpatterns = [
       path("index", cache_page(300, cache="goods_index")(views.XxxView.as_view())),
   ]
   ```

2. settings.py中配置缓存配置项

   ```python
   CACAHES = {
       "goods_index": {
           "LOCATION": "redis://127.0.0.1:6379/2"
       }
   }
   ```

3. admin.py高级管理类

   ```python
   from django.core.cache import caches
   
   INDEX_CACHE = caches["goods_index"]
   
   @admin.register(SKU)
   class XxxAdmin(admin.ModelAdmin):
       def save_model(self, request, obj, form, change):
           super().save_model(request,obj, form, change)
       	# 清除首页缓存
           INDEX_CACHE.clear()
           
       def delete_model(self, ...):
           super().delete_model(request,obj...)
       	# 清除首页缓存
           INDEX_CACHE.clear()
   ```

   <font color=red>**在admin后台进行增删改数据时，admin.ModelAdmin中的save_model()方法和delete_model()方法会被调用，所以我们通过重写这两个方法，实现在增删改数据时进行整个缓存数据库的清除flushdb**</font>

4. 创建管理员用户并测试

   ```python
   python3 manage.py createsuperuser
   http://127.0.0.1:8000/admin/
    
   # 对sku中的数据进行增删改操作
   ```

## 六、关于缓存压缩

- 说明

  django自带的缓存装饰器并没有开放出压缩接口，故使用django-redis组件进行压缩，来节约内存

- 使用

  ```python
  # settings.py
  CACHES = {
      "default":{},
      "goods_index":{
          "OPTIONS":{
              "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor"
          }
      }
  }
  ```

   

## 一、详情页模型类梳理

- 类1：Catalog表

  catalog.name

- 类2：SKU表

  标题：name

  图片：default_image_url

  副标题：caption

  价格：price

- 类3：SPUSaleAttr

  销售属性名id：id

  销售属性名：name

- 类4：SaleAttrValue

  销售属性值id：id

  销售属性值名字：name

- 类5：SPUSpec

  规格属性名id：id

  规格属性名：name

- 类6：SPUSpecValue

  规格属性值id：id

  规格属性值名字：name

- 类7：SPUImage

  详情页图片路径：image

## 二、各种类型装饰器

1. 普通函数装饰器

   ```python
   def xxx(func):
       def wrapper(*args, **kwargs):
           return func(*args, **kwargs)
       return wrapper
   ```

2. 视图函数装饰器

   ```python
   def xxx(func):
       def wrapper(request, *args, **kwargs):
           return func(request, *args, **kwargs)
       return wrapper
   ```

3. 类视图函数装饰器

   ```python
   def xxx(func):
       def wrapper(self, request, *args, **kwargs):
           return func(self, request, *args, **kwargs)
       return wrapper
   ```

4. 可传参的装饰器

   ```python
   def cache_check(**cache_kwargs):
       def _cache_check(func):
           def wrapper(self, request, *args, **kwargs):
               return func(self,request,*args,**kwargs)
           return wrapper
       return _cache_check
   ```

   

## 一、购物车模块功能会议

### 1.参会人员

​	产品经理、后端工程师、前端工程师、测试工程师

### 2.会议主题

​	达达商城购物车模块功能实现

### 3.会议纪要

- 实现功能

  添加购物车、查询购物车、修改购物车、删除购物车、数据合并、全选、取消全选、单选、取消单选... ..

### 4.需要思考的问题

1. **购物车数据特点**

   - 数据量较大
   - 价值相对较低
   - 访问频率不低

2. **数据存储问题**

   - MySQL数据库

     根据购物车数据的特点，决定把MySQL数据库留给更重要的功能模块，比如用户模块、订单模块... ...，购物车数据不使用MySQL，使用Redis数据库作为永久存储

   - Redis数据库

     1. Redis基于内存，速度快

     2. 考虑数据安全性，尽量不能丢失任何数据

        ```python
        1.考虑Redis数据持久化的方式
          方式一：RDB
            	save 900 1
        		save 300 10
        		save 60 10000
          方式二：AOF【选择】 策略 appendfsync always
        		appendfsync always # 基本不丢失数据
        		appendfsync everysec # 最多丢失一秒
        		appendfsync no # 丢失数量不一定
                
        		# 重写appendonly.aof文件策略
                auto-aof-rewrite-percentage 100
        		auto-aof-rewrite-min-size 64mb
        ```

     3. 数据结构存储设计

        ```python
        1.购物车中都存储哪些数据
          用户id：user_id
          商品id：sku_id
          数量：  count
          选中状态：1 | 0
        
        2.何种数据类型？
          2.1 字符串
              # 方案
                user_id: {
                    "sku_id1": [5,1],
                    "sku_id2": [8,0],
                    "sku_id3": [2,1]
                }
                
          2.2 列表【消息队列】
          2.3 哈希
              HSET user_id  sku_id  [5,1]
              HSET user_id  sku_id  [8,0]
              哈希的优势在于针对性提取，但是购物车中的数据一般都是查看所有，很少要针对性提取某一个购物车商品
          2.4 集合【共同关注、共同好友、增量爬虫、分布式爬虫】
          2.5 有序集合【排行榜】
        ```


## 二、添加购物车模块

- 商品详情页 - 选择商品数量 - 点击加入购物车

- 路由 - 分布式路由 - 视图[POST]

  请求体数据：`{"sku_id": 1, "count": 5}`

- 后端视图逻辑

  1. 获取请求体数据
  2. 将该商品信息存入Redis数据库
  3. 返回购物车中商品种类的数量

## 三、查询购物车模块

- 仔细分析前端所需数据，确认数据来源【Redis、MySQL】
- MySQL层面的ORM查询一定要结合 **ER图** 和 模型类

## 四、购物车数据合并

- 离线添加购物车[<font color=red>**非登录状态**</font>]

  商品详情页 - 加入购物车 - 将商品数据存入**浏览器本地存储**中[{},{}]

- 在线添加购物车[<font color=red>**登录状态**</font>]

  数据存入Redis数据库

- <font color=red>**数据合并**</font>

  - 第一份数据：浏览器本地存储

  - 第二份数据：Redis数据库中的数据

  - 合并

    用户在登录或者新用户注册时，将离线购物车数据提交给后端，后端将其和该用户Redis中的数据进行合并

  <font color=red>**注意:写程序时，主体逻辑写dtoken应用或user应用下，获取Redis中购物车数据及具体合并的代码写在了carts应用下**</font>

   

## 一、订单模块

### 1、确认订单页

- 订单模块流程
  1. 购物车点击 <font color=red>**去结算**</font> |  详情页点击 <font color=red>**立即购买**</font>
  2. 订单确认页 [<font color=red>**显示地址及商品信息，并未创建订单**</font>]
  3. 订单确认页中点击 确认并付款 [<font color=red>**创建订单**</font>]
  4. 支付宝支付
- 确认订单页两个链条
  1. 购物车 - 去结算 - 订单确认页【地址、商品】
  2. 详情页 - 立即购买 - 订单确认页【地址、商品】

### 2、生成订单

**生成订单**

```python
1.链条一[settlement_type=0]
  购物车 - 去结算 - 确认并付款 - 生成订单
2.链条二[settlement_type=1]
  详情页 - 立即购买 - 确认并付款 - 生成订单
    
# 购物车链条
1、订单表中插入数据
2、订单商品表中插入数据
3、更新sku的库存和销量
4、删除购物车中已转化为订单的商品数据
```

**订单模块数据表**

```python
1.表1：订单表
  订单编号、订单总金额、支付方式、运费... ...

    订单编号      总金额     外键用户
   202202091111   6000        1
   202202091118   3000        2
    
2.表2：订单商品表
    
    sku_id  数量    价格    订单编号
    666     1     3000    202202091111
    888     3     900     202202091111
    999     10    2100    202202091111
    666     1     3000    202202091118
```

### 3、订单模块数据表

- **数据表详情**

  1. 订单表[OrderInfo]
  2. 订单商品表[OrderGoods]
  3. 关系
     - 用户表和订单表---> 1:n 【一个用户有多个订单】
     - 订单表和订单商品表---> 1:n 【一个订单有多个商品】
     - SKU表和订单商品表 ---> 1:n 【1个SKU商品可能在多个订单商品中出现】

- **订单表和订单商品表细节**

  1. 订单编号[order_id]

     不使用自增id作为订单编号，因为订单表数据量庞大，为了高扩展，会由不同的MySQL数据库专门维护订单表，如果使用自增的id作为订单编号，维护成本较高，所以一般使用 **时间戳+用户id** 作为订单编号

  2. 合理冗余字段【数据库反范式】

     订单表中冗余地址相关字段，避免数据失真

     订单商品表中冗余价格字段，增加查询效率

  3. choices参数

     - 应用场景

       需要创建一个有固定值的字段，可使用此参数

       性别：choices = ( (1, "男"), (2, "女") )

       订单状态：choices = ( (1, "待付款"), (2, "待发货"), (), () )

     - 优点

       当数据量庞大时，大大减少数据库存储的压力

       admin后台管理人员操作起来更加方便，避免工作失误

### 4、确认订单页

- Redis中查询商品【sku_id】
- MySQL中查询数据：利用sku_id

### 5、生成订单

- 订单表中插入数据
- 更新SKU的库存和销量
- 订单商品表中插入数据

<font color=red>**使用事务transaction**</font>

## 二、Redis分布式锁

- 场景

  当多个进程需要互斥的访问共享资源时，Redis分布式锁是一种非常有效的技术手段

- 执行步骤

  1. 多个进程先到Redis数据库中获取分布式锁，锁只有一把
  2. 获得锁的进程操作共享资源，操作完成后释放锁，其他进程继续获取锁

- 实现原理

  - 获取锁原理

    `set key value nx ex timeout`

  - 释放锁原理

    `del key`

- Python实现分布式锁

  ```python
  import redis
  
  pool = redis.ConnectionPool(host="127.0.0.1", port=6379, db=0)
  r = redis.Redis(connection_pool=pool)
  
  with r.lock("key", blocking_timeout=5) as lock:
      # 操作共享资源[数据库]
      pass
  ```

   

## 一、支付模块

### 1、加密

#### 1.1 对称加密

- 对称加密

  加密过程和解密过程使用同一把钥匙，所以叫做对称加密

- 特点

  钥匙只有一把，不太安全，一旦密钥泄露，则加密的信息不安全

#### 1.2 非对称加密

- 非对称加密

  两把钥匙，公钥和私钥[<font color=red>**成双成对**</font>]，一个公钥一定对应着唯一的私钥

- 说明

  1. 如果用公钥对数据进行加密，则此公钥对应的私钥才能解密
  2. 如果用私钥对数据进行加密，则此私钥对应的公钥才能解密

- 常见非对称加密算法

  RSA、DSA、ECC ... ...

- 应用场景

  1. 加密和解密：公钥加密，私钥解密

  2. 签名和验签：验证消息来源

     私钥签名，公钥验签


### 2、支付宝相关接口

- 1.初始化alipay对象

  ```python
  from alipay import Alipay
  
  alipay = AliPay(
      # 应用id,控制台获取
      appid=settings.ALIPAY_APP_ID,
      # 异步通知地址-必须为公网地址[POST请求]
      app_notify_url=None,
      # 应用私钥[用于签名]
      app_private_key_string=app_private_key_string,
      # alipay公钥[验签-验证消息来源]
     alipay_public_key_string=alipay_public_key_string,
      # 签名使用算法
      sign_type="RSA2",
      # 默认False[生产环境], 设置为True[沙箱环境]
      debug=True
  )
  ```

- 2.获取支付链接

  - API文档：[alipay.trade.page.pay](https://opendocs.alipay.com/open/028r8t?scene=22)

  - alipay模块接口：**api_alipay_trade_page_pay()**

  - 返回值：**查询字符串**

    ```python
    alipay.api_alipay_trade_page_pay(
        # 订单标题
        subject=order_id,
        # 订单编号
        out_trade_no=order_id,
        # 总金额
        total_amount=total_amount,
        # 同步通知地址[GET]
        return_url=settings.ALIPAY_RETURN_URL,
        # 异步通知地址-公网IP[POST]
        notify_url=settings.ALIPAY_NOTIFY_URL
    )
    ```

- 3.验签接口

  - API文档：[异步通知验签](https://opendocs.alipay.com/open/270/105902#s7)

  - alipay模块接口：**verify()**

  - 返回值：True | False

    ```python
    alipay.verify(request_data, sign)
    
    # 参数request_data：请求体数据
    # 参数sign：签名[请求体]
    ```

- 4.主动查询接口

  - API文档：[alipay.trade.query](https://opendocs.alipay.com/open/028woa)

  - alipay模块接口：**api_alipay_trade_query()**

  - 返回值：Json

    ```python
    alipay.api_alipay_trade_query(
        out_trade_no=out_trade_no,
        trade_no=trade_no
    )
    
    # 参数out_trade_no：商户订单编号
    # 参数trade_no：支付宝交易号
    # 两个参数支付宝发送GET请求时在查询字符串中
    ```

### 3、相关URL地址

1. **returnUrl**

   同步通知URL地址，GET请求，同步返回参数，**无具体支付结果**

   查询参数中，有订单编号、sign、订单金额等信息，用于主动查询获取支付结果

2. **notifyUrl**

   <font color=red>**异步通知URL地址，POST请求，异步返回参数，有具体支付结果**</font>

   在请求体中[request.POST]，有具体该订单的交易状态，还有签名[<font color=red>**必须验签**</font>]、<font color=red>**必须为公网地址**</font>

### 4、第三方支付流程[Alipay]

1. 商户系统调用 [alipay.trade.page.pay](https://opendocs.alipay.com/open/028r8t?scene=22)（统一收单下单并支付页面接口）向支付宝发起支付请求，支付宝对商户请求参数进行校验，而后重新定向至用户登录页面
2. 用户确认支付后，支付宝通过 get 请求 returnUrl（商户入参传入），返回同步返回参数
3. 交易成功后，支付宝通过 post 请求 notifyUrl（商户入参传入），返回异步通知参数
4. 若由于网络等原因，导致商户系统没有收到异步通知，商户可自行调用 [alipay.trade.query](https://opendocs.alipay.com/open/028woa)（统一收单线下交易查询）接口查询交易以及支付信息（商户也可以直接调用该查询接口，不需要依赖异步通知）

### 5、需要注意细节

1. 由于同步返回的不可靠性，支付结果必须以异步通知或查询接口返回为准，不能依赖同步跳转
2. 商户系统接收到异步通知以后，必须通过验签（验证通知中的 sign 参数）来确保支付通知是由支付宝发送的。详细验签规则请参见 [异步通知验签](https://opendocs.alipay.com/open/270/105902#s7)
3. 接收到异步通知并验签通过后，请务必核对通知中的 app_id、out_trade_no、total_amount 等参数值是否与请求中的一致，并根据 trade_status 进行后续业务处理
4. 在支付宝端，partnerId 与 out_trade_no 唯一对应一笔单据，商户端保证不同次支付 out_trade_no 不可重复；若重复，支付宝会关联到原单据，基本信息一致的情况下会以原单据为准进行支付







# 快速搞定环境

## 一、模块安装及文件拷贝

- 安装django-redis组件

  ```python
  sudo pip3 install django-redis
  ```

- 拷贝前端文件

  ```python
  1.将前端文件夹client拷贝到用户主目录下 /home/tarena/
  
  2.拷贝到nginx目录下：/var/www/html
    sudo mkdir /var/www/html/dadashop/
        sudo cp -fr client/.  /var/www/html/dadashop/
  ```

## 二、配置并重启Nginx

- sudo vim /etc/nginx/conf.d/dadashop.conf

  ```nginx
  server {
          
          listen 7000 default_server;
          listen [::]:7000 default_server;
          server_name __;
  
          root /var/www/html;
          # Add index.php to the list if you are using PHP
          index index.html index.htm index.nginx-debian.html;
  
          location / {
                  # First attempt to serve request as file, then
                  # as directory, then fall back to displaying a 404.
                  try_files $uri $uri/ =404;
          }
  }
  ```

- 重新启动nginx

  ```python
  sudo /etc/init.d/nginx restart
  ```

## 三、配置数据库

- 建库

  ```mysql
  create database dashopt default charset utf8;
  ```

- 删除项目迁移文件

  - user应用下的迁移文件
  - goods应用下的迁移文件

- 同步数据库

  ```linux
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```

## 四、测试

### 1、启动项目

```python
python3 manage.py runserver
```

### 2、启动celery

```python
celery -A dashopt worker --loglevel info
```

### 3、访问主页

```python
http://127.0.0.1:7000/dadashop/templates/index.html  
```

### 4、注册用户

```python
http://127.0.0.1:7000/dadashop/templates/register_sms.html
```

















