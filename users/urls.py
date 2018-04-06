from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
from homepage.views import homepage

urlpatterns = [

    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^homepage/$', homepage, name='homepage'),

]
