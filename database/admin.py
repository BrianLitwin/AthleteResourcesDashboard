from django.contrib import admin

# Register your models here.

from .models import Workouts, Settings, Metric_Info, Exercises, Exercise_Metrics, EM_Containers, Sequences

admin.site.register(Workouts)
admin.site.register(Sequences)
admin.site.register(Exercises)
admin.site.register(EM_Containers)
admin.site.register(Exercise_Metrics)
admin.site.register(Metric_Info)
admin.site.register(Settings)
