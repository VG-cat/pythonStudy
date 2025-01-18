from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo
# Create your views here.


def index(request):

    # 实现业务逻辑
    #1.先把所有书籍查询出来
    # select * from bookinfo
    # ORM
    books = BookInfo.objects.all()
    # books = [BookInfo(),BookInfo()]
    #2.组织数据
    context = {
        'books':books
    }

    reslut = 10/0

    #3.将组织号的数据传递给模板
    return render(request,'index.html',context)
    return HttpResponse('~~~~~~~~~~')