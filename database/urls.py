from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^workout_data/$', views.All_Workout_Data.as_view(), name='All_Workout_Data'),
    url(r'^workout_data/(?P<userID>\d+)/$', views.Workout_Data.as_view(), name='Workout_Data'),
]
