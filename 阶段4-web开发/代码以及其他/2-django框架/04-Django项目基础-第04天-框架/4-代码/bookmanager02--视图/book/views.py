import json

from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def index(request):

    """
    reverse  就是通过 name 来动态获取路径(路由)
    如果没有设置namespace 则可以通过name来获取 reverse(name)
    如果有设置namespace 则可以通过namespace:name来获取 reverse(namespace:name)

    # 登陆成功之后需要跳转到首页
    # 注册成功之后需要跳转到首页
    """
    # viewname 通过视图名字
    # 路由是动态获取的
    # path = reverse('index')
    # print(path)

    #如果我们设置了namespance 这个时候就需要通过 namespace:name 来获取路由
    # path=reverse('book:index')
    # print(path)
    # 跳转页面
    # 登陆成功之后需要跳转到首页
    # return redirect('/home/')
    # return redirect(path)


    # 注册成功之后需要跳转到首页
    # return redirect('/home/')
    # return redirect(path)


    return HttpResponse("index")



def detail(request,book_id,category_id):

    # 1/100/
    # print(category_id,book_id)


    ###########################GET 查询字符串#################################
    """
    https://www.baidu.com/s?ie=utf-8&wd=itcast&rsv_pq=fdf543ed000f8688&rsv_t=8862Eb1lxc9858Ihke7VdJylicTyYs%2F3EuFyVPKcOBnv9wmTxLdhwlYL6%2F8&rqlang=cn&rsv_enter=1&rsv_sug3=5&rsv_sug1=4&rsv_sug7=100

    以? 作为一个分隔
    ?前边 表示 路由
    ?后边 表示 get方式传递的参数 称之为 查询字符串
    ?key=value&key=value...

    我们在登陆的时候会输入用户名和密码 理论上 用户名和密码都应该以POST方式进行传递
    只是为了让大家好理解,我们接下来 用 get方式来传递用户名和密码
    """

    # query_params = request.GET
    # print(query_params)
    # #QueryDict: {'username': ['itcast'], 'password': ['123']}
    #
    # #QueryDict
    # #<QueryDict: {'username': ['itcast', 'itheima'], 'password': ['123']}>
    #
    # # QueryDict 以普通的字典形式来获取 一键多值的是时候 只能获取最后的那一个值
    # # 我们想获取 一键一值的化 就需要使用 QueryDict 的get方法
    # # 我们想获取 一键多值的化 就需要使用 QueryDict 的getlist方法
    # username=query_params['username']
    # password=query_params.get('password')
    #
    # # print(username,password)
    #
    # # print(username)
    #
    # users = query_params.getlist('username')
    # print(users)

    ###########################POST 表单数据#################################

    # data = request.POST
    # print(data)

    ###########################POST json数据#################################
    """
    JSON 是双引号
    {
        "name":"itcast"
    }
    """

    # print(request.POST)
    # body=request.body
    # b'{\n    "username":"itcast",\n    "passwrod":"123"\n}'
    # body_str = body.decode()  # JSON形式的字符串
    """
    {
        "username":"itcast",
        "passwrod":"123"
    }
    """
    # print(type(body_str))
    # print('~~~~~~~')
    # print(body_str['username'])

    """
    json
    json.dumps   将字典转换为 JSON形式的字符串
    json.loads   将JSON形式的字符串 转换为字典
    """
    # data = json.loads(body_str)
    # print(data)
    ###########################请求头#################################

    # print(request.META)
    #
    # content_type=request.META['CONTENT_TYPE']
    # print(content_type)

    # print(request.method)
    #
    # print('我是有底线的~~~')

    ###########################跳转页面#################################

    # 需求是跳转到首页
    # 通过reverse 这个名字来找到路径
    path = reverse('book:index')
    return redirect(path)

    return redirect('/index/')

    return redirect('http://www.itcast.cn')

    ###########################JsonResponse#################################
    from django.http import JsonResponse
    data = {'name': 'itcast'}

    return JsonResponse(data)

    ###########################HttpResponse#################################
    data = {'name':'itcast'}
    # HttpResponse
    # content       传递字符串 不要传递 对象,字典等数据
    # statue        HTTP status code must be an integer from 100 to 599. 只能使用系统规定的
    # content_type  是一个MIME类型
    #               语法形式是: 大类/小类
    #   text/html   text/css    text/javascript
    #   application/json
    #   image/png   image/gif   image/jpeg
    return HttpResponse(data,status=400)


"""
保存在客户端的数据叫做 cookie
    0.概念
    1.流程(原理)

        第一次请求过程
        ① 我们的浏览器第一次请求服务器的时候,不会携带任何cookie信息
        ② 服务器接收到请求之后,发现 请求中没有任何cookie信息
        ③ 服务器设置一个cookie.这个cookie设置在相应中
        ④ 我们的浏览器接收到这个相应之后,发现相应中有cookie信息,浏览器会将cookie信息保存起来

        第二次及其之后的过程
        ⑤ 当我们的浏览器第二次及其之后的请求都会携带cookie信息
        ⑥ 我们的服务器接收到请求之后,会发现请求中携带的cookie信息,这样的话就认识是谁的请求了

    2.看效果
    3.从http协议角度深入掌握cookie的流程(原理)

保存在服务器的数据叫做 session

"""

def set_cookie(request):

    #1. 先判断有没有cookie信息
    # 先假设就是没有

    #2.获取用户名
    username=request.GET.get('username')
    #3. 因为我们假设没有cookie信息,我们服务器就要设置cookie信息
    response = HttpResponse('set_cookie')

    # key,value
    response.set_cookie('username',username)


    #4.返回相应
    return response
