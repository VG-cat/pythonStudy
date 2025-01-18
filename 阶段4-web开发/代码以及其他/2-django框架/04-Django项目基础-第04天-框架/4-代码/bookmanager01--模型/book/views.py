from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo
# Create your views here.


def index(request):

    # 1.到数据库中查询书籍
    books= BookInfo.objects.all()
    for book in books:
        print(book)


    # 此处省略了很多代码

    for book in books:
        print(book)


    #

    for book in books:
        print(book)

    #############################
    for book in BookInfo.objects.all():
        print(book)

    #2.组织数据
    context = {
        'books':books
    }
    #3.传递给模板
    return render(request,'index.html')

    return HttpResponse('index')

"""

缓存
    内存:     存储容量小,读取速度快,断电即失
    硬盘:     存储容量大,读取速度慢,断电保存

当前缓存的概念:
    我们将硬盘的数据 存在在内存中,这样读取速度就很快

"""

"""
类似于 ipython的东西
python manage.py shell
"""




