from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.
"""
视图
1.就是python函数
2.函数的第一个参数就是 请求  和请求相关的 它是 HttpRequest的实例对象
3.我们必须要返回一个相应   相应是 HttpResponse的实例对象/子类实例对象
"""


def index(request):
    name = '志玲姐姐 '
    #request, template_name, context=None
    # 参数1: 当前的请求
    # 参数2: 模板文件
    # 参数3:context 传递参数

    context = {
        'name':name
    }

    return render(request,'index.html',context)

    return HttpResponse('index')