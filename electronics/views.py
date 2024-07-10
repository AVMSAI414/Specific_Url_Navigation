from django.shortcuts import render

# Create your views here.
def samsung(request):
    return render(request,"samsung.html")


def oppo(request):
    return render(request,"oppo.html")