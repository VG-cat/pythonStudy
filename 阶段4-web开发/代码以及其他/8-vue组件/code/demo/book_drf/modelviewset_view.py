from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from QQLoginTool.QQtool import OAuthQQ
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination

from book_drf.serializer import BookSerialzier
from books.models import BookInfo
from django.db import DatabaseError

class PageNum(PageNumberPagination):
    """
        自定义分页器
    """
    page_size_query_param = 'page_size' # 指定控制每页数量的参数
    max_page_size = 6 # 指定每页最大返回数量



class Books(ModelViewSet):
    queryset = BookInfo.objects.all()  # 指定当前类视图使用的查询集数据
    # serializer_class = BookSerialzier  # 指定当前类视图使用的序列化器
    # 认证
    authentication_classes = (BasicAuthentication,SessionAuthentication)
    # 权限
    permission_classes = (IsAuthenticated,)

    # 用户限流
    # throttle_classes = [UserRateThrottle]
    # 限流
    # throttle_scope = 'uploads'
    # 指定过滤字段
    # filter_fields=('btitle','bread')
    # 指定排序方法类
    filter_backends = [OrderingFilter]
    # 指定排序字段
    ordering_fields=('id','bread')
    # 指定分页器
    pagination_class = PageNum



    def get_serializer_class(self):
        if self.action =='lastdata':
            return BookSerialzier
        elif self.action=='create':
            return BookSerialzier
        else:
            return BookSerialzier

    @action(methods=['get'],detail=True)
    def lastdata(self,request,pk):
        raise DatabaseError
        print(self.action)
        book=BookInfo.objects.get(id=pk)
        ser=self.get_serializer(book)
        return Response(ser.data)


