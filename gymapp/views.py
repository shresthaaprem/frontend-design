from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'app/index.html')

def About(request):
    return render(request,'app/about.html')

def FrontEnd(request):
    return render(request,'app/frontend/index.html')