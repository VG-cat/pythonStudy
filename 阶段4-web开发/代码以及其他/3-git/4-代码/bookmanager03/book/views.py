from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class SetSession(View):

    def get(self,request):

        # request.session=SessionStorage
        # 增加数据
        # request.session['name']='itcast'
        request.session['name']='12345678901234567892345678923456782345678234789234567892345678234567823478923456789234567823456782347892345678923456782345678234789234567892345678234567823456789'
        request.session['photo']='http://www'
        request.session['id']='123'
        # 删除某一个数据
        # del request.session['name']

        # 删除session的所有数据,保留key
        # request.session.clear()

        # 把数据库/redis中的key 都删除了
        # request.session.flush()

        # session是有时间的 默认是2周
        # 我们可以设置时间
        # request.session.set_expiry(sencods)
        request.session.set_expiry(10)



        return HttpResponse('abc')


class GetSession(View):

    def get(self,request):

        # 获取数据
        # dict['key']
        # dict.get('key') v
        # name = request.session['name']
        name = request.session.get('name')
        print(name)

        return HttpResponse('get session')



class LoginView(View):

    def get(self,request):
        return render(request, 'login.html')
        return HttpResponse('get')


    def post(self,request):



        return HttpResponse('post')
