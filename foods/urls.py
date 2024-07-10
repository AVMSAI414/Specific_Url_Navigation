from django.urls import path
from foods.views import *
app_name="foods"

urlpatterns = [
    path("sambar/",sambar,name="sambar"),
    path("biryani/",biryani,name="biryani"),
]
