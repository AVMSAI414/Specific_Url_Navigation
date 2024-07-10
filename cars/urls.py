from django.urls import path
from cars.views import *
app_name="car"
urlpatterns = [
    path("rolls_royce/",rolls_royce,name="rolls_royce"),
]
