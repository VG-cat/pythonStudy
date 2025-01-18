from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$',views.LoginView.as_view()),
    url(r'^rece/$',views.ReceiveView.as_view()),


]