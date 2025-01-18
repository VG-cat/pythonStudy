## 安装

pip install flask

中文文档：https://dormousehole.readthedocs.io/en/latest/installation.html#python

## 虚拟环境

![](./images/Snipaste_2025-01-08_12-37-42.png)

## 基础使用

```
# coding=utf-8

from flask import Flask, render_template, request, redirect, url_for
#__name__  表示index.py文件
app = Flask(__name__)


#创建路由和视图函数的映射
@app.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':
    # debug 模式下热更新
    app.run(debug=True)
```

run中可以添加参数：

debug，是否启动调式

port:指定服务器端口，默认5000

host:服务器ip,0.0.0.0表示本机所有IP

## 配置信息

app.config

app.config['SECRET_KEY'] = 'FSFSD'

配置静态文件和模板文件(默认同名)：

app = Flask(\__name__,static_floder='',template_floder='')



```
或者从文件单独配置：
config.py:

SECRET_KEY = 'FSFSD' 
....


import config

app.config.from_object(config)
```

## 模板

jinja2模板语言

```
#创建路由和视图函数的映射
@blue.route('/')
def index():
    return render_template('index.html',name='zhangsan')

@blue.route('/api/01')
def api01():
    #json序列化
    return dumps({'message': 'Hello World!'})
```

```
{{ var}}   变量
{{% tag%}}  标签
{#  注释 #}


{% if %}
{% endif %}

{% for i in list%}
{{i}}
{{loop.index}} # 下标
{{loop.revindex}}
{% endfor%}
```

 ```
 # 继承
 父：base.html
 {% block blockname%}
 {% endblock%}
 
 
 子：child.html
 {% extends 'base.html'%}
 
 {% block blockname%}
 {{ super()}}  # 显示父内容
 <h1>你好</h1>
 {% endblock%}
 ```

```
# 导入其他页面
{% include '2.html'%}
```

```
# 宏定义函数
{% macro person(name) %}
{{name}}---
{% endmacro%}

#使用
{{person('tom')}}

#导入
{% from 'xx' import xx %}
```

```
# 过滤器
{{变量 | 过滤器 | 过滤器}}

#常见过滤器
lower
upper 
title
captializa
sum
sort
first
last
default('vc')
...
```



## 蓝图

蓝图是一种规划，只用用来规划urls,路由

蓝图的基本使用：

1、在views中初始化蓝图

```
from flask import Blueprint
blue = Blueprint('user',__name__)
```

2、在init文件中将蓝图进行注册

app.register_blueprint(blueprint = blue)

## 路由参数

 ```
 @blue.route('/temp/<string:parm>/')  # 不支持包含/的字符串
 @blue.route('/temp/<int:parm>/')
 @blue.route('/temp/<float:parm>/')
 @blue.route('/temp/<path:parm>/')   # 支持包含/的字符串
 @blue.route('/temp/<uuid:parm>/')   # uuid:32位16进制
 @blue.route('/temp/<any（apple,orange）:parm>/')   # any表示泛型
 ```

```
@blue.route('/temp/<int:parm>/',method=['GET','POST'])
```

## 请求和响应

request请求对象

![](./images/Snipaste_2025-01-08_14-38-09.png)

```
@blue.route('/temp/<int:parm>/',method=['GET','POST'])
def temp(id):
	print(request.method)
	print(request.args)   返回类字典对象
	print(request.args.get('name'))   返回类字典对象
```

 

response响应对象

返回字符串

返回模板

返回json

返回自定义response对象

```
res = make_response('{hello}',200)
res = Response('{hello}',200)
```

## 重定向

 ```
 @blue.route('/')
 def test():
 	# return redirect('hhtp://www.baidu.com')
 	# return redirect('/index')
 	
 	ret = url_for('user.index'，name='ss')   # 蓝图.视图函数名，--反向解析
 	return redirect(ret)
 ```

## 会话技术

### cookie

客户端会话技术，存在客户端

作用是让服务器认识浏览器，常用于登录

![](./images/Snipaste_2025-01-08_15-45-18.png)

### session

服务器端会话技术，存在服务端，session的实现依赖cookie

![](./images/Snipaste_2025-01-08_16-23-41.png)

 

## 模型

借助插件 flask-sqlalchemy实现orm

flask-sqlalchemy实现ORM

flask-migrate 实现数据迁移

pymysql MySQL的驱动

![](./images/Snipaste_2025-01-08_20-16-54.png)

### 数据迁移

生成数据库表结构

先在终端进入app.py所在的目录（项目目录）

