from django.shortcuts import render

# Create your views here.
def biryani(request):
    return render(request,"biryani.html")

def sambar(request):
    return render(request,"sambar.html")