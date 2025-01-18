## 简介

是一个python web框架和异步网络库，通过使用非阻塞网络I/O，可以扩展到数以万计的开放连接，适合实时长轮询，长期连接

![](./images/Snipaste_2025-01-04_17-15-22.png)

Flask 适合小型项目和快速原型开发，

Django 适合大型、功能全面的 Web 应用，

Tornado 适合需要高并发和实时通信的应用。

## 安装

pip install tornado

![](./images/Snipaste_2025-01-08_13-06-57.png)

## 处理请求和上传文件

```
import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

# 处理get和post请求
class LoginHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        # uname = self.get_argument('uname')
        self.render("template/login.html")
        uname = self.get_query_argument('uname')

    def post(self,*args,**kwargs):
        # uname = self.get_argument('uname')
        uname = self.get_body_argument('uname')


# 上传文件
class UploadHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render("template/uploadfile.html")


    def post(self,*args,**kwargs):

        print(self.request.files)
        imgs = self.request.files['image1']

        for img in imgs:
            filename = img['filename']
            body = img['body']
            content_type = img['content_type']

            with open(os.path.join(os.getcwd(),'files',filename), 'wb') as f:
                f.write(body)
		# 设置响应头
        self.set_header('Content-Type',content_type)
        self.write(body)
        
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/login/", LoginHandler),
        (r"/upload", UploadHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
```

## 请求对象和响应对象

```
self.request:  self.request.uri.....

响应信息一般做设置

self.set_header('Content-Type',content_type)  # 设置响应头

self.set_header('Location','www.baidu.com')  # 直接调整百度

self.set_status(200)

self.write(body)  # 设置响应体
```

## 连接数据库

```
def _getconn():
    return sqlite3.connect('test.db')
    
class RegisterHandler(tornado.web.RequestHandler):
	# 接收参数
    def initialize(self,conn):
        self.conn = conn

    def get(self,*args,**kwargs):
        try:
            cursor = self.conn.cursor()
            cursor.execute("select * from users")
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            
def make_app():
    return tornado.web.Application([
        (r"/register", RegisterHandler,{'conn':_getconn()}),
    ])
```

## 重定向

```


class IndexHandler(tornado.web.RequestHandler):
  
    def get(self,*args,**kwargs):
    	# 方式一
    	self.set_status(302)
        self.set_header('Location','www.baidu.com')  # 重定向到百度
        
        #方式二
        self.redirect('www.baidu.com')
     
     def write_error(self):
     		pass
        

def make_app():
    return tornado.web.Application([
        (r"/index", IndexHandler),
        (r"/index2", tornado.web.RedirectHandler,{'url':'www.baidu.com'}), # 方式三
    ])   

```

## cookie

```
# 普通设置
self.set_cookie('uname','lisi',expires_days=3)
# 加密设置
self.set_secure_cookie('uname','lisi',expires_days=3)

self.get_cookie('uname')
self.get_secure_cookie('uname')


# 自动获取密钥，放入cookie中
settings = {
	'cook_secret':'sfdsfsf'
}

def make_app():
    return tornado.web.Application([
        (r"/index", IndexHandler),
    ],**settings) 
```

## 模板语法

```
class TemplateHandler(RequestHandler):
    def get(self):
        # 方式一
        str = 'hello:{{name}}'   #在html中可以直接写改语法
        t = Template(str)
        content = t.generate(name='tom')
        self.write(content)
        
        # 方式二
        self.render('template.html',name='tom')


#设置模板文件前缀
settings = {
	'template_path':os.path.join(os.getcwd(),'templates')
}

def make_app():
    return tornado.web.Application([
        (r"/index", TemplateHandler),
    ],**settings) 
```

列表：{{list[0]}}

字典：dict.get('key1')

对象：obj.name

也可以直接传入函数

脚本传入(取消转义)：{{%raw html%}}

循环遍历：

