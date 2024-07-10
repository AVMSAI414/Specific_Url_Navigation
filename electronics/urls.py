from django.urls import path
from electronics.views import *
app_name="Elect"

urlpatterns = [
    path("samsung/",samsung,name="samsung"),
    path("oppo/",oppo,name="oppo"),
]
