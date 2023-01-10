from django.urls import path
from time_app.views import set_timezone, get_time

urlpatterns = [
    path("", get_time, name="time"),
    path("timezone/", set_timezone, name="set_time"),
]