```
{%for i in list%}

	{{i}}<br/>
{% end %}


{%for k,v in dict.items() %}

	{{k}}<br/>
{% end %}
```

条件判断：

````
{%if p == None%}
1
{%else%}
2
{%end%}
````

## csrf 防跨域

```
# 表单中添加
<form>
{% raw xsrf_form_html() %}
</form>


# 添加配置
settings = {
	'template_path':os.path.join(os.getcwd(),'templates')
	'xsrf_cookies':True
}
```

## 处理静态文件

```
<img src='/static/image0.png'/>或
<img src='{{static_url("image0.png")}}'/>
```



```
from tornado.web import StaticFileHandler

# 添加配置  方法二
settings = {
	'template_path':os.path.join(os.getcwd(),'templates')，
	'xsrf_cookies':True，
	'static_path':os.path.join(os.getcwd(),'static')，  # 方法二
}


def make_app():
    return tornado.web.Application([
        (r"/static/(.*)", StaticFileHandler,{'path':os.path.join(os.getcwd(),'static')}), #方法一
    ],**settings) 
```

## torndb

![](./images/Snipaste_2025-01-06_15-43-52.png)

https://www.cnblogs.com/aibabel/p/11480612.html

https://torndb.readthedocs.io/en/latest/#

conn.close()

不需要创建游标

## SQLAlchemy

操作对象的方式操作数据库

![](./images/Snipaste_2025-01-06_16-42-42.png)



### 建表

```
# coding=utf-8

# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.types import TypeDecorator,Integer,String

# 创建对象的基类:
Base = declarative_base()

# 自定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:配置引擎
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test',encoding='utf-8', echo=True)

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


# 创建数据库表，已经存在则不创建
Base.metadata.create_all()

# 删除数据库表
Base.metadata.drop_all()
```

### 连接池

避免频繁的连接_断开数据库操作

```
# 创建DBSession类型:连接池对象，默认5个连接
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()

# 创建新User对象:
new_user = User(id='5', name='Bob')

# 添加到session:
session.add(new_user)

# 提交即保存到数据库:
session.commit()

session.refresh()

#执行完毕， 关闭session:
session.close()
```

![](./images/Snipaste_2025-01-06_21-18-27.png)
echo=True ：表示打印信息

### 查询，排序

```
session.add_all(users)

# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
print('name:', user.name)

#多条件查询，and_,or_,not_
user = session.query(User).filter(and_(User.id=='5',User.name=='tom').one()

#降序
all_users = session.query(User).order_by(User.name.desc()).all()

#计数
num = session.query(User).count()

# 分页
datas = session.query(User).offset((num-1)*size).limit(size).all()

# 通过主键查询,get传入主键
user = session.query(User).get('lisi')

# 删除
user = session.query(User).filter(User.id=='5').delete()

#更新,或者利用更新对象属性，再add操作
user = session.query(User).filter(User.id=='5').update({User.name:'tom'})

#分组
from sqlalchemy.sql.functions import func
data = session.query(func.count(User.id),User.name).group_by(User.name).all()

# 查看部分字段
data = session.query(User.name.label(u'名字')).all()
```

### 公共装饰器

可以将公共部分创建连接池的操作提取为装饰器

```
def connwrapper(func):
	def _wrapper(*args,**kwargs)：
		from sqlalchemy.orm import sessionmaker
		
		engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test',encoding='utf-8', echo=True)
		DBSession = sessionmaker(bind=engine)
        session = DBSession()
        data = func(session,*args,**kwargs)
        session.close()
        
        return data
    return _wrapper
```

```
@connwrapper
def deleteUserById(session,id):
    user = session.query(User).filter(User.id=='5').delete()
    session.commit()
	pass
```

### 多表查询

![](./images/Snipaste_2025-01-06_21-07-45.png)

## 自定义session

tornado中不包含session相操作，需要自己定义

