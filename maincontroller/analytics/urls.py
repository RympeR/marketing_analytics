from django.urls import path, include
from .views import *
from analytics.dash_apps.finished_apps import simpleexample


app_name = 'analytics'

urlpatterns = [
    path('', index, name='analytics-index')
]