输入命令：

```
flask db init      # 创建迁移文件夹migrate，只需要执行一次
flask db migrate   # 生成迁移文件，将类转化为sql语句
flask db upgrade   # 执行迁移文件
flask db downgrade # 撤销上次操作
```

第一次使用时，需要下载数据库驱动

### 单表操作

```
@blue.route('/api/02/<string:name>')
def api02(name):
    # 添加一条数据
    user = User()
    user.name = name
    db.session.add(user)  # 添加到session
    
    # db.session.add_all(users)  #添加多条时，参数则换为列表
    db.session.commit()  #同步到数据库
    
    db.session.rollback()  #回滚
    db.session.flush()   #清空缓存
```

```
u = User.query.first()
db.session.delete(u)
db.session.commit()
```

![](./images/Snipaste_2025-01-08_21-14-34.png)

![](./images/Snipaste_2025-01-08_21-15-07.png)

### 分页

```
@blue.route('/api/03')
def api02():
    u = User.query.paginate(page=1, per_page=5, error_out=False)

    print(u.items)
    print(u.has_next)
```

![](./images/Snipaste_2025-01-08_22-09-16.png)

page从1开始记录

### 一对多

```
class Grade(db.Model):
	__tablename__ = 'grade'
	
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	name = db.Column(db.String(30),unique =True)
	
	# 建立关系，允许反向查询
	# 第一个参数：要建立联系的对象名
	# 第二个参数：反向引用名称，允许student通过grade属性，反向获取Grade全部信息（name,id..)
	# 第三个参数：懒加载，被调用时才会建立联系
	# grade.student  即查询所有相关的所有学生
	# student.grade  学生反向查询班级
	student = db.relationship('Student'，backref='grade'，lazy=True)
	

class Student(db.Model):
	__tablename__ = 'student'
	
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	name = db.Column(db.String(30),unique =True)
	
	# 外键
	gradeid = db.Column(db.Integer,db.ForeignKey(Grade.id))

```

![](./images/Snipaste_2025-01-08_23-11-09.png)

### 多对多

需要三张表

```

#用户收藏表，中间表
collection = db.Table(
	'collection',  #表名
	db.Column('user_id',db.Integer,primary_key=True,db.ForeignKey('user.id'))   # user 小写
	db.Column('movie_id',db.Integer,primary_key=True,db.ForeignKey('movie.id'))   # user 小写
)


#用户表
class User(db.Model):
	__tablename__ = 'user'
	
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	name = db.Column(db.String(30),unique =True)
	
	# 反向关联，两个表写一个即可,并传入中间表
	movies = db.relationship('Movie'，backref='users'，lazy=True，secondary=collection)
	
# 电影表	
class Movie(db.Model):
	__tablename__ = 'movie'
	
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	name = db.Column(db.String(30),unique =True)
	
```

```
# 增加

user = User.query.get(1)
movie = Movie.query.get(1)
user.movies.append(movie)
db.session.commit()


# 查询
user.movies  #正向
movie.users  #反向
```

##  插件

### flask-caching



```
# coding='utf-8'  插件管理

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

# 数据库初始化
db = SQLAlchemy()
migrate = Migrate()
cache = Cache(
    config={'CACHE_TYPE': 'SimpleCache'},
)


# 和app绑定
def init_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)
```

```
@blue.route('/api/03')
@cache.cached(timeout=10)   #10秒之内从缓存获取
def api02():
    u = User.query.paginate(page=1, per_page=5, error_out=False)

    print(u.items)
    print(u.has_next)
```

### flask-mail 发送邮箱验证码

```
from flask_mail import Mail

mail = Mail()

mail.init(app)

...
```

```
from flask_mail import Message
message = Message(subject='主题'，recipients=['2222@qqq'],body='测试消息')
mail.send(message)
```



## 钩子函数（中间件）

在执行函数和目标函数之间挂载的函数，框架开发者为调用者提供了一个point-挂载点，是一种AOP切面编程的思想。

![](./images/Snipaste_2025-01-09_15-03-41.png)

```
@blue.before_request
def before_request():
    print(request.endpoint)
    # return 'ee'  之间return则不会继续执行
```

## 内置对象

![](./images/Snipaste_2025-01-09_15-19-20.png)

## 前后端分离

直接返回json或者利用插件flask-restful

flask-restful对增删改查操作进行了封装

此时不再需要蓝图处理，不再需要模板

### 类视图