```
#coding=utf-8

import uuid
import pickle

class Session(object):
    def __init__(self):
        self.__session_id = str(uuid.uuid4().get_hex())
        self.cache ={}

    def get(self,key,default=None):
        return self.cache.get(key,default)

    def set(self, key,value):
        self.cache[key] = value

    def clear(self):
        self.cache.clear()

    @property
    def sessionid(self):
        return self.__session_id

    def serialize(self):
        # 序列化当前对象
        return pickle.dumps(self)

    @staticmethod
    def deserialize(str):
        return pickle.loads(str)


import redis
class SessionManage(Session):
    conn=redis.Redis(host='localhost', port=6379, db=0)

    @classmethod
    def cache2redis(cls,session):
        cls.conn.set(session.sessionid,session.serialize(),ex=60*60*24)

    @classmethod
    def getSessionById(cls,sessionid):
        rs = Session.deserialize(cls.conn.get(sessionid)) if cls.conn.get(sessionid) else None

        if not rs:
            rs = Session()
        return rs
```

## 异步非阻塞

Tornado 的定义是 Web 框架和异步网络库,其中他具备有异步非阻塞能力，能解决他两个框架请求阻塞的问题，在需要并发时候就应该使用 Tornado。



Tomado 异步使用方式 简而言之，Tomnado的异步包括两个方面,异步服务端和异步客户端。无论服务端和客户端,具体的异步模型又可以分为回调(callback)和协程(coroutine)。具体应用场景，也没有很明确的界限。往往一个请求服务里还包含对别的服务的套户端异步请求。



tornado.web.asynchronous的作用是保持长连接,也就是除非你主动调用self.finish()方法,否则requestHandler将不会返回
tornado.gen.coroutine是使用协程的方式实现类似异步的处理效果。

最新版的tornado,其实不一定需要写tornado.web.asynchronous装饰器

### 服务端

```
tornado.web.asynchronous    异步装饰器
tornado.gen.coroutine       协程装饰器
```

异步操作会利用回调函数处理

```
class IndexHandler(RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render('index.html')
        self.finish()   # 主动结束连接
```

```
from tornado.concurrent import Future

class IndexHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        yield self.read('index.html')
       
 	def read(self):
 		# 类似生成器中的send
 		future = Future()
 		future.set_result(aa)
 		return future
```

### 客户端
 同步客户端
 ```
from tornado.httpclient import AsyncHTTPClient, HTTPClient,HTTPRequest


# 同步请求
# 发送get请求
def get(url):
    http = HTTPClient()
    response = http.fetch(url)
    return response.body

# 发送post请求
def post(request):
    http = HTTPClient()
    response = http.fetch(request)
    return response.body


request = HTTPRequest(url='http://localhost:8080/index.html', method='Post',headers={'user-agent':'Mozilla/5.0'})
 ```

异步客户端

```
from tornado.httpclient import AsyncHTTPClient

def get(url,callback=None):
    http = AsyncHTTPClient()
    http.fetch(url,callback)

# 回调函数 处理耗时任务
def handle_callback(response):
    content = response.body


get('http://localhost:8080/index.html', callback=handle_callback)

tornado.ioloop.IOLoop.instance().start()  # 协程调度器
```

## websocket

独立创建再TCP上的协议，使用80端口，可以跳过大部分防火墙的限制

双工通信，不再需要客户端请求才能向客户端发送信息

![](./images/Snipaste_2025-01-06_23-26-54.png)
服务端：
```
from tornado.websocket import WebSocketHandler


class HelloHandler(WebSocketHandler):
    def open(self):
        pass
	
	#监听收到消息
    def on_message(self, message):
        print('Message received: %s' % message)
        self.write_message('已收到')

    def on_close(self):
        print('Connection closed')

    def check_origin(self, origin):
        # 允许跨域
        return True
```

客户端：

![](./images/Snipaste_2025-01-07_12-40-14.png)
