from django.conf.urls import url
from . import views
from users.views import logout_view

urlpatterns = [
    url(r'^$', views.homepage, name="homepage"),
    url(r'workouts/(?P<userID>\d+)/$', views.workouts, name="workouts"),
    url(r'logout/$', logout_view, name="workouts"),
    url(r'public_logs/$', views.public_logs, name="public_logs"),
    url(r'public_log/(?P<userID>\d+)/$', views.public_log, name="public_log")
]
