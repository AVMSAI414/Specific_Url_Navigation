from django.shortcuts import render

# Create your views here.
def benz(request):
    return render(request,"benz.html")

def rolls_royce(request):
    return render(request,"rolls_royce.html")