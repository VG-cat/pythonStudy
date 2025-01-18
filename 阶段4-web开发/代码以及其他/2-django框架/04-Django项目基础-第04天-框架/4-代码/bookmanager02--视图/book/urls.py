from django.conf.urls import url
from book.views import index,detail,set_cookie

urlpatterns = [
    # name 就是给url起一个名字
    # 我们可以通过name找到这个路由
    url(r'^home/$',index,name='index'),

    #http://127.0.0.1:8000/分类id/书籍id/
    #http://127.0.0.1:8000/category_id/book_id/
    #分组来获取正则中的数据
    #根据位置来获取 url中的参数
    # url(r'^(\d+)/(\d+)/$',detail),

    #关键字参数--推荐大家使用关键字参数
    url(r'^(?P<category_id>\d+)/(?P<book_id>\d+)/$',detail),

    url(r'^set_cookie/$',set_cookie),
]