```
# coding='utf-8'
# api文件
from flask_restful import Resource


# 类视图 CBV  ： class base view
# 函数视图 FBV
class HelloWorld(Resource):
    def get(self):
        return 'Hello World'

    def post(self):
        pass
```



### 字段格式化

```
from flask_restful import Resource,fields,marshal_with
```

![](./images/Snipaste_2025-01-09_16-42-49.png)

user: fields.Nested(sub_fields)  嵌套子结构

list: fields.List(fileds.Nested(sub_fields))  列表格式

```
class User(Resource):
	@marshal_with(user_fileds)
	def get(self):
		return {'msg':'成功'，'age':22}
```

![](./images/Snipaste_2025-01-09_17-04-20.png)

在其他路由上添加endpoint，会在格式化字段中返回该路由

### 参数解析

解析前端返回的参数

```
from flask_restful import Resource,reqparse
```

```
parser = reqparse.RequestParser()
parser.add_argument('name',type=str,required=True,help="不能为空.")
parser.add_argument('age',type=str,action='append') # 可以有多个age

class HelloWorld1(Resource):
    def get(self):
        arg = parser.parse_args()
        name = arg['name']
        return name
```

## 项目结构

![](./images/Snipaste_2025-01-09_17-26-33.png)

前后端分离时，不需要views,templates,不需要蓝图处理

### app.py

```
# coding=utf-8
from App import  create_app

if __name__ == '__main__':
    app = create_app()
    # debug 模式下热更新
    app.run(debug=True)
```

### init.py

```
# coding='utf-8'

# 初始化文件 创建flask应用，导包后会自动执行

from flask import Flask
from .views import blue
from .extensions import init_extensions
from .urls import  *

def create_app():
    app = Flask(__name__)

    #注册蓝图
    app.register_blueprint(blue)

    # 配置数据库
    db_uri = 'sqlite:///test.db'
    # db_uri = 'mysql+pymysql://root:123456@localhost:3306/test'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   #禁止对象追踪修改

    # 初始化插件
    init_extensions(app)

    return app
```



### views.py

```
# coding='utf-8'

# 存放 视图和映射函数


from flask import Flask, render_template, request, redirect, url_for
from json import dumps

# 利用蓝图 管理 app路由，使得整个项目共用一个app
from flask import Blueprint

from .models import  *
from .extensions import cache

blue = Blueprint('user', __name__)
blue2 = Blueprint('product', __name__)

#创建路由和视图函数的映射
@blue.route('/')
def index():
    return render_template('index.html',name='zhangsan')

@blue.route('/api/01')
def api01():
    #json序列化
    return dumps({'message': 'Hello World!'})


@blue.route('/api/02/<string:name>')
def api02(name):
    # 添加一条数据
    user = User()
    user.name = name
    db.session.add(user)  # 添加到session
    db.session.commit()  #同步到数据库


@blue.route('/api/03')
@cache.cached(timeout=10)   #10秒之内从缓存获取
def api03():
    u = User.query.paginate(page=1, per_page=5, error_out=False)

    print(u.items)
    print(u.has_next)


#钩子函数
# @blue.before_request
# def before_request():
#     print(request.endpoint)
#     return 'ee'


@blue.route('/detail/<id>')
def detail(id):
    return 'hello world {0}'.format(id)
```



### models.py

```
# coding='utf-8'   对接数据库
from .extensions import db

class User(db.Model):
    __tablename__ = 'flask_users'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

```



### urls.py

```
# coding='utf-8'
# 前后端分离 ：路由文件

from .api import HelloWorld,HelloWorld1
from .extensions import api


# 配置路由
api.add_resource(HelloWorld, '/')
api.add_resource(HelloWorld1, '/hello1/')


```



### api.py

```
# coding='utf-8'
# api文件
from flask_restful import Resource,fields,marshal_with,reqparse


# 类视图 CBV  ： class base view
# 函数视图 FBV
class HelloWorld(Resource):
    def get(self):
        return 'Hello World'

    def post(self):
        pass

# 参数转化器
parser = reqparse.RequestParser()
parser.add_argument('name',type=str,required=True,help="不能为空.")

class HelloWorld1(Resource):
    def get(self):
        arg = parser.parse_args()
        name = arg['name']
        return name
```



### extensions.py

```
# coding='utf-8'  插件管理

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_restful import Api

# 数据库初始化
db = SQLAlchemy()
migrate = Migrate()
api = Api()
cache = Cache(
    config={'CACHE_TYPE': 'SimpleCache'},
)


# 和app绑定
def init_extensions(app):

    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)
    api.init_app(app)
```

