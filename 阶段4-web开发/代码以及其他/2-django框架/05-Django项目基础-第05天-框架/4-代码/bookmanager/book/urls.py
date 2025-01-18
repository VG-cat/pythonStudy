from django.conf.urls import url
from book.views import index
urlpatterns = [
    #index/
    # url的第一参数是:正则
    # url的第二参数是:视图函数名
    #pay/order/
    url(r'^index/$',index),
]