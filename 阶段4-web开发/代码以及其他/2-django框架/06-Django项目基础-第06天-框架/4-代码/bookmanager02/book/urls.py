from django.conf.urls import url
from book.views import index,detail,set_cookie,get_cookie,set_session,get_session
from book.views import BookView,CenterView,HomeView

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

    # cookie的第一次请求
    url(r'^set_cookie/$',set_cookie),

    # cookie的第二次及其之后的请求
    url(r'^get_cookie/$',get_cookie),


    url(r'^set_session/$',set_session),
    url(r'^get_session/$',get_session),


    # url的第一个参数是 正则
    # url的第二个参数是 视图函数名
    url(r'^login/$',BookView.as_view()),


    url(r'^center/$',CenterView.as_view()),


    url(r'^index/$',HomeView.as_view()),
]