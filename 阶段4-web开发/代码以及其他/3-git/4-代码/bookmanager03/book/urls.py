from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^set_session/$',views.SetSession.as_view()),
    url(r'^get_session/$',views.GetSession.as_view()),
    url(r'^login/$',views.LoginView.as_view()),
]