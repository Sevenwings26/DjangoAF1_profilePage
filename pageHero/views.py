from django.shortcuts import render

# Create your views here.

def landingPage(request):
    return render (request, "landingpage.html" )

def visionPage(request):
    return render(request, 'vision.html